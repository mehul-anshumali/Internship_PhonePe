# Convert this setup into two nodes Galera clusters and then add another node to this cluster.
- ## Configure First Server (VM1)
  - Create a Galera configuration file with the following command:
    ```
    sudo nano /etc/mysql/conf.d/galera.cnf
    ```
    - Add the following lines:
      ```
      [mysqld]
      binlog_format=ROW
      default-storage-engine=innodb
      innodb_autoinc_lock_mode=2
      bind-address=0.0.0.0

      # Galera Provider Configuration
      wsrep_on=ON
      wsrep_provider=/usr/lib/galera/libgalera_smm.so

      # Galera Cluster Configuration
      wsrep_cluster_name="galera_cluster"
      wsrep_cluster_address="gcomm://192.168.1.1,192.168.1.2"

      # Galera Synchronization Configuration
      wsrep_sst_method=rsync

      # Galera Node Configuration
      wsrep_node_address="192.168.1.1"
      wsrep_node_name="node1"
      ```
    - Save and close the file when you are finished.

- ## Configure Second Server (VM2)
  - Create a Galera configuration file with the following command:
    ```
    sudo nano /etc/mysql/conf.d/galera.cnf
    ```
    - Add the following lines:
      ```
      [mysqld]
      binlog_format=ROW
      default-storage-engine=innodb
      innodb_autoinc_lock_mode=2
      bind-address=0.0.0.0

      # Galera Provider Configuration
      wsrep_on=ON
      wsrep_provider=/usr/lib/galera/libgalera_smm.so

      # Galera Cluster Configuration
      wsrep_cluster_name="galera_cluster"
      wsrep_cluster_address="gcomm://192.168.1.1,192.168.1.2"

      # Galera Synchronization Configuration
      wsrep_sst_method=rsync

      # Galera Node Configuration
      wsrep_node_address="192.168.1.2"
      wsrep_node_name="node2"
      ```
    - Save and close the file when you are finished.

- ## Initialize the Galera Cluster
  - Before starting the cluster, you will need to stop the MariaDB service on all servers.
  - Run the following command to stop the MariaDB service on all servers.
    ```
    sudo systemctl stop mariadb
    ```
  - Next, initialize the cluster in the first node with the following command:
    ```
    galera_new_cluster
    ```
  - The above command will start the cluster and add node1 to the cluster.
  - You can check it with the following command:
    ```
    sudo mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
    Enter password:
    ```
  - Provide your root password and hit Enter. You should see the following output:
    ```
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | wsrep_cluster_size | 1     |
    +--------------------+-------+
    ```
  - Next, go to the second server and start the MariaDB service:
    ```
    sudo systemctl start mariadb
    ```
  - Next, verify your cluster size with the following command:
    ```
    sudo mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
    Enter password:
    ```
  - Provide your root password and hit Enter. You should see that the second server has joined the cluster.
    ```
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | wsrep_cluster_size | 2     |
    +--------------------+-------+
    ```
- ## Add another node
  - To do this create a new VM and install MariaDB in it.
  - Create a Galera configuration file with the following command:
    ```
    sudo nano /etc/mysql/conf.d/galera.cnf
    ```
    - Add the following lines:
      ```
      [mysqld]
      binlog_format=ROW
      default-storage-engine=innodb
      innodb_autoinc_lock_mode=2
      bind-address=0.0.0.0

      # Galera Provider Configuration
      wsrep_on=ON
      wsrep_provider=/usr/lib/galera/libgalera_smm.so

      # Galera Cluster Configuration
      wsrep_cluster_name="galera_cluster"
      wsrep_cluster_address="gcomm://192.168.1.1,192.168.1.2,192.168.1.3"

      # Galera Synchronization Configuration
      wsrep_sst_method=rsync

      # Galera Node Configuration
      wsrep_node_address="192.168.1.3"
      wsrep_node_name="node3"
      ```
    - Save and close the file when you are finished.
  - Restart the MariaDB service.
    ```
    sudo systemctl restart mariadb
    ```
  - Next, verify your cluster size with the following command:
    ```
    sudo mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
    Enter password:
    ```
  - Provide your root password and hit Enter. You should see that the third server has joined the cluster.
    ```
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | wsrep_cluster_size | 3     |
    +--------------------+-------+
    ```

- ##  Test Galera Cluster Replication
  - Your Galera cluster is now up and running. It’s time to test and see whether replication is working.
  - To do so, create databases on servers and check whether it has been replicated to other servers.

