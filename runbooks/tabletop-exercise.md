# Tabletop exercise runbook

**Type:** discussion-based simulation. No Azure changes are performed.

## Participants

Incident commander, recovery lead, identity/network owner, application owner, data owner, security lead, communications lead and evidence recorder.

## Scenario

A synthetic regional outage makes the primary application region unavailable. An identity dependency is degraded. The recovery team decides whether to invoke the BCDR plan.

## Timeline prompts

| Inject | Expected discussion |
|---|---|
| T+0 | Who detects and declares the incident? What evidence is required? |
| T+10 | Which business services are impacted? What tier and MTD apply? |
| T+20 | Is identity, DNS, network and secrets available in recovery? |
| T+30 | Is the last recoverable data point known and consistent? |
| T+45 | Who approves recovery and which plan version is authoritative? |
| T+60 | How are application and business transactions validated? |
| T+75 | Who approves customer traffic restoration? |
| T+90 | What communications, evidence and follow-up actions are required? |

## Evidence

Capture exercise ID, UTC timestamps, participants, plan version, assumptions, decisions, risks, unresolved dependencies, action owner and due date.

## Exit criteria

- Critical dependencies and decision owners identified.
- Recovery sequence reviewed against dependencies.
- RTO/RPO measurement points agreed.
- Gaps assigned to owners.
- Lessons learned approved and tracked.

Do not report tabletop duration as measured technical RTO.
