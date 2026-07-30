---
title: "Blog 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

## Context

The production datastore of my internship project is not a managed service. It is a C++23 server named RaftDB, running as a sidecar container within the same ECS Fargate task as the Go application. The application talks to it via `127.0.0.1:9100` with `DATA_MODE=raftdb-only`, meaning every pixel on the collaborative canvas, along with configs, bans, milestones, and pixel placement history, resides within that exact single process (`awsplace/cdk/lib/ecs.ts:130-140`).

RaftDB persists its state on disk. Its runtime contract explicitly defines the layout: the writable data directory is `/data/raftdb`, the write-ahead log is at `/data/raftdb/wal`, the local checkpoints are at `/data/raftdb/snapshots`, and the process only publishes the temporary readiness marker at `/tmp/raftdb-ready` after the recovery process is complete (`awsplace/docs/raftdb/runtime-contract.md:34-41`).

Fargate does not preserve containers. Every `cdk deploy`, every new image digest, every `force-new-deployment` replaces the task with a completely new one. So I have a process whose entire value is the bytes it has written to disk, running on a platform that throws that disk away.

## What an Empty WAL Cost Me

Locally, this was never an issue, because Docker Compose gave me a persistent disk. The `raftdb` service mounts a named volume, and a named volume survives `docker compose down`:

```yaml
services:
  raftdb:
    build:
      context: .
      dockerfile: raftdb/Dockerfile
    container_name: awsplace-raftdb
    environment:
      RAFTDB_PORT: "9100"
      RAFTDB_DATA_DIR: /data/raftdb
    volumes:
      - raftdb_data:/data/raftdb
    ports:
      - "9100:9100"

volumes:
  pg_data:
  raftdb_data:
```

The snippet above is abbreviated from `awsplace/docker-compose.yml:7-19` and `:138-140`. Rebuild the image, restart the container, and the WAL segments and snapshot catalog under `/data/raftdb` are still there. My local canvas retained its pixels across a rebuild without me doing anything.

On Fargate, before I attached persistent storage, the exact opposite happened. The replacement task started with an empty `/data/raftdb`. There was no tail of a WAL to replay and no snapshot to restore, so every deployment gave me a blank slate. Testing anything that depended on pre-existing state meant manually re-seeding the canvas first, and I was deploying several times an hour. The most interesting part of the job—watching the server recover—was exactly the part I couldn't observe, because there was never anything to recover.

## Why EFS and Not the Alternatives

I considered three other options before mounting Amazon EFS, and each option failed for a specific reason.

An **EBS volume** can only be attached to a single compute instance at a time. With a Fargate task replacement, the new task is a different instance with its own lifecycle, and I would have to detach the volume from the dying task and reattach it to the new one at the exact right moment. That handover is not something an ECS deployment provides out of the box, and if done wrong, the replacement task fails to mount anything.

**Amazon S3** is not a filesystem. RaftDB appends to its write-ahead log in-place, and it replays the tail of the WAL at startup (`runtime-contract.md:114-116`). S3 objects are immutable: appending means rewriting the entire object. S3 is still in the design, but as a destination for complete checkpoints, not as the WAL storage device.

A **task-scoped ephemeral volume** is, by definition, destroyed with the task. That is exactly the failure mode I was experiencing.

Amazon EFS was the only option that is both a POSIX filesystem and capable of being mounted by whichever task exists at this very moment, outliving all of them. The CDK portion for it is very short:

```typescript
const fileSystem = new efs.FileSystem(scope, 'RaftDbApplicationFileSystem', {
  vpc: props.vpc,
  vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
  encrypted: true,
  removalPolicy: RemovalPolicy.DESTROY,
});
const accessPoint = fileSystem.addAccessPoint('ApplicationAccessPoint', {
  path: '/raftdb/production/member-1',
  createAcl: { ownerUid: '10001', ownerGid: '10001', permissions: '0750' },
  posixUser: { uid: '10001', gid: '10001' },
});

props.taskRole.addToPrincipalPolicy(new iam.PolicyStatement({
  actions: ['elasticfilesystem:ClientMount', 'elasticfilesystem:ClientWrite'],
  resources: [fileSystem.fileSystemArn],
  conditions: {
    StringEquals: { 'elasticfilesystem:AccessPointArn': accessPoint.accessPointArn },
  },
}));
```

That is `awsplace/cdk/lib/raftdb-application.ts:32-51`. Then the task definition declares the volume with transit encryption and IAM authorization enabled, and mounts it into the exact path RaftDB already expects:

```typescript
taskDefinition.addVolume({
  name: 'raftdb-data',
  efsVolumeConfiguration: {
    fileSystemId: raftDb.fileSystem.fileSystemId,
    transitEncryption: 'ENABLED',
    authorizationConfig: {
      accessPointId: raftDb.accessPoint.accessPointId,
      iam: 'ENABLED',
    },
  },
});

raftDbContainer.addMountPoints({
  sourceVolume: 'raftdb-data',
  containerPath: '/data/raftdb',
  readOnly: false,
});
```

From `awsplace/cdk/lib/ecs.ts:87-125`. Notice what didn't change: the container still writes to `/data/raftdb`, exactly like it did under Docker Compose. The local loop and the deployed loop now share the same durability contract instead of two different designs.

<figure>
  <img src="/images/3-BlogPosted/efs-console.png" alt="Amazon EFS console showing the RaftDB file system with General Purpose performance, Bursting throughput, regional availability, and encryption enabled" loading="lazy">
  <figcaption>The production file system after creation. General Purpose performance mode and Bursting throughput are the defaults generated by the CDK snippet above.</figcaption>
</figure>

# The Access Point Handles Identity

The RaftDB container runs under `user: '10001:10001'` and is forced to start rootless (`ecs.ts:101`, `runtime-contract.md:43-46`). A standard NFS mount would hand it a root-owned directory, and the first WAL write would fail with a permission error. The standard remedy is an entrypoint that runs `chown` before dropping privileges, which requires the container to be root initially.

The access point eliminates that step. `createAcl` forces EFS to create `/raftdb/production/member-1` owned by uid and gid `10001` with mode `0750`, and `posixUser` forces every request going through the access point to be evaluated under that exact uid and gid. The container's numeric identity matches the directory it drops into, so no `chown`, no root, no init script.

The access point is also the authorization boundary. The IAM statement above grants `ClientMount` and `ClientWrite` on the file system only when `elasticfilesystem:AccessPointArn` exactly matches this access point, meaning the task role cannot touch any other directory on the same file system even if one existed. `runtime-contract.md:100-101` states the same rule from the other side: IAM remains the authorization boundary for EFS access points.

This very construct also paves the way for a multi-voter cluster in the future. `awsplace/cdk/lib/raftdb.ts:388-408` creates an access point for each member at `/raftdb/${dataGeneration}/member-${nodeId}`, where `dataGeneration` is provided by the environment, so three voters can share one file system while remaining completely unable to touch each other's WALs. That is the staging goal documented in the `RaftDbStagingStack`, not what runs today. Production is a single voter with `desiredCount: 1` and a fixed path `/raftdb/production/member-1`.

# The Cost: Stop-Then-Start Deployment

This is the part I didn't foresee. Persistent storage alters the deployment strategy, and not in a pleasant way.

RaftDB has exactly one writer, and Raft leader fencing does not yet exist (`runtime-contract.md:78-80`). If ECS performed a normal rolling deployment, the new task would mount `/raftdb/production/member-1` while the old task still had the WAL open. Two processes appending to the same log means data corruption, not a lock contention scenario that can be retried. Thus, the service is configured so overlap is impossible:

```typescript
const service = new ecs.FargateService(scope, 'Service', {
  cluster,
  taskDefinition,
  desiredCount: 1,
  // A single raftdb writer owns the EFS WAL. Stop it before replacement;
  // overlapping tasks would open the same durable files concurrently.
  minHealthyPercent: 0,
  maxHealthyPercent: 100,
  // ...
});
```

`minHealthyPercent: 0` is permission for ECS to drop the running task count to zero. `maxHealthyPercent: 100` forbids it from running two tasks. Together, these two values turn a rolling replacement into a stop-then-start (`awsplace/cdk/lib/ecs.ts:159-170`).

The cost is obvious: the canvas is unreachable for the duration of the deployment window, on every deployment. There is no overlap to hide behind, no second task serving traffic, and no autoscaling by task count, because a second task means a second writer. I chose that over the alternative, which was a corrupted WAL.

The other half of this bargain is the shutdown time. `stopTimeout: Duration.seconds(120)` gives the container ECS's maximum allowance to handle `SIGTERM` (`ecs.ts:119`). Graceful shutdown stops accepting clients, closes active connections, and publishes a final checkpoint, exiting with code 0 only if that checkpoint succeeds (`runtime-contract.md:118-123`). If the task is killed instead of gracefully stopped, acknowledged commands are still recovered from the synced WAL on EFS, and that exact property is what makes the persistent mount worth its availability cost.

Startup is a mirror image. The replacement task remounts that exact access point, validates the selected snapshot before binding the client port, restores it, and then replays the tail of the WAL. Missing, corrupted, or mismatched data will fail the startup rather than seed an empty database (`runtime-contract.md:114-116`). The health command demands `/tmp/raftdb-ready` and writes a probe file under the data directory, so a read-only or unavailable mount fails health instead of pretending to work (`:105-112`). The App container waits for the RaftDb container to report `HEALTHY` before it starts.

<figure>
  <img src="/images/3-BlogPosted/raftdb-efs-devloop.svg" alt="Activity diagram of the RaftDB development and deploy loop: local named volume, immutable image publication, stop-then-start deployment onto the same EFS access point, snapshot restore and WAL replay, contrasted with the discarded ephemeral-volume path" loading="lazy">
  <figcaption>The entire loop. The left branch is what the EFS access point makes possible; the right branch is what a task-scoped volume would do to the canvas on every deploy.</figcaption>
</figure>

The result is exactly what I wanted from the beginning. A deployment is now a recovery exercise I can sit back and watch, and the canvas on the other side of it is the exact canvas I left behind.

## References

- [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)
- [Amazon ECS: using Amazon EFS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html)
- [Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Amazon ECS rolling update deployment: minimumHealthyPercent and maximumPercent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html)
- [Docker: persist data with volumes](https://docs.docker.com/engine/storage/volumes/)


---
**Original post on AWS Study Group:** [View here](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2228318824599744/#)
