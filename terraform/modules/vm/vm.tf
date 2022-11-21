resource "azurerm_network_interface" "" {
  name                = ""
  location            = ""
  resource_group_name = ""

  ip_configuration {
    name                          = "internal"
    subnet_id                     = ""
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = ""
  location            = ""
  resource_group_name = ""
  size                = "Standard_DS2_v2"
  admin_username      = ""
  network_interface_ids = []
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCy4maxpA/1EPQQQ2aLgcQIOyEPzPhsieBzGUBCRpGYz5RuBHKxX64chDyMAeVkzf1QfEnGSqR6SeKzTmbYYro7YfjHvgMK8K+eN1WVcwHE9T/7pjQSr5ZFI95PDdzY8UCjHmV6w4Y6Bm6anzmZ+CfTBZwESO1Aj+liL+YBL3cIw5B5FsvUdTPptqyqr/wCxjuHwjMle8Eh+a/oAIjWIRUysrhL1M8dP8cYdpQLaChEmukk1Y6eWcDPROgOOm/HFapnq4rayvu4g5EPDxv64VY7Oun1lZ8lt0X6y0vVMYSVv3PpKw55v6725tUB31Sw8r+so/yyKgevdgzHzQYV64pHAoFFFKwHyIDC1EzNAuyKQedrR0aEvZkNQy1xaXIlF/UT6s/QPDNEQB+65wA0oSmKPqfrn+FNwZ/niLeQTHz6Sxc6bNX4HSJt4TLBaoTMrM9tDjmUww+KX0YQzdJbedAuvToQvimEZALMiwAyj5xNP14o6d/Kb21SlTZQTRZzxXs= quocd@QuocDuong"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
