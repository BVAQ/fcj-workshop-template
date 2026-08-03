---
title: "Blog 3 - Using Amazon EFS for a RaftDB Container on ECS Fargate"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# PERSISTENT STORAGE FOR A STATEFUL CONTAINER ON ECS FARGATE USING AMAZON EFS

This technical blog post addresses the persistent storage challenge for a C++23 RaftDB sidecar container running on Amazon ECS Fargate, explaining how Amazon EFS and EFS Access Points preserve the write-ahead log and application state across task replacements.

### Key Technical Highlights Covered in the Blog:

- **The Ephemeral Storage Problem**: Explains why Fargate's task-scoped storage causes data loss on every deployment, since each **cdk deploy** or **force-new-deployment** replaces the task with a completely new one, discarding the WAL and snapshots written by RaftDB.

- **Storage Option Analysis**: Evaluates EBS (single-attach limitation incompatible with task replacement), S3 (object storage incompatible with in-place WAL appends), and ephemeral volumes (destroyed with the task) before selecting EFS as the only POSIX-compliant, multi-attach, task-outliving storage option.

- **EFS Access Point Identity Management**: Details how EFS Access Points enforce UID/GID ownership (**10001:10001**) and directory permissions (**0750**) at the filesystem level, eliminating the need for root privileges or **chown** entrypoint scripts in the container.

- **IAM-Scoped Mount Authorization**: Shows how the IAM policy restricts **ClientMount** and **ClientWrite** actions to a specific Access Point ARN, preventing the task role from touching any other directory on the same file system.

- **Stop-Then-Start Deployment Strategy**: Describes the **minHealthyPercent: 0** and **maxHealthyPercent: 100** configuration that forces ECS to terminate the running task before starting a replacement, preventing concurrent WAL writers that would cause data corruption.

- **Graceful Shutdown and Recovery Cycle**: Explains the full lifecycle from **SIGTERM** handling with a 120-second **stopTimeout** for checkpoint publication, through startup validation with snapshot verification and WAL tail replay, ensuring data integrity across every deployment.

---

### Facebook Community Post

![Facebook Community Post](/images/3-BlogPosted/fb-post-blog3.png)

- **Official Publication Link**: [AWS Study Group Facebook Post](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2228318824599744/)
- **Target Audience**: Cloud Engineers, Backend Developers, Systems Architects
- **Community Engagement**: Published on the AWS Study Group community platform for peer review and architectural feedback.
