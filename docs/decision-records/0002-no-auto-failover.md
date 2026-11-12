# ADR 0002: No automatic production failover in this lab

- **Status:** Accepted
- **Decision:** Automation validates plans and produces readiness reports; it does not trigger production failover/failback.
- **Context:** Failover can create data loss, split-brain, customer impact and significant cost if invoked incorrectly.
- **Consequences:** Real recovery requires service-specific instructions, approved incident/change, explicit human authorization, isolated test network where appropriate and evidence capture.
