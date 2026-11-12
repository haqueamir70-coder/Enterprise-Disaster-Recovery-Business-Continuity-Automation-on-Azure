# Backup and restore validation

## Design checklist

- Identify the correct Azure Backup vault type and datasource support.
- Define backup frequency, retention, consistency model and window.
- Review soft delete, enhanced soft delete, immutability and Resource Guard/MUA availability for the specific vault/datasource/region.
- Separate backup operator, security administrator and workload owner responsibilities.
- Review cross-region/cross-subscription restore and encryption/key dependencies where supported.
- Define restore-test frequency by business risk and compliance obligations.
- Keep restore network isolated and validate recovered data before release.

## Restore evidence

Capture protected item, policy version, recovery-point timestamp, restore mode/location, operator, approver, start/end time, data validation, app validation, observed RTO/RPO, deviations, cleanup and evidence location.

A successful backup job does not prove that an application can be restored or that restored data is transactionally consistent.
