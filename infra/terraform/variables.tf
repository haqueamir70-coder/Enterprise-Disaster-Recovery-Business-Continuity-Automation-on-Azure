variable "location" {
  description = "Approved Azure region for the lab foundation."
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Unique resource group name."
  type        = string
  default     = "rg-bcdr-lab"
}

variable "environment" {
  description = "Environment tag."
  type        = string
  default     = "lab"

  validation {
    condition     = contains(["lab", "dev", "test"], var.environment)
    error_message = "This example foundation is restricted to lab/dev/test."
  }
}

variable "deploy_foundation" {
  description = "Opt-in flag; false keeps the plan empty by default."
  type        = bool
  default     = false
}
