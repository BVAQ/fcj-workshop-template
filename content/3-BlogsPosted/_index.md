---
title: "Blogs Posted"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

Below is the list of technical blogs sharing the journey of deploying the internship project on AWS infrastructure:

###  [Blog 1 - Building an Auto-Scaling GitLab Runner on AWS EC2](3.1-Blog1/)
This blog shares the process of designing and deploying an auto-scaling GitLab Runner on AWS EC2. Instead of relying on a low-end personal machine, the system uses the Docker Autoscaler and scales to zero when there are no jobs, effectively saving costs while resolving the CI/CD pipeline bottleneck.

###  [Blog 2 - Configuring OpenID Connect (OIDC) between GitLab CI and AWS](3.2-Blog2/)
This blog delves into eliminating static AWS Access Keys in the CI/CD pipeline by setting up OpenID Connect (OIDC). Instead of storing long-lived secrets, GitLab CI uses short-lived JWTs to authenticate with an AWS IAM role, combined with strict validation steps to ensure a secure chain of custody from source code to deployment.

###  [Blog 3 - Using Amazon EFS for a RaftDB Container on ECS Fargate](3.3-Blog3/)
This blog solves the persistent storage challenge for a C++ RaftDB sidecar container running on Amazon ECS Fargate. By leveraging Amazon EFS and EFS Access Points, the system overcomes Fargate's ephemeral storage limits, preserving the entire write-ahead log and application state across deployments.