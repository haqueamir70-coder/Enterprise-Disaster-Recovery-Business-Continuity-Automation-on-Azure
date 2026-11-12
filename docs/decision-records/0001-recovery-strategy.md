# ADR 0001: Workload-specific recovery strategy

- **Status:** Accepted for this lab
- **Decision:** Separate compute replication, data backup/restore and native PaaS resilience into workload-specific patterns.
- **Context:** One generic "DR enabled" switch cannot describe recovery capability across Azure services.
- **Consequences:** Each service needs a support-matrix reference, owner, recovery method, consistency model, RTO/RPO, dependencies, test evidence and cost model. Terraform foundation remains separate from actual service onboarding.
