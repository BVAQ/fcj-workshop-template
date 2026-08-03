---
title: "Blog 2 - Configuring OpenID Connect (OIDC) between GitLab CI and AWS"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# ZERO STATIC KEYS: SECURING A GITLAB CI/CD PIPELINE WITH OPENID CONNECT AND AWS IAM

This technical blog post explains how to eliminate long-lived AWS Access Keys from a self-hosted GitLab CI/CD pipeline by implementing OpenID Connect (OIDC) federation, allowing jobs to assume an IAM role with short-lived credentials scoped to a specific project and branch.

### Key Technical Highlights Covered in the Blog:

- **OIDC Federation Architecture**: Explains how GitLab acts as an OpenID Connect identity provider, issuing short-lived JWTs for each job that declares **id_tokens**, while AWS IAM validates the token signature via a registered OIDC provider and JWKS endpoint.

- **Trust Policy with Subject Pinning**: Details the IAM trust policy that performs exact-match on the **aud** claim and pattern-match on the **sub** claim (**project_path:…:ref_type:branch:ref:main**), ensuring only the correct project and branch can assume the deployment role.

- **Minimal Credential Exposure**: Describes how only 3 out of 14 pipeline jobs (**push-ecr**, **publish-raftdb-image**, **deploy-to-aws**) declare **id_tokens** and obtain AWS credentials, while the remaining 11 jobs, including the RaftDB image build, run without any AWS identity.

- **Chain of Custody for Container Images**: Walks through the multi-step verification pipeline where the RaftDB image is built without AWS credentials, scanned with Trivy, artifact-transferred with evidence files, re-verified byte-for-byte after ECR upload, and re-tested from the registry before deployment.

- **STS Session Traceability**: Shows how **--role-session-name "GitLabCI-${CI_PIPELINE_ID}"** embeds the pipeline identifier into every CloudTrail entry, enabling full audit traceability from AWS API calls back to specific CI/CD pipeline runs.

- **Immutable Image Tags on ECR**: Explains the ECR tag mutability configuration using **MUTABLE_WITH_EXCLUSION** with a wildcard filter on **raftdb-***, preventing overwrite of published production images while allowing other tags to move freely.

---

### Facebook Community Post

![Facebook Community Post](/images/3-BlogPosted/fb-post-blog2.png)

- **Official Publication Link**: [AWS Study Group Facebook Post](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2227894604642166/)
- **Target Audience**: DevOps Engineers, Security Engineers, Cloud Architects
- **Community Engagement**: Published on the AWS Study Group community platform for peer review and architectural feedback.
