# Azure BCDR Interview Handbook — 65 Questions & Answers

Practical preparation for Azure DevOps, Cloud/Platform Engineering, SRE, Infrastructure and DevSecOps interviews. Expand each answer with a diagram, a measurable example and a trade-off.

## BCDR foundations

**1. What is the difference between business continuity and disaster recovery?**  
Business continuity keeps critical business processes operating during disruption, possibly at a reduced level. Disaster recovery restores technology services and data after an outage. DR is one component of the broader BC program.

**2. Define RTO.**  
Recovery Time Objective is the target maximum elapsed time to restore a service after disruption to an agreed acceptable level. Measure it end-to-end through business acceptance, not only VM boot.

**3. Define RPO.**  
Recovery Point Objective is the maximum targeted data-loss interval measured against the latest acceptable consistent recovery point.

**4. RTO vs RPO?**  
RTO is time to restore service; RPO is the allowable data-loss interval. A workload can meet one and miss the other.

**5. What is a BIA?**  
A Business Impact Analysis identifies critical processes, impact over time, dependencies, maximum tolerable downtime, minimum service levels and recovery priorities.

**6. MTTR vs RTO?**  
MTTR is an observed operational metric (mean time to repair/recover, depending on definition); RTO is a business-approved target. Define start/end points before comparing.

**7. What is MTD/MTPD?**  
Maximum tolerable downtime/period of disruption is the point beyond which business impact becomes unacceptable. RTO should leave margin below it.

**8. What is a recovery tier?**  
A grouping of services by business criticality and recovery targets. Organization-specific tiers should include dependencies, not just application labels.

**9. What is an application dependency map?**  
A graph of services required for the app to function: identity, DNS, network, secrets, databases, queues, APIs, certificates and third parties.

**10. Why can infrastructure recovery meet its target while the business service remains unavailable?**  
The app may lack identity, DNS, keys, routes, valid data, integrations, capacity or business validation. Measure end-to-end service recovery.

**11. What is a tabletop exercise?**  
A discussion-based simulation where responders walk through roles, decisions, communications and assumptions without executing technical changes.

**12. Tabletop vs test failover vs live failover?**  
Tabletop tests process and decisions; test failover starts a recovery copy in an isolated test environment; live failover moves recovery to the secondary environment under approved incident/change control.

## Azure Site Recovery

**13. What is Azure Site Recovery (ASR)?**  
A DR service that orchestrates replication and recovery for supported workloads between supported locations. Verify source/target support and limits.

**14. What is a Recovery Services vault?**  
A management container used by Azure Backup and Azure Site Recovery for supported scenarios. It is not a universal vault for every Azure Backup datasource.

**15. What is an ASR recovery plan?**  
An orchestration object that groups replicated machines and defines recovery order, groups, scripts/manual actions and checkpoints where supported.

**16. What is test failover?**  
A test recovery operation that starts recovered workload instances in a selected test network without affecting production failover state, when performed as documented.

**17. Why use an isolated test network?**  
To prevent duplicate IP/identity conflicts, accidental production writes, unintended customer traffic and cross-environment security exposure.

**18. Planned vs unplanned failover?**  
Planned failover is initiated when source infrastructure is available and can coordinate shutdown/synchronization to reduce data loss. Unplanned failover handles an outage where the source may be unavailable and uses an available recovery point.

**19. What is reprotect?**  
After failover, reprotect configures protection in the reverse direction where supported so the recovered site becomes the replication source.

**20. Is failback simply reversing failover?**  
No. It requires reverse protection, synchronization, data reconciliation, a cutback window, validation and separate approval.

**21. What should be checked before enabling ASR?**  
Workload support, source/target region, OS/disk/VM limits, network connectivity, required components, permissions, capacity, encryption and cost.

**22. What is a recovery point?**  
A point-in-time replicated state selected for recovery. The newest point may not always be the best if application consistency is uncertain.

**23. What is application-consistent recovery?**  
A recovery point coordinated with application/OS mechanisms to improve data consistency. Support and behavior depend on workload/configuration.

**24. How do you validate recovered VMs?**  
Validate boot/agent health, identity, DNS, routes, mounted disks, services, dependencies, synthetic transactions, data consistency and business acceptance.

**25. Does ASR protect every Azure service?**  
No. ASR supports specific workload types/configurations. PaaS services often use service-specific geo-replication, backup or native resilience.

**26. How do you design recovery order?**  
Recover shared dependencies first—identity, DNS, network, keys—then data platform, middleware, APIs and front end. Confirm via dependency graph and service owners.

**27. What if the recovery region lacks quota or capacity?**  
Recovery can be blocked/delayed. Pre-check quotas, VM SKU availability, zonal/region capacity and IP ranges; evaluate reserved capacity where justified.

## Azure Backup

**28. What is Azure Backup?**  
A managed service protecting supported workloads/data sources through policies, vaults and recovery points.

**29. Recovery Services vault vs Backup vault?**  
Different vault types support different workloads/features. Select based on current datasource support, not assumption.

**30. What is a backup policy?**  
Defines backup schedule/frequency, retention and applicable workload settings. Policy design should map to business RPO and retention.

**31. What is soft delete?**  
A protection feature retaining deleted backup data for a defined/relevant period to help recover from accidental/malicious deletion. Behavior depends on workload/vault.

**32. What is immutable backup?**  
Backup data is protected against modification/deletion according to supported immutability controls. Validate vault type, datasource, lock mode and implications.

**33. What is Resource Guard / multi-user authorization?**  
An additional authorization layer for sensitive backup operations, helping protect against compromised backup administrators. Supported operations vary.

**34. Why is a successful backup job not enough?**  
It does not prove that data can be restored, the app is consistent, dependencies work or the service meets RTO. Execute restore tests.

**35. What is cross-region restore?**  
A feature enabling recovery from a secondary region for supported backup scenarios. Availability/constraints vary by vault, datasource and region.

**36. How do you protect backup from ransomware?**  
Use least privilege, MFA/PIM, soft delete, immutability where supported, Resource Guard/MUA, monitoring, isolated credentials, separate subscriptions and tested restores.

**37. How do you choose retention?**  
Based on regulatory/legal needs, business requirements, recovery scenarios, data lifecycle, storage cost and immutability constraints.

**38. What should a restore test capture?**  
Recovery point, restore mode, start/end time, data validation, app validation, approver, operator, actual RTO/RPO, deviations, cleanup and evidence.

## Azure architecture and networking

**39. How do you select a recovery region?**  
Assess service availability, regional pairing guidance, data residency, latency, capacity/quota, dependencies, connectivity, cost and business risk.

**40. What is an Azure region pair?**  
A Microsoft-defined pairing used for certain platform update/geo-redundancy considerations. Pairing does not mean every service automatically replicates or fails over.

**41. Availability zone vs regional DR?**  
Availability zones address datacenter-level failures within a region; regional DR addresses loss of an entire region. They solve different failure domains.

**42. Why is DNS critical during DR?**  
Users/services must resolve endpoints in the recovery region. TTL, private DNS, resolver reachability, split-horizon and caching affect cutover.

**43. Which network dependencies are often missed?**  
UDRs, NSGs, firewalls, NAT/egress, private endpoints, private DNS zones, peering, VPN/ExpressRoute, identity endpoints and third-party allowlists.

**44. How do private endpoints affect DR?**  
Private endpoint NICs and DNS records are regional/network-context dependent. Recovery design must create/validate target-region endpoints and DNS resolution.

**45. How do you prevent split-brain?**  
Ensure only one authoritative write site. Use controlled failover, fencing/quorum/lease mechanisms where appropriate, traffic control and data consistency checks.

**46. What is a degraded-mode strategy?**  
A minimum acceptable service level during recovery, such as read-only mode, limited features, queued writes or manual fallback.

## Terraform and automation

**47. Why use Terraform for DR infrastructure?**  
It enables repeatable infrastructure, configuration review, drift detection and recovery-environment provisioning. It does not replace service-specific recovery orchestration.

**48. What belongs in Terraform state?**  
Resource identity/attributes required to manage infrastructure. State can contain sensitive values and must be encrypted, access-controlled, locked and backed up.

**49. How do you secure Terraform state?**  
Use a remote backend with encryption, RBAC, network controls, locking, versioning/backup and restricted CI identity. Never commit state or plan files.

**50. Why run Terraform plan before apply?**  
Plan exposes proposed changes for human review, policy checks and blast-radius assessment. In DR, unintended replacement can damage recovery capability.

**51. How would you implement CI/CD for Terraform?**  
PR validation (fmt, validate, security/policy scan), OIDC auth, plan artifact/review, approvals, controlled apply, drift monitoring and audit logs.

**52. Why OIDC instead of a service-principal secret?**  
Federated short-lived tokens reduce long-lived credential storage/rotation exposure. Scope trust to repo, branch/environment and required permissions.

**53. What is idempotency?**  
Repeated execution with the same desired state converges to the same result without unintended additional changes. Automation should safely handle retries.

**54. How do you handle secrets in a pipeline?**  
Prefer managed identities/federated credentials; retrieve secrets at runtime only when necessary; mask logs; minimize permissions and lifetime.

**55. How do you test DR automation without Azure charges?**  
Unit-test plan parsing, dependency graphs, policy checks and simulated state transitions; use static Terraform validation and mocked boundaries. Real recovery needs an approved lab.

## Security, governance and scenario troubleshooting

**56. How do you separate duties in DR?**  
Separate declaration/approval, platform deployment, backup administration, recovery operations and business acceptance. Use just-in-time elevation and audit approvals.

**57. What is least privilege in a DR environment?**  
Each identity receives only the roles/scope needed for its defined task, with time-bound elevation for sensitive operations.

**58. Why should backup admins not be the only recovery approvers?**  
A single compromised/misused identity could destroy protection and recovery. Independent authorization reduces concentration risk.

**59. What is a break-glass account?**  
An emergency privileged identity used when normal authentication/control paths fail. It must be tightly controlled, monitored and periodically tested.

**60. Which DR metrics belong on a dashboard?**  
Protected workload count, replication health/lag, last recovery-point age, backup job/restore status, dependency readiness, quota headroom, observed RTO/RPO and action backlog.

**61. How do you prove an application is recovered?**  
Use synthetic transactions, data integrity checks, dependency checks, security validation, error/latency thresholds and business owner sign-off.

**62. Region is down but VMs recovered; users cannot connect. What do you check?**  
DNS, Front Door/Traffic Manager or routing, firewall/NSG, private endpoint DNS, certificates, identity, WAF, public IP and dependency allowlists.

**63. Latest recovery point is older than RPO. What do you do?**  
Escalate the RPO gap, quantify data-loss exposure, select the safest consistent point, preserve evidence and reconcile data after recovery.

**64. Test failover succeeded but cleanup failed. What is the risk?**  
Orphan resources, cost, duplicate identities/IPs and unintended connectivity. Keep the exercise open, isolate resources, follow cleanup guidance and verify removal.

**65. Recovery plan is green but database cannot accept writes. What now?**  
Business recovery is incomplete. Check data consistency, primary/secondary role, network, authentication, storage and app configuration; do not send production traffic until validated.

## Interview answer framework

For scenario questions, structure your answer as: **impact → scope → authority → recovery point → dependencies → execution → validation → communication → evidence → lessons learned**. State assumptions and distinguish lab simulation from proven production recovery.
