---
title: "Blog 1 - Building an Auto-Scaling GitLab Runner on AWS EC2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# AUTO-SCALING GITLAB CI/CD RUNNERS ON AWS EC2 WITH DOCKER AUTOSCALER AND TERRAFORM

This technical blog post walks through designing and deploying a self-hosted GitLab Runner that automatically provisions ephemeral EC2 workers via AWS Auto Scaling Groups, scaling to zero when idle and spinning up fresh instances on demand.

### Key Technical Highlights Covered in the Blog:

- **Docker Autoscaler Executor**: Explains the GitLab Runner Docker Autoscaler executor model where a lightweight Runner Manager continuously polls for jobs and delegates actual build work to short-lived EC2 instances managed by the Fleeting AWS plugin.

- **Scale-to-Zero Architecture**: Details the Auto Scaling Group configuration with **desired_capacity = 0** and **idle_count = 0**, ensuring no EC2 instances exist when no pipeline is running, reducing costs to near zero during idle periods.

- **Single-Use Ephemeral Workers**: Describes the **capacity_per_instance = 1** and **max_use_count = 1** configuration that guarantees each EC2 instance handles exactly one job before being terminated, providing a clean and predictable build environment for every pipeline run.

- **Terraform and Fleeting Plugin Coordination**: Addresses the dual-controller problem where Terraform creates the ASG but the Fleeting plugin manages **desired_capacity** at runtime, using **ignore_changes** in the lifecycle block to prevent configuration drift.

- **Pre-baked VM Images with Packer**: Describes using HashiCorp Packer to build custom Amazon Machine Images (AMIs) with Docker and the CI image pre-pulled, eliminating cold-start overhead when new workers boot.

- **Prebuilt CI Docker Image via GitHub Actions**: Explains the workflow that automatically builds and publishes the CI environment image to GitHub Container Registry (GHCR), ensuring all workers share an identical, versioned build environment.

---

### Facebook Community Post

![Facebook Community Post](/images/3-BlogPosted/fb-post-blog1.png)

- **Official Publication Link**: [AWS Study Group Facebook Post](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2225051181593175/)
- **Target Audience**: DevOps Engineers, Cloud Infrastructure Engineers, CI/CD Practitioners
- **Community Engagement**: Published on the AWS Study Group community platform for peer review and architectural feedback.
