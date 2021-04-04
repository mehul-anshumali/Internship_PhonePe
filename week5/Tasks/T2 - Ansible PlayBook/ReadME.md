# Write a ansible playbook to automate the entire setup of a galera cluster.
- ## The playbook should include:
  - Setup of 3 node galera cluster.
  - Demote the 3rd node to an async slave.
  - Provisions to uninstall/destroy the cluster.
  - The playbook should be idempotent (i.e running the playbook multiple times shouldn't affect the setup).
  - The cluster once setup should have only 2 new users - one for you with read/write permissions and another called monitoring with only read permissions.
<hr>
