---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# The Problem

My internship project, **awsplace**, is hosted on a GitLab instance that I set up myself at `git.namanhishere.com`. That is the only git remote of the repository. Every pipeline action involving AWS starts from here: pushing the container image to Amazon ECR, running `npx cdk deploy` for the `AwsplaceStack`, uploading the frontend bundle to Amplify Hosting, and forcing a new deployment on ECS.

The most obvious way to do this is to create an IAM user, generate an access key pair, and paste `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` into the project's CI/CD variables. It takes two minutes and works perfectly the first time. I don't want to do that, for very specific reasons, not just theoretical ones.

A stored access key does not expire on its own. My key would reside in the variable store of a self-hosted GitLab instance on a machine at my house, with no key rotation process behind it. Every job in the pipeline would inherit it, including the jobs that build the C++ datastore image and run four contract tests against that image—jobs that have absolutely no business talking to AWS. And if the key were to leak—through a misplaced `set -x`, a third-party CI plugin, or a compromised runner—the scope of damage would extend indefinitely until I notice it and manually revoke it.

Therefore, the pipeline holds no AWS keys whatsoever. The only AWS-related value stored in GitLab is `${AWS_ROLE_ARN}`, which is a role reference, not a credential. Knowing it doesn't grant anyone any permissions.

# How the Trust Relationship is Established

GitLab can act as an OpenID Connect identity provider. For any job that declares the `id_tokens` keyword, GitLab generates a short-lived JWT, signed with its own key, and injects it into that specific job's environment. The token is never written to the repository and never saved as an artifact.

On the AWS side, there are two entities. First is an IAM OIDC identity provider registered for the issuer URL `https://git.namanhishere.com`, which allows IAM to fetch the JWKS document and verify the signature on tokens issued by my GitLab. Second is an IAM role with a trust policy that designates that provider as the principal and limits which tokens are allowed to assume the role.

The audience is more important than it looks. In `.gitlab-ci.yml`, I declare it explicitly:

```yaml
id_tokens:
  AWS_JWT_TOKEN:
    aud: https://git.namanhishere.com
```

All three jobs that need credentials declare that exact value, so here `aud` and `iss` are the same string. This is a deliberate choice, and it comes with a trade-off that needs to be stated plainly: an audience that matches the issuer is a weaker constraint than a consumer-specific audience, such as `sts.amazonaws.com`, because it cannot distinguish between "a token intended for AWS" and "a token intended for anything else trusting my GitLab." Currently, AWS is the only OIDC relying party in the project, so this difference only exists on paper. If I were to add a second relying party, the first thing I'd have to do is separate the audiences.

<figure>
  <img src="/images/3-BlogPosted/iam-oidc.png" alt="AWS IAM Console showing the git.namanhishere.com OpenID Connect identity provider with exactly one registered audience" loading="lazy">
  <figcaption>The IAM identity provider for my GitLab instance, with exactly one registered audience. This is the <code>aud</code> value that all three credential-bearing jobs request; separating it is a prerequisite for a second relying party.</figcaption>
</figure>

The trust policy is where the actual authorization resides. It performs an absolute string match on the audience and a pattern match on the subject, so a token generated for a different project or a different branch of the same project cannot assume the role, even if the signature is perfectly valid:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/git.namanhishere.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "git.namanhishere.com:aud": "https://git.namanhishere.com"
        },
        "StringLike": {
          "git.namanhishere.com:sub": "project_path:namanhishere/awsplace:ref_type:branch:ref:main"
        }
      }
    }
  ]
}
```

The Account ID is hidden throughout this article. The `sub` claim is what does the real work: GitLab constructs it from the project path, ref type, and ref name. Pinning it to `ref:main` is what prevents a branch or a fork from generating its own credentials to deploy. A valid signature does not equate to granted permissions.

<figure>
  <img src="/images/3-BlogPosted/gitlab-oidc-trust.svg" alt="Sequence diagram depicting a GitLab CI job exchanging a signed OIDC token for temporary AWS credentials via IAM and STS" loading="lazy">
  <figcaption>The entire handshake process, from declaring <code>id_tokens</code> to a 3600-second STS session. Each step includes the corresponding line in <code>.gitlab-ci.yml</code>.</figcaption>
</figure>

# Job Configuration

The token exchange step itself is just an `aws-cli` command. This is the `before_script` of the `push-ecr` job, which builds the Go application image and pushes it to ECR:

```yaml
before_script:
  - >
    ASSUME_ROLE_OUTPUT=$(aws sts assume-role-with-web-identity
    --role-arn ${AWS_ROLE_ARN}
    --role-session-name "GitLabCI-${CI_PIPELINE_ID}"
    --web-identity-token ${AWS_JWT_TOKEN}
    --duration-seconds 3600
    --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]"
    --output text)
  - export AWS_ACCESS_KEY_ID=$(echo "$ASSUME_ROLE_OUTPUT" | awk '{print $1}')
  - export AWS_SECRET_ACCESS_KEY=$(echo "$ASSUME_ROLE_OUTPUT" | awk '{print $2}')
  - export AWS_SESSION_TOKEN=$(echo "$ASSUME_ROLE_OUTPUT" | awk '{print $3}')
```

The folded scalar `- >` is the reason this command reaches the shell as a single line despite spreading across seven YAML lines.

Three details in the command above carry their own weight. `--web-identity-token` only accepts the injected `${AWS_JWT_TOKEN}` and nothing else, so no secrets are interpolated from the variable store. `--role-session-name` embeds `${CI_PIPELINE_ID}`, meaning every session appearing in CloudTrail can be traced back to a specific pipeline; the `publish-raftdb-image` job uses `"GitLabCI-${CI_PIPELINE_ID}-RaftDB"`, so its actions are distinguishable from the application image push. And `--query` combined with `--output text` returns the three credential fields as tab-separated text, which the three `export` lines then extract using `awk`. No credentials are ever printed to the logs.

Once those variables are exported, the rest of the job just uses standard AWS tooling. Logging into the registry uses a token derived from that very session:

```bash
aws ecr get-login-password --region "$AWS_REGION" | \
  docker login --username AWS --password-stdin "$ECR_REGISTRY"
```

`get-login-password` prints the password to stdout, and piping it into `--password-stdin` keeps it from being exposed on the process table or in the job logs. It expires along with the session, just like everything else here.

# What the Credentials Can and Cannot Do

The session is granted for 3600 seconds. When the pipeline ends, the credentials become useless, and there's nothing left to rotate or revoke. That number hasn't been fine-tuned; it's the same `--duration-seconds 3600` across all three jobs, and it's longer than the actual needs of a single run. Tightening it per job would further narrow the window of risk, at the cost of a failed deployment if a CDK deploy takes longer than the lifespan of its own credentials.

What the session is allowed to do depends on the role's permission policy, and this is the true weakness of my current setup. A single role serves all three jobs, so `push-ecr` runs with the exact same permissions as `deploy-to-aws`, a job that requires CloudFormation, ECS, Amplify, Secrets Manager, EFS, S3, and Route 53 to build the `AwsplaceStack`. The identity is short-lived, but the permissions granted to it are by no means narrow. Federation has eliminated the issue of stored secrets, but it hasn't eliminated the issue of overly broad permissions, and I shouldn't pretend otherwise.

Three jobs declare `id_tokens`: `push-ecr`, `publish-raftdb-image`, and `deploy-to-aws`. Everything else in the pipeline runs without any AWS identity whatsoever, and that is the truly interesting half of the design.

<figure>
  <img src="/images/3-BlogPosted/gitlab-ci.png" alt="GitLab Pipeline #73 in job dependencies view, showing fourteen jobs across the build-ci-image, test, build, and deploy stages" loading="lazy">
  <figcaption>Pipeline #73 on <code>main</code>: 14 jobs, 35 minutes. Three of those jobs hold an AWS identity. The other eleven, including <code>raftdb-image</code>, hold nothing.</figcaption>
</figure>

# Chain of Custody

This is the part I'm truly willing to defend in a review session.

The RaftDB container image is the production datastore for awsplace. `raftdb-image` is the job that builds it, and that job has no `id_tokens` block, no role ARN, and no way to touch AWS. It runs in the `test` stage on `docker:27-cli`, builds `raftdb:${CI_COMMIT_SHA}`, and runs four contract tests against the newly built image: `container_contract_test.sh`, `qualification_runtime_contract_test.sh`, `migration_runtime_contract_test.sh`, and `s3_runtime_contract_test.sh`. It installs Trivy 0.72.0 by downloading the release archive along with its checksums file, verifying the checksums file against a hardcoded sha256 in the pipeline, and only then verifying the archive against the checksums file. It records the Docker image ID before and after the scan and fails if they differ, because a scanner has no reason to mutate the very artifact it's inspecting. Any CRITICAL finding fails the job immediately. A HIGH finding does too, unless `RAFTDB_ACCEPT_HIGH_CVES` is set exactly to the `$CI_COMMIT_SHA` being built, turning risk acceptance into a decision for a specific commit rather than a switch someone flips and forgets.

The significance of not granting credentials to that job is this: a hijacked build step still has nowhere to push. A malicious dependency in RaftDB's Dockerfile can try whatever it wants, but it won't reach ECR, because there's no identity in that job's environment capable of touching ECR.

Therefore, the tested image must be moved. The job saves it and hands it off as an artifact, accompanied by a small evidence document:

```bash
docker save --output raftdb-image.tar "$LOCAL_IMAGE"
gzip -9 raftdb-image.tar
jq -n \
  --arg commit "$CI_COMMIT_SHA" \
  --arg imageId "$IMAGE_ID_AFTER_SCAN" \
  --arg tag "$LOCAL_IMAGE" \
  --argjson criticalCount "$CRITICAL_COUNT" \
  --argjson highCount "$HIGH_COUNT" \
  --argjson highAccepted "$HIGH_ACCEPTED" \
  '{commit: $commit, imageId: $imageId, localTag: $tag, scan: {criticalCount: $criticalCount, highCount: $highCount, highAccepted: $highAccepted}}' \
  > raftdb-image-evidence.json
```

`publish-raftdb-image` receives that part via `needs: [{job: raftdb-image, artifacts: true}]`. Before requesting a token, it establishes the artifact's identity twice over. It reads `.commit` from `raftdb-image-evidence.json` and fails if it isn't `$CI_COMMIT_SHA`, thereby dropping a stale artifact from a previous pipeline. Then it runs `gzip -dc raftdb-image.tar.gz | docker load` and compares the `{{.Id}}` of the loaded image against `.imageId` in the evidence file, failing on the slightest mismatch. Only when both checks pass does `aws sts assume-role-with-web-identity` appear, using a session name with a `-RaftDB` suffix. The credentials arrive at step four, not step one.

What it does with those credentials is also deliberately constrained. `scripts/ensure-ecr-repository.sh` resolves the repository URI, then the job asserts the repository part is exactly `awsplace-ecs`, refusing to proceed with anything else. It pushes the tag `raftdb-${CI_COMMIT_SHA}`. That tag is immutable on ECR by configuration: the repository runs with `--image-tag-mutability MUTABLE_WITH_EXCLUSION` and an exclusion filter `filterType=WILDCARD,filter=raftdb-*`, so normal tags can still move but `raftdb-*` tags cannot. If the tag already exists, the job pulls it and compares its image ID to the image it just verified, failing if the tag points to different bytes instead of overwriting anything.

Then it does my favorite thing in the entire pipeline. It reads the returned digest, validates it against `^sha256:[0-9a-f]{64}$`, wipes all local copies of the image using `docker image rm --force`, pulls the image back *by digest*, and runs the container test and migration test again on the exact bytes returned by ECR:

```bash
docker image rm --force \
  "$LOCAL_IMAGE" \
  "${ECR_URI}:${IMAGE_TAG}" \
  "${ECR_URI}@${IMAGE_DIGEST}" 2>/dev/null || true
docker pull "${ECR_URI}@${IMAGE_DIGEST}"
bash raftdb/test/container_contract_test.sh "${ECR_URI}@${IMAGE_DIGEST}"
bash raftdb/test/migration_runtime_contract_test.sh "${ECR_URI}@${IMAGE_DIGEST}"
```

Removing the local images first is what gives meaning to the re-pull. Without that, Docker would just use the layers it already has, and the test wouldn't prove anything about what's actually sitting in the registry.

The digest is then forwarded as a dotenv report:

```yaml
artifacts:
  expire_in: 90 days
  paths:
    - raftdb-publish-evidence.json
    - raftdb-publish.env
  reports:
    dotenv: raftdb-publish.env
```

`deploy-to-aws` receives `PUBLISHED_RAFTDB_IMAGE_DIGEST` from that dotenv report, and it doesn't trust it outright. Its `before_script` reads `.digest` from `raftdb-publish-evidence.json` and fails if the dotenv value and the evidence file disagree. It then exports the matched value as `RAFTDB_IMAGE_DIGEST` and runs `scripts/validate-deploy-env.sh`. That script demands the presence of nine variables, strips any values that still contain an unresolved `${VAR}` reference, validates `RAFTDB_IMAGE_DIGEST` against the same sha256 pattern, and checks `HOSTED_ZONE_ID` against `^Z[A-Z0-9]+$`. This entire block runs *before* the STS command. A missing secret or a malformed digest fails the job while it still has no AWS credentials and hasn't created any AWS resources.

The result is that the digest CDK pins into the ECS task definition is proven to be the digest of an image built without AWS permissions, scanned, tested in four different ways, verified byte-for-byte upon handover, and re-tested once again after taking a round trip through the registry.

<figure>
  <img src="/images/3-BlogPosted/cicd-pipeline.svg" alt="Four stages of the awsplace GitLab pipeline with the RaftDB image chain of custody highlighted" loading="lazy">
  <figcaption>Four stages: <code>build-ci-image</code>, <code>test</code>, <code>build</code>, <code>deploy</code>. The custody lane runs from the credential-less <code>raftdb-image</code> job to the digest verification step in <code>deploy-to-aws</code>.</figcaption>
</figure>

## References

- [GitLab: ID token authentication](https://docs.gitlab.com/ci/secrets/id_token_authentication/)
- [GitLab: `id_tokens` keyword reference](https://docs.gitlab.com/ci/yaml/#id_tokens)
- [GitLab: Configure OpenID Connect with AWS to retrieve temporary credentials](https://docs.gitlab.com/ci/cloud_services/aws/)
- [AWS STS API: `AssumeRoleWithWebIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)
- [AWS IAM: Create OpenID Connect identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
- [Amazon ECR: Private registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html)
- [Amazon ECR: Image tag mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html)


---
**Original post on AWS Study Group:** [View here](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2227894604642166/#)
