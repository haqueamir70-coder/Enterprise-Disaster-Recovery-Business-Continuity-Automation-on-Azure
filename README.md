# Enterprise Disaster Recovery & Business Continuity Automation on Azure

[![BCDR Lab CI](https://github.com/haqueamir70-coder/Enterprise-Disaster-Recovery-Business-Continuity-Automation-on-Azure/actions/workflows/ci.yml/badge.svg)](https://github.com/haqueamir70-coder/Enterprise-Disaster-Recovery-Business-Continuity-Automation-on-Azure/actions/workflows/ci.yml)

A portfolio-grade reference implementation for designing, validating, and operating business continuity and disaster recovery capabilities on Microsoft Azure.

> **Safety scope:** This is an engineering lab using synthetic plans. It does not connect to production, trigger actual failover, replicate workloads, modify backups, or prove achieved RTO/RPO. Terraform is deliberately opt-in and defaults to no resource creation. Real recovery requires a service-specific design, approved change, operator authorization and a tested non-production environment.

## Engineering outcomes

- Business impact analysis, service tiers, dependency mapping, RTO/RPO and recovery milestones.
- Azure multi-region architecture spanning identity, DNS, networking, secrets, application and data tiers.
- Azure Site Recovery concepts: recovery plans, test failover, planned/unplanned failover, reprotect and failback.
- Azure Backup concepts: vault selection, retention, soft delete, immutability, Resource Guard/MUA and restore validation.
- Terraform Azure foundation, CI validation and IaC security scanning.
- Python readiness validator for recovery order, dependencies, missing services, cycles and RTO/RPO input policy.
- Operational runbooks, tabletop exercise, evidence checklist and **65 interview questions with answers**.

## Architecture

See [architecture/README.md](architecture/README.md) and [architecture/bcdr-reference-architecture.mmd](architecture/bcdr-reference-architecture.mmd).

The logical flow is primary region → supported replication/backup workflows → recovery region → dependency and application validation → business acceptance. Recovery plans coordinate steps; they do not automatically restore DNS, external integrations, identity or data consistency.

## Quick start

Requirements: Python 3.12+.

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m dr.cli validate --plan dr/plans/sample-enterprise.json
python -m pytest -q
ruff check .
```

The validator reports whether a **synthetic JSON model** satisfies local rules. PASS does not mean Azure replication, backup health, recoverability or business RTO/RPO have been verified.

## Terraform: safe-by-default

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
az login
az account show
terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -out=tfplan
```

Default `deploy_foundation=false` creates no Azure resources. To create the optional Resource Group and Log Analytics Workspace, set the flag to true only in an approved lab subscription, review the plan and cost, then apply deliberately. This repository does **not** deploy ASR replication, Backup vaults, recovery plans or production workloads.

## Repository layout

| Directory | Contents |
|---|---|
| `dr/` | Typed recovery-plan model and readiness validation CLI |
| `tests/` | Dependency, ordering and objective validation tests |
| `infra/terraform/` | Opt-in Azure foundation |
| `architecture/` | Reference architecture and diagrams |
| `docs/` | BIA, RTO/RPO, security, backup and decision records |
| `runbooks/` | Tabletop, test failover, failover/failback procedures |
| `interview-prep/` | 65 BCDR/Azure/DevOps interview Q&A |
| `.github/workflows/` | CI quality, security and IaC checks |

## Dated technology baseline — 12 November 2026

AzureRM provider pinned to **5.13.0**, released 5 November 2026. See [technology baseline](docs/technology-baseline.md) for version policy and official upstream links. Versions must be checked again when upgrading.

## Security

Use GitHub OIDC/workload identity federation instead of long-lived Azure client secrets. Enforce least privilege, separate recovery and backup administration, protect vault control planes, isolate test networks, and never commit credentials, Terraform state/plans or real customer metadata.

## Interview preparation

Read [interview-prep/README.md](interview-prep/README.md): 65 detailed questions covering BCDR, ASR, Azure Backup, networking, Terraform, security, monitoring and troubleshooting scenarios.

## Portfolio evidence checklist

- [ ] CI green on the default branch.
- [ ] Python tests and Terraform validation pass.
- [ ] Architecture diagram matches actual code and marks optional services.
- [ ] Synthetic readiness report captured.
- [ ] Tabletop exercise has decisions, timestamps, evidence and action owners.
- [ ] Real Azure lab, if conducted, has approval, budget, cleanup evidence and measured results.
- [ ] No unsupported claim that RTO/RPO was achieved.

## Official documentation

- [Azure Site Recovery overview](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview)
- [Azure Backup overview](https://learn.microsoft.com/azure/backup/backup-overview)
- [Azure reliability](https://learn.microsoft.com/azure/reliability/)
- [Terraform AzureRM provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

Service support, regional availability, feature limits and pricing change. Validate workload-specific Microsoft documentation before real-world implementation.

## License

MIT — see [LICENSE](LICENSE).
