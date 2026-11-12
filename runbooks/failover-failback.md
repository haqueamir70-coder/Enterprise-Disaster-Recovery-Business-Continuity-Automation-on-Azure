# Planned/unplanned failover, reprotect and failback

Use the Azure Site Recovery instructions for the exact protected workload type and current service experience.

## Decision and authorization

- Incident commander declares the event using approved criteria.
- Business owner approves recovery decision and accepted data-loss exposure.
- Recovery lead confirms supported workload, region, recovery point and dependency availability.
- Communications lead coordinates updates.
- Record approvals and timestamps.

## High-level phases

1. **Assess:** identify blast radius, replication health, application/data consistency and dependencies.
2. **Select:** choose a supported recovery point based on agreed data-loss tolerance.
3. **Recover:** perform planned or unplanned failover through the documented service workflow.
4. **Validate:** restore identity/network/secrets, application tiers, data integrity, synthetic transactions and business acceptance.
5. **Stabilize:** monitor errors, latency, data writes, queues, DNS and integrations.
6. **Reprotect:** configure reverse replication where supported and wait for a healthy protected state.
7. **Failback:** schedule a separate approved cutback, reconcile data, execute supported workflow, validate and monitor.
8. **Close:** preserve evidence, update plans and run a post-incident review.

Never assume every workload supports the same sequence, that DNS/external dependencies are automatic, or that failback is just another failover click.
