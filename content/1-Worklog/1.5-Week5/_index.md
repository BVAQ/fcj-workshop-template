---
title: "Week 5 Worklog"
date: 2026-07-13
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Objectives:

* Set up the foundational infrastructure for the final project.
* Implement the backend components and database schemas.

### Tasks:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 21 | - Provision VPC, Subnets, and Security Groups for the project. | 07/13/2026 | 07/13/2026 | Approved Architecture Diagram |
| 22 | - Set up the database (RDS/DynamoDB) and configure initial tables/schemas. | 07/14/2026 | 07/14/2026 | Project Requirements |
| 23 | - Develop core backend scripts/Lambda functions. | 07/15/2026 | 07/15/2026 | AWS SDK Documentation |
| 24 | - Integrate backend with the database and test CRUD operations. | 07/16/2026 | 07/16/2026 | Project Requirements |
| 25 | - Set up IAM roles and strict permission policies for backend services. | 07/17/2026 | 07/17/2026 | AWS IAM Docs |
| 6 | - Connect State Machine to Network layer: Respond to client after Committed.<br>- Handle NOT_LEADER error for client reconnection. | TBD | TBD | RaftDB C++ Report |
| 7 | - Implement basic commands in the command engine: GET, SET, EXISTS, DEL.<br>- Ensure Atomicity for overwrite operations. | TBD | TBD | RaftDB C++ Report |

### Achievements:

* Integrated serverless computing paradigms into the project by developing and deploying AWS Lambda functions for backend processing.
* Orchestrated event-driven architectures utilizing Amazon EventBridge and SNS to trigger serverless workflows asynchronously.
* Successfully established the critical bridge between RaftDB's State Machine and its Network layer, guaranteeing clients only receive "OK" responses post-consensus.
* Implemented the NOT_LEADER redirect mechanism, empowering clients to automatically discover and reconnect to the active cluster Leader without manual intervention.
* Built the core storage engine commands, fully supporting standard KV operations such as GET, SET, EXISTS, and DEL in-memory.
* Engineered strict atomicity guarantees for data overwrite operations, ensuring the database remains completely resilient against race conditions during concurrent accesses.
* Synthesized AWS serverless components with custom backend services, bridging the gap between managed cloud services and raw C++ performance.
