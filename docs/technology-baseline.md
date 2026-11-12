# Technology baseline

**Last checked: 12 November 2026.** This is a dated snapshot, not an evergreen claim.

| Component | Project baseline | Notes |
|---|---:|---|
| Terraform CLI | >=1.10, <2.0 | Use an organization-approved, pinned CLI build |
| AzureRM provider | 5.13.0 | Release published 5 November 2026 |
| Python | 3.12+ | CI uses Python 3.12 |
| GitHub Actions | checkout v4, setup-python v5, setup-terraform v3 | Check upstream runtime notices and pin immutable SHAs for production |

## Upgrade process

1. Review release notes and breaking changes.
2. Upgrade in a dedicated PR and review lockfile changes.
3. Run fmt, init, validate, Checkov and plan in a non-production subscription.
4. Inspect the exact provider resource support for ASR/Backup before expanding IaC.
5. Never auto-apply provider updates to production DR infrastructure.

## Official references

- AzureRM v5.13.0 release (5 Nov 2026): https://github.com/hashicorp/terraform-provider-azurerm/releases/tag/v5.13.0
- Provider documentation: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- Changelog: https://github.com/hashicorp/terraform-provider-azurerm/blob/main/CHANGELOG.md
- Azure Site Recovery overview: https://learn.microsoft.com/azure/site-recovery/site-recovery-overview
- Azure Backup overview: https://learn.microsoft.com/azure/backup/backup-overview
- Azure reliability: https://learn.microsoft.com/azure/reliability/
- GitHub Actions security: https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions
