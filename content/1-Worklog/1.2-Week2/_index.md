---
title: "Week 2 Worklog"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Objectives:

* Deepen knowledge of EC2 scaling and load distribution.
* Master AWS storage solutions, specifically Amazon S3 and EFS.

### Tasks:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 6 | - Study Elastic Load Balancing (ELB) types (ALB, NLB).<br>- Understand Auto Scaling Groups (ASG). | 06/22/2026 | 06/22/2026 | cloudjourney.awsstudygroup.com |
| 7 | - Practice: Configure an Application Load Balancer targeting multiple EC2 instances. | 06/23/2026 | 06/23/2026 | FCAJ Compute Modules |
| 8 | - Learn Amazon S3 basics (Buckets, Objects, Storage Classes, Versioning). | 06/24/2026 | 06/24/2026 | AWS S3 Documentation |
| 9 | - Practice: Create an S3 bucket, upload files, configure static website hosting. | 06/25/2026 | 06/25/2026 | cloudjourney.awsstudygroup.com |
| 10 | - Explore Amazon EFS and compare with EBS and S3.<br>- Practice: Mount EFS to multiple EC2 instances. | 06/26/2026 | 06/26/2026 | FCAJ Storage Modules |
| 6 | - Implement TCP server module (Client Sessions, EPOLLIN/EPOLLOUT).<br>- Write Frame Parser module, handle TCP fragmentation/coalescing. | TBD | TBD | RaftDB C++ Report |
| 7 | - Implement Reliable UDP layer.<br>- Write Unit tests: Fuzzing TCP Parser to reject malformed packets. | TBD | TBD | RaftDB C++ Report |

### Achievements:

* Successfully architected and deployed an auto-scaling environment utilizing an Application Load Balancer (ALB) to efficiently distribute traffic across multiple EC2 instances.
* Mastered Amazon S3 capabilities by successfully creating buckets, managing objects, and configuring a fully functional static website hosting environment.
* Developed a comprehensive understanding of AWS storage options, clearly distinguishing the architectural differences, performance characteristics, and optimal use cases for EBS, EFS, and S3.
* Implemented the core networking layer for RaftDB, successfully managing complex client sessions and handling low-level EPOLLIN/EPOLLOUT events.
* Developed a robust Frame Parser module capable of accurately processing TCP fragmentation and coalescing, ensuring reliable data extraction without buffer overflow risks.
* Expanded network capabilities by implementing a Reliable UDP (RUDP) layer to facilitate high-speed intra-cluster communication.
* Fortified the network parser's resilience by writing rigorous unit tests, specifically utilizing fuzzing techniques to automatically reject malformed TCP packets.
