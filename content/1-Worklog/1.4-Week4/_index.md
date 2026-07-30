---
title: "Week 4 Worklog"
date: 2026-07-06
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Objectives:

* Understand the serverless computing model using AWS Lambda and API Gateway.
* Select and plan the architecture for the final internship project.

### Tasks:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 16 | - Learn AWS Lambda and API Gateway basics. | 07/06/2026 | 07/06/2026 | cloudjourney.awsstudygroup.com |
| 17 | - Practice: Build a simple serverless REST API using Lambda and API Gateway. | 07/07/2026 | 07/07/2026 | FCAJ Serverless Guide |
| 18 | - Project Kickoff: Brainstorming and selecting the project topic. | 07/08/2026 | 07/08/2026 | Project Guidelines |
| 19 | - Architecture Design: Drafting architecture diagrams for the chosen project. | 07/09/2026 | 07/09/2026 | AWS Architecture Center |
| 20 | - Present project plan and architecture to mentors for approval. | 07/10/2026 | 07/10/2026 | Mentor Feedback Notes |
| 6 | - Upgrade AppendEntries RPC: Send Log Entries.<br>- Optimize Batch sending to increase throughput. | TBD | TBD | RaftDB C++ Report |
| 7 | - Implement Conflict Resolution logic.<br>- Implement Commit Index calculation mechanism. | TBD | TBD | RaftDB C++ Report |

### Achievements:

* Transitioned from manual AWS Management Console operations to Infrastructure as Code (IaC) by mastering the AWS Cloud Development Kit (CDK).
* Successfully initialized a complete AWS CDK project, deploying scalable infrastructure via automated CloudFormation stacks.
* Refactored earlier manual setups (VPC, EC2, S3) into modular, reusable CDK constructs, significantly improving deployment consistency and speed.
* Upgraded the Raft cluster's AppendEntries RPC, successfully enabling the transmission of actual Log Entries from the Leader to Follower nodes.
* Optimized network throughput by engineering a Batch sending mechanism, drastically reducing the RPC overhead for high-volume data streams.
* Successfully implemented Raft's Conflict Resolution logic, enabling the Leader to automatically detect inconsistencies and overwrite malformed Follower logs seamlessly.
* Developed a precise Commit Index calculation mechanism, ensuring the State Machine only executes commands that have safely achieved majority consensus.
