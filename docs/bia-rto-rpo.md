# Business impact analysis, RTO and RPO

## Definitions

- **BIA:** assessment of business processes, impact over time, dependencies, maximum tolerable downtime and recovery priorities.
- **RTO:** target maximum elapsed time to restore the service to an agreed acceptable level.
- **RPO:** maximum targeted data-loss interval, measured against the latest acceptable consistent recovery point.
- **MTD/MTPD:** maximum tolerable period of disruption before impacts become unacceptable.
- **MBCO:** minimum acceptable service level during disruption.

## Example tiers (illustrative only)

| Tier | Example service | Target RTO | Target RPO | Design implication |
|---|---|---:|---:|---|
| 0 | Identity, DNS, network | 30 min | 15 min | Pre-staged dependencies and tested emergency access |
| 1 | Revenue-critical API/data | 90 min | 30 min | Replication/restore and consistency validation |
| 2 | Customer web experience | 4 hr | 1 hr | Redeploy immutable artifacts and controlled traffic switch |
| 3 | Analytics/batch | 24 hr | 24 hr | Scheduled restore/rebuild may be acceptable |

Targets must be agreed with service owners and risk stakeholders. These numbers are sample inputs, not Microsoft service guarantees.

## Measurement model

Record incident declaration, recovery decision, dependencies ready, data recovery-point timestamp, app start, end-to-end synthetic transaction success and business owner acceptance.

- Observed RTO = service acceptance timestamp − agreed recovery start timestamp.
- Observed RPO = disruption timestamp − latest validated consistent recovery-point timestamp.

Do not use VM boot time as service RTO or replication lag alone as verified application RPO.

## BIA workshop prompts

1. Which business process stops if this service is unavailable?
2. What is financial, legal, safety, customer and reputational impact by time interval?
3. What is maximum tolerable downtime and minimum service level?
4. Which identity, DNS, network, secrets, data and third-party services are prerequisites?
5. What data consistency, transaction replay and reconciliation are required?
6. Who can declare a disaster and authorize failover?
7. What evidence demonstrates recovery and acceptance?
8. Which dependencies are outside the team's control?

Targets require business-owner and risk approval. Revisit after major architecture or regulatory changes.
