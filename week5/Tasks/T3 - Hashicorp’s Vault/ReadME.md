# Integrate with Hashicorp’s Vault
- Setup Hashicorp’s vault and have your ansible playbook(created in task 2) reference it to create mariadb users.
- Ansible should use your credentials (username and private key) stored in vault to run the playbooks in the corresponding VMs
- Ansible playbook should connect to vault over https (for which you will need to use self signed certificates)
<hr>
