# BCDR operations checklist

## Before an incident
- [ ] BIA and service-tier owners are current.
- [ ] Dependencies and recovery order are reviewed.
- [ ] Recovery plan is versioned and approved.
- [ ] Replication and backup health are monitored.
- [ ] Recovery-region quota, SKUs, network and access are reviewed.
- [ ] Test failover/restore is scheduled.
- [ ] Emergency access and communication tree are tested.

## During an incident
- [ ] Incident commander declares event and scope.
- [ ] Business owner approves recovery decision.
- [ ] Recovery point and data-loss exposure are recorded.
- [ ] Identity, DNS, network, keys and data prerequisites are validated.
- [ ] Recovery actions and timestamps are logged.
- [ ] Application/business owners accept service before release.

## After an incident/exercise
- [ ] Reprotect/failback considered and separately approved.
- [ ] Temporary resources/connectivity cleaned up.
- [ ] Actual RTO/RPO and deviations documented.
- [ ] Costs, security events and lessons reviewed.
- [ ] BIA, runbooks and architecture updated.
