---
title: "Week 1 Worklog"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Objectives:

* Connect and get acquainted with members of First Cloud AI Journey (FCAJ).
* Understand fundamental AWS services and navigate the AWS Management Console & CLI.

### Tasks:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 1 | - Get acquainted with FCAJ members<br>- Read and take notes on internship unit rules and regulations | 06/15/2026 | 06/15/2026 | FCAJ Onboarding Docs |
| 2 | - Learn about AWS and its service categories:<br>&emsp;+ Compute<br>&emsp;+ Storage<br>&emsp;+ Networking<br>&emsp;+ Database | 06/16/2026 | 06/16/2026 | cloudjourney.awsstudygroup.com |
| 3 | - Create AWS Free Tier account<br>- Learn about AWS Console & AWS CLI<br>- Practice:<br>&emsp;+ Create AWS account<br>&emsp;+ Install & configure AWS CLI | 06/17/2026 | 06/17/2026 | cloudjourney.awsstudygroup.com |
| 4 | - Learn basic EC2:<br>&emsp;+ Instance types, AMI, EBS<br>- SSH connection methods to EC2<br>- Learn about Elastic IP | 06/18/2026 | 06/18/2026 | cloudjourney.awsstudygroup.com |
| 5 | - Practice:<br>&emsp;+ Launch an EC2 instance<br>&emsp;+ Connect via SSH<br>&emsp;+ Attach an EBS volume | 06/19/2026 | 06/19/2026 | cloudjourney.awsstudygroup.com |
| 6 | - Read and discuss Raft algorithm whitepaper.<br>- Analyze awsplace project specifications.<br>- Initialize repository: CMakeLists.txt, presets, GoogleTest. | 06/15/2026 | 06/15/2026 | RaftDB C++ Report |
| 7 | - Setup CI/CD (GitHub Actions).<br>- Design Network Server architecture (epoll/kqueue).<br>- Draft PROTOCOL.md.<br>- Define Error Codes and Leader Redirect mechanism. | 06/15/2026 | 06/15/2026 | RaftDB C++ Report |

### Achievements:

* Successfully navigated the AWS onboarding process and gained a robust understanding of fundamental cloud computing concepts, specifically Compute, Storage, Networking, and Database services.
* Established a fully functional AWS development environment, including a well-configured Free Tier account, AWS Management Console access, and a secured AWS CLI setup.
* Demonstrated hands-on proficiency by launching and connecting to an Amazon EC2 instance via SSH, as well as successfully attaching and managing EBS volumes.
* Laid the foundational architecture for the RaftDB C++ project by establishing a robust build system utilizing CMake and Ninja, complete with various compilation presets (ASan, UBSan, Release, Fuzz).
* Engineered the initial network server architecture leveraging highly efficient asynchronous non-blocking I/O models (epoll/kqueue) to ensure optimal performance.
* Drafted comprehensive technical specifications, including the Protocol specification document for binary communication and predefined Error Codes for Leader Redirect mechanisms.
* Automated the development workflow by integrating GitHub Actions for continuous integration, ensuring all unit tests and builds are validated upon every commit.
