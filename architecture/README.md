# Reference architecture

Logical architecture only; it is not a deployment manifest. Verify regional pairing, service support, quotas, networking and workload limits against current Microsoft documentation.

## Components

- Primary region: production workload and source data.
- Recovery region: pre-provisioned or deploy-on-recovery dependencies, protected workload components and isolated test network.
- Azure Site Recovery: supported compute replication and recovery-plan orchestration.
- Azure Backup: workload-specific backup protection and restore; vault type and features depend on datasource.
- Identity: Microsoft Entra ID, privileged access, managed identities and emergency access.
- Network: hub/spoke or Virtual WAN, private DNS, private endpoints, firewalls, routes and controlled ingress.
- Operations: incident commander, recovery lead, app/data owners, communications lead and evidence recorder.

## Design decisions

1. Select regions based on service availability, data residency, capacity, latency, connectivity and business risk.
2. RTO is end-to-end service restoration, not VM boot time.
3. RPO is based on the latest validated consistent recovery point.
4. Protect backup control plane separately from compute replication.
5. Test failover uses an isolated network and documented cleanup.
6. Failback is a separately approved workflow involving reprotection, synchronization, reconciliation and validation.

See [bcdr-reference-architecture.mmd](bcdr-reference-architecture.mmd).
