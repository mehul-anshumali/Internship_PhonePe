# Upgrade the Galera cluster from 10.5.6 to 10.5.9.
- ## Backup preparation
  - The backup we did in the last step that must be prepared:
    ```
    mariabackup --prepare \
     --target-dir=/home/mehul/backup/
    ```
- ## Uninstall the Old Version
  - When upgrading to a new release of MariaDB, it is necessary to remove the existing installation of MariaDB, before installing the new version of MariaDB versions.
 
  - **Stop the Galera Cluster node**
 
    -  Before the old version can be uninstalled, we first need to stop the node.
      ```
      sudo systemctl stop mariadb
      ```
    - Uninstall via APT (Debian/Ubuntu).
      ```
      sudo apt remove "mariadb-*"
      ```
    - Uninstall the Galera package as well.
      ```
      sudo apt remove galera-4
      sudo apt remove galera
      ```
    - Before proceeding, verify that all MariaDB packages are uninstalled. The following command should not return any results:
      ```
      apt list --installed | grep -i -E "mariadb|galera"
      ```
      **Gives some warnings ignore** 
     
  - **Install the New Version**
  
    - Configure the APT package repository.
      ```
      sudo apt install wget

      wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup

      echo "6528c910e9b5a6ecd3b54b50f419504ee382e4bdc87fa333a0b0fcd46ca77338 mariadb_repo_setup" \
          | sha256sum -c -

      chmod +x mariadb_repo_setup
      ```
      ```
      sudo ./mariadb_repo_setup \
      --mariadb-server-version="mariadb-10.5"
      ```
      - **If it gives any error like:**
        ```
        [error] The following package is needed by the script, but not installed:
            apt-transport-https
        Please install and rerun the script.
        ```
        - To resolve this issue, type the following command:
          ```
          sudo apt-get install -f apt-transport-https
          ```
          - Again run the following command:
            ```
            sudo ./mariadb_repo_setup \
              --mariadb-server-version="mariadb-10.5"
            ```
      - Update System
        ```
        sudo apt update && sudo apt upgrade
        ```
      - Install MariaDB and package dependencies
        ```
        sudo apt install mariadb-server mariadb-client
        ```
      - Upgrade the Data Directory
        ```
        sudo mariadb-upgrade
        ```
       
  - **Testing**
  
    - Login to MariaDB Shell Test login to MariaDB shell using mysql command:
      ```
      sudo mysql -u root -p
      ```
      ```
      Welcome to the MariaDB monitor.  Commands end with ; or \g.
      Your MariaDB connection id is 9
      Server version: 10.5.9-MariaDB MariaDB Server

      Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

      Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

      MariaDB [(none)]> SHOW GLOBAL VARIABLES LIKE 'version';
      +---------------+-------------------------------------+
      | Variable_name | Value                               |
      +---------------+-------------------------------------+
      | version       | 10.5.9-MariaDB-1:10.5.9+maria~focal |
      +---------------+-------------------------------------+
      1 row in set (0.001 sec)

      MariaDB [(none)]> SELECT VERSION();
      +-------------------------------------+
      | VERSION()                           |
      +-------------------------------------+
      | 10.5.9-MariaDB-1:10.5.9+maria~focal |
      +-------------------------------------+
      1 row in set (0.000 sec)
      ```
    - Restart the MariaDB service.
      ```
      sudo systemctl restart mariadb
      ```
    - Next, verify your node joins the cluster with the following command
      ```
      sudo mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
      Enter password:
      ```
    - Provide your root password and hit Enter. You should see that the node has joined the cluster.
      ```
      +--------------------+-------+
      | Variable_name      | Value |
      +--------------------+-------+
      | wsrep_cluster_size | 3     |
      +--------------------+-------+
      ```

