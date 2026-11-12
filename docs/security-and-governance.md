# Security and governance design

## Identity and access

- Use Microsoft Entra ID and least-privilege RBAC.
- Separate backup administration, recovery operation, platform deployment and application validation.
- Use PIM/JIT elevation where licensed and available.
- Maintain monitored emergency access accounts with named owners.
- Prefer managed identities for Azure workload access.
- For GitHub Actions to Azure, use OIDC/workload identity federation; do not store long-lived client secrets.

## Backup protection

Evaluate soft delete, enhanced soft delete, immutability where supported, Resource Guard/MUA, vault access controls and cross-region/subscription restore. Exact controls depend on vault type, datasource, region and feature support. Protect backup data and identities that can delete or alter it.

## Network

- Test recovery in isolated address space with no accidental production route.
- Pre-plan IP mapping, route tables, NSGs/firewalls, private DNS, private endpoints and outbound egress.
- Validate that recovery dependencies can resolve and authenticate in the target region.
- Define controlled ingress and DNS TTL/cutover strategy.

## Data and secrets

- Validate encryption, key availability, CMK permissions and regional dependencies.
- Never commit secrets, Terraform state/plans, customer data or sensitive topology.
- Treat backup metadata, resource IDs and recovery evidence as sensitive operational information.

## Change control

Require a change record, named recovery commander, technical approvers, business-owner approval, rollback criteria, communications plan and post-exercise cleanup. The repository validator does not authorize or execute Azure operations.
