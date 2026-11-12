output "resource_group_id" {
  description = "Resource group ID; null when deploy_foundation=false."
  value       = try(azurerm_resource_group.bcdr[0].id, null)
}

output "log_analytics_workspace_id" {
  description = "Workspace ID; null when deploy_foundation=false."
  value       = try(azurerm_log_analytics_workspace.bcdr[0].id, null)
}
