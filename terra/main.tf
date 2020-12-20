terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.26"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "location" {
  type = string  
  description = "Geographic location of cloud resources"
  default = "westeurope"
}

# resource group
resource "azurerm_resource_group" "rb_group" {
  name = "rb_group"
  location = var.location
}

# network
resource "azurerm_virtual_network" "rb_vnet" {
  name = "rb_vnet"
  resource_group_name = azurerm_resource_group.rb_group.name
  location = var.location
  address_space = [ "10.0.0.0/16" ]
}

resource "azurerm_subnet" "rb_subnet" {
  name = "rb_subnet"
  resource_group_name = azurerm_resource_group.rb_group.name
  virtual_network_name = azurerm_virtual_network.rb_vnet.name
  address_prefixes = ["10.0.10.0/24"]
}

resource "azurerm_network_security_group" "rb_nsg" {
  name = "rb_nsg"
  location = var.location
  resource_group_name = azurerm_resource_group.rb_group.name

  security_rule {
    name = "SSH"
    priority = 1001
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"
    source_port_range = "*"
    destination_port_range = "22"
    source_address_prefix = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_public_ip" "rb_publicip" {
  name = "rb_public_ip"
  location = var.location
  resource_group_name = azurerm_resource_group.rb_group.name
  allocation_method = "Static"
}

resource "azurerm_network_interface" "rb_nic" {
  name = "rb_nic"
  location = var.location
  resource_group_name = azurerm_resource_group.rb_group.name

  ip_configuration {
    name  = "rb_nic_config"
    subnet_id = azurerm_subnet.rb_subnet.id
    private_ip_address_allocation = "dynamic"
    public_ip_address_id = azurerm_public_ip.rb_publicip.id
  }
}