# :dart: Week 4 Tasks Lists 
# Introduction to Ansible
- ### Intent: Learn the fundamentals of Ansible 
  - Task: Run a shell command on 3 VMs from your local machine and save its output in a file locally.

## Galera cluster setup using Ansible
- ### Intent: Explore different ansible modules. Design automation
  - #### Tasks: Write a ansible playbook to automate the entire setup of a galera cluster. 
   - The playbook should include:
      - Setup of 3 node galera cluster.
      - Demote the 3rd node to an async slave. 
      - Provisions to uninstall/destroy the cluster.
      - The playbook should be idempotent (i.e running the playbook multiple times shouldn't affect the setup).
      - The cluster once setup should have only 2 new users - one for you with read/write permissions and another called monitoring with only read permissions.

#  Additional tasks
- ## Integrate with Hashicorp’s Vault:
  - ### Intent: Explore Hashicorp’s Vault
    - ####  Tasks
      - Setup Hashicorp’s vault and have your ansible playbook(created in task 2) reference it to create mariadb users. 
      - Ansible should use your credentials (username and private key) stored in vault to run the playbooks in the corresponding VMs
      - Ansible playbook should connect to vault over https (for which you will need to use self signed certificates)
