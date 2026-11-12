# Test failover runbook (operator-reviewed template)

> Procedural template only. Do not use against production without an approved change and the current Microsoft workload-specific instructions.

## Preconditions

- Approved non-production exercise, named recovery lead and application/data owners.
- Supported source/target workload and region confirmed in the current support matrix.
- Replication health and recovery point reviewed.
- Test network isolated from production; DNS, routing, NSG, firewall and private endpoint design reviewed.
- Data classification, secrets and external integrations reviewed.
- Evidence recorder and cleanup owner identified.
- Success, abort and rollback criteria agreed.

## Procedure

1. Freeze scope and record plan/version, time and approvers.
2. Confirm replication status, recovery point and dependency readiness.
3. Invoke Test failover through the documented ASR workflow for the supported workload, selecting the approved recovery point and isolated network.
4. Validate identity, DNS, secrets, database consistency, app health, synthetic transactions and external dependencies.
5. Record actual milestones and compare against approved objectives.
6. Obtain application and business-owner acceptance.
7. Clean up the test failover using the supported cleanup workflow; verify temporary resources/connectivity are removed.
8. Record evidence, gaps, costs, lessons and next review date.

## Abort conditions

Unexpected production connectivity, uncertain data consistency, missing approval, invalid recovery point, failed security controls or inability to clean up safely.

A test failover does not switch production users, prove failback or automatically establish contractual RTO/RPO.
