---
title: "Week 3 Worklog"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Objectives:

* Understand fundamental AWS networking concepts (VPC).
* Learn relational and non-relational database offerings on AWS.

### Tasks:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 11 | - Learn Amazon VPC basics: Subnets, Route Tables, Internet Gateways. | 06/29/2026 | 06/29/2026 | cloudjourney.awsstudygroup.com |
| 12 | - Practice: Build a custom VPC with public and private subnets, NAT Gateway. | 06/30/2026 | 06/30/2026 | FCAJ Networking Modules |
| 13 | - Learn Amazon RDS (Relational Database Service) concepts and engines. | 07/01/2026 | 07/01/2026 | AWS RDS Docs |
| 14 | - Practice: Provision an RDS MySQL instance and connect via EC2 in a private subnet. | 07/02/2026 | 07/02/2026 | FCAJ Database Modules |
| 15 | - Learn Amazon DynamoDB basics (NoSQL, Tables, Items, Partition Keys). | 07/03/2026 | 07/03/2026 | cloudjourney.awsstudygroup.com |
| 6 | - Build Raft Core State Machine .<br>- Implement Randomized Election Timeout. | TBD | TBD | RaftDB C++ Report |
| 7 | - Implement RequestVote RPC logic: Handle vote rejection/approval, handle Split-brain. | TBD | TBD | RaftDB C++ Report |

### Achievements:

* Mastered AWS networking fundamentals by designing and provisioning a custom Virtual Private Cloud (VPC), complete with customized public and private subnets.
* Configured robust routing mechanisms and security measures, successfully implementing Route Tables, Internet Gateways, and strict Security Groups to control inbound/outbound traffic.
* Explored managed database services by deploying Amazon RDS, understanding the operational benefits over self-hosted databases.
* Successfully architected the Core State Machine for the Raft consensus algorithm, properly defining and transitioning between Follower, Candidate, and Leader states.
* Implemented a critical Randomized Election Timeout mechanism, effectively mitigating the risk of split votes and election collisions in the Raft cluster.
* Developed the complex RequestVote RPC logic, enabling nodes to intelligently evaluate terms and log indices to approve or reject leader elections.
* Established robust handling for network partitions (Split-brain scenarios), ensuring the distributed system maintains data consistency under adverse network conditions.
