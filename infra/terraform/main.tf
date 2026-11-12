locals {
  common_tags = {
    project     = "azure-bcdr-lab"
    environment = var.environment
    managed_by  = "terraform"
    purpose     = "disaster-recovery-learning"
  }
}

resource "azurerm_resource_group" "bcdr" {
  count    = var.deploy_foundation ? 1 : 0
  name     = var.resource_group_name
  location = var.location
  tags     = local.common_tags
}

resource "azurerm_log_analytics_workspace" "bcdr" {
  count               = var.deploy_foundation ? 1 : 0
  name                = "${var.resource_group_name}-law"
  location            = azurerm_resource_group.bcdr[0].location
  resource_group_name = azurerm_resource_group.bcdr[0].name
  sku                 = "PerGB2018"
  retention_in_days   = 30
  tags                = local.common_tags
}
