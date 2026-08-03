---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Introduction

During my internship project at FCAJ, I hosted all the source code on my personal GitLab and set up a GitLab Runner on my home machine to run CI/CD.

The problem was that the machine's configuration was not powerful enough to run multiple pipelines concurrently, so I only configured 1 concurrent job. This meant that whenever multiple pipelines were triggered, the jobs had to queue up for a very long time. There were times when an entire pipeline took more than an hour to complete, and jobs running AddressSanitizer (ASan) or ThreadSanitizer (TSan) alone had to wait over 30 minutes just to acquire a worker.

<figure>
  <img src="/images/3-BlogPosted/longqueue.png" alt="GitLab jobs list with wait times from 11 to 33 minutes" loading="lazy">
  <figcaption>Jobs aren't running slowly. They just take too long to acquire a worker.</figcaption>
</figure>

At that point, I suddenly thought: instead of upgrading the hardware, why not leverage **AWS EC2 Auto Scaling Group**? AWS still offers $200 in student credits, so this was also a great opportunity to try deploying a GitLab Runner capable of automatically scaling based on the number of jobs that need to be run. It perfectly solved the problem I was facing while giving me a chance to practice with AWS infrastructure on a real-world problem.

# Design Goals

My goal was not to build a complete CI/CD system or replace GitLab SaaS. What I wanted was simply:

- No cost for workers when no pipeline is running (scale-to-zero).
- Accept a few dozen seconds of cold start in exchange for near-zero cost.
- When there's a pipeline, workers must be created automatically without manual intervention.
- Each job runs in a completely fresh environment to avoid interfering with one another.
- After completion, the worker self-destructs to avoid wasting resources.

In short, I wanted to turn GitLab Runner into an "exists only when needed" service.

# Architecture Design Idea

The entire system is divided into two parts.

The first part is the **Runner Manager**, running continuously on a small machine. Its only task is to connect to GitLab, monitor the pipeline queue, and decide when more workers are needed.

The second part consists of the **EC2 Workers** located in an **Auto Scaling Group** with **desired capacity = 0**. Normally, no EC2 instances exist. Only when a new job appears on GitLab does the Runner Manager request the Auto Scaling Group to spin up an additional instance. After booting, the worker takes exactly one job, runs it inside a Docker container, and then terminates itself.

What I like about this model is that the Runner Manager is always very lightweight, while all the resources needed for building appear only when truly necessary.

<figure>
  <img src="/images/3-BlogPosted/gitlab-runner-ec2-autoscale-vi.svg" alt="Diagram of GitLab Runner Manager controlling EC2 Auto Scaling Group and temporary workers" loading="lazy">
  <figcaption>Two main flows of the system: preparing the worker image and executing a CI job on a temporary EC2 instance.</figcaption>
</figure>

The execution flow of a job can be summarized as follows:

1. Runner Manager receives the job from GitLab via HTTPS.
2. The Fleeting AWS plugin requests the Auto Scaling Group to increase capacity from **0** to **1**.
3. The EC2 instance boots from a custom AMI, Runner Manager connects via SSH, and starts the Docker container.
4. Logs and results are returned to GitLab.
5. The worker is discarded after the job, and the capacity returns to **0**.

## One Job Per Machine

The most critical part of the Runner configuration is actually quite short:

```toml
[[runners]]
  executor = "docker-autoscaler"

  [runners.autoscaler]
    plugin               = "aws:latest"
    capacity_per_instance = 1
    max_use_count         = 1
    max_instances         = 10

    [[runners.autoscaler.policy]]
      idle_count = 0
      idle_time  = "5m"
```

**capacity_per_instance = 1** limits each EC2 instance to running one job at a time, while **max_use_count = 1** ensures the instance is scheduled for removal immediately after its first use. I accept losing local cache and the ability to reuse workers in exchange for a cleaner, more predictable environment for each pipeline. In a production environment, **aws:latest** should also be pinned to a specific plugin version.

## Only One Capacity Controller Should Exist

Terraform initially creates the Auto Scaling Group, but GitLab Runner is the component that scales the **desired_capacity** up or down during operation. If Terraform continues to try managing this value on every **apply**, the two controllers might pull the capacity in different directions.

```hcl
resource "aws_autoscaling_group" "runner" {
  name                = "${var.name_prefix}-asg"
  min_size            = 0
  max_size            = var.max_instances
  desired_capacity    = 0
  vpc_zone_identifier = local.subnet_ids

  launch_template {
    id      = aws_launch_template.runner.id
    version = "$Latest"
  }

  lifecycle {
    # The Fleeting plugin is the controller of capacity after the ASG is created.
    ignore_changes = [desired_capacity]
  }
}
```

**ignore_changes** does not mean Terraform abandons management of the ASG. Terraform still manages the Launch Template, subnets, tags, and other infrastructure attributes; it just doesn't overwrite the number of instances the Runner is requesting.

# Prebuilt Docker Image with GitHub Actions

One problem I encountered quite early on was the build environment.

If every newly started worker has to install compilers, SDKs, and dependencies before running a pipeline, most of the time will be wasted preparing the environment rather than running the job.

To solve this, I isolated the entire build environment into a separate Docker image. This image is automatically built by GitHub Actions and published to the GitHub Container Registry (GHCR) whenever there are changes.

As a result, all workers share the exact same build environment. When a new package or tool is needed, I simply update the Dockerfile and let GitHub Actions rebuild the image.

This also makes managing the CI environment much simpler because all dependencies reside in a single place.

Here is a simplified version of the image build and publish workflow:

```yaml
name: Build CI image

on:
  push:
    paths:
      - "ci-image/**"

permissions:
  contents: read
  packages: write

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: docker/login-action@v4
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v7
        with:
          context: ./ci-image
          push: true
          tags: |
            ghcr.io/${{ github.repository }}-ci:latest
            ghcr.io/${{ github.repository }}-ci:sha-${{ github.sha }}
```

<figure>
  <img src="/images/3-BlogPosted/ghcr.png" alt="Docker image of the GitLab Runner worker published on GitHub Container Registry" loading="lazy">
  <figcaption>The CI image on GHCR has both the <code>latest</code> tag and a tag associated with the commit for easy tracking.</figcaption>
</figure>

In the demo version, I still use **latest** for quick updates. If higher reproducibility is needed, the worker should pull the image by digest or an immutable tag instead of a tag that might point to new content.

# Pre-baking the VM Image

Just having a Docker image is not enough.

If every time an EC2 instance boots up it has to install Docker and pull the image from GHCR, the cold start will still be quite long. With a system designed to scale from 0, these few dozen seconds would occur on every initial pipeline.

Therefore, I used Packer to create a **custom Amazon Machine Image (AMI)**.

This AMI already contains:

- Docker
- Necessary tools
- The Docker image for CI

Packer uses the **amazon-ebs** builder, runs the provisioning script, and packages the final state into an AMI:

```hcl
build {
  name    = "gitlab-runner-worker"
  sources = ["source.amazon-ebs.runner"]

  provisioner "shell" {
    environment_vars = [
      "CI_IMAGE=${var.ci_image}",
      "SSH_USER=${var.ssh_username}",
    ]
    script = "${path.root}/scripts/install.sh"
  }
}
```

The provisioning script installs Docker and runs **docker pull "${CI_IMAGE}"** right during the AMI build process. Because the layers are already present on disk, a new worker only needs to check or download changed layers when booting.

<figure>
  <img src="/images/3-BlogPosted/config.png" alt="Packer variables file containing region, instance type, and CI image address on GHCR" loading="lazy">
  <figcaption>Input values used to build the worker AMI with Packer.</figcaption>
</figure>

<figure>
  <img src="/images/3-BlogPosted/build_image.png" alt="Packer log pulling the Docker image and completing the Amazon Machine Image creation" loading="lazy">
  <figcaption>The experimental build completed after 6 minutes and 44 seconds; the preparation cost is paid once instead of repeating on every job.</figcaption>
</figure>

When the Auto Scaling Group creates a new worker, the machine is almost ready to run jobs immediately without having to reinstall from scratch.

Building the AMI takes a few extra minutes, but this is a one-time cost. In return, all subsequently created workers boot significantly faster.

# Observing the Worker Lifecycle

To verify autoscaling, I monitored both the Runner logs and the Auto Scaling Group status simultaneously:

```bash
watch -n 5 'aws autoscaling describe-auto-scaling-groups \
  --auto-scaling-group-names <asg_name> \
  --query "AutoScalingGroups[0].{desired:DesiredCapacity,instances:Instances[].LifecycleState}"'
```

If the system operates correctly, **desired** will follow the sequence **0 → 1 → 0**. During a burst of multiple jobs, EC2 instances in **Initializing**, **Running**, **Shutting-down**, and **Terminated** states might appear simultaneously because each worker has its own lifecycle.

<figure>
  <img src="/images/3-BlogPosted/ec2.png" alt="Temporary EC2 workers in running, shutting-down, and terminated states" loading="lazy">
  <figcaption>New workers and workers being reclaimed can overlap during a pipeline burst.</figcaption>
</figure>

<figure>
  <img src="/images/3-BlogPosted/runner.png" alt="GitLab Runner using Docker Autoscaler is online and processing jobs" loading="lazy">
  <figcaption>Runner result on the GitLab management page.</figcaption>
</figure>

# Conclusion

Upon completion, my GitLab Runner could automatically scale according to the number of pending pipelines.

When there are no jobs, all EC2 workers are shut down, and the cost is nearly zero. When a new pipeline appears, the Auto Scaling Group automatically creates a worker, runs exactly one job, and reclaims the instance upon completion.

This is not yet a production-ready system. I still have many things I want to improve, such as using private subnets, substituting IAM Roles for access keys, pinning images by digest, or adding monitoring for the entire worker initialization process.

Nevertheless, this project helped me better understand how the GitLab Runner Autoscaler works, and how to combine Terraform, Packer, and AWS Auto Scaling Groups to build an automatically scaling CI/CD system without having to maintain a continuously running cluster of machines.

## References

- [GitLab Docker Autoscaler executor](https://docs.gitlab.com/runner/executors/docker_autoscaler/)
- [GitLab Runner advanced configuration](https://docs.gitlab.com/runner/configuration/advanced-configuration/#the-runnersautoscaler-section)
- [HashiCorp: Manage AWS Auto Scaling Groups with Terraform](https://developer.hashicorp.com/terraform/tutorials/aws/aws-asg)
- [HashiCorp Packer: Amazon EBS builder](https://developer.hashicorp.com/packer/integrations/hashicorp/amazon/latest/components/builder/ebs)


---
**Original post on AWS Study Group:** [View here](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2225051181593175/#)
