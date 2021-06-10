# Convert this setup into Master Master replication b/w both the VMs.
- ## Configuration on the Slave server:
  - Uncomment below line in `/etc/mysql/mariadb.conf.d/50-server.cnf`:
 
    ```
    log_bin = /var/log/mysql/mysql-bin.log
    log_bin_index =/var/log/mysql/mysql-bin.log.index
    ```
  - Restart the `mariadb.service`.
  - First, log in to MariaDB shell with the following command:
    ```bash
    sudo mysql -u root -p
    ```
    - Provide your root password when prompted, then create a user with the following command:
      ```sql
      MariaDB [(none)]> CREATE USER 'master1'@'%' identified by 'your-password';
      ```
    - Next, grant the replication slave privilege to this user with the following command:
      ```sql
      MariaDB [(none)]> GRANT REPLICATION SLAVE ON *.* TO 'master1'@'%';
      ```
    - Next, flush the privileges with the following command:
      ```sql
      MariaDB [(none)]> FLUSH PRIVILEGES;
      ```
    - Next, check the master server status with the following command:
      ```sql
      MariaDB [(none)]> show master status;
      ```
      - You should get the following output:
        ```sql
        +------------------+----------+--------------+------------------+
        | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
        +------------------+----------+--------------+------------------+
        | mysql-bin.000002 |      315 |              |                  |
        +------------------+----------+--------------+------------------+
        ```
        
     - Next, exit from the MariaDB shell with the following command:
     ```sql
     MariaDB [(none)]> exit;
     ```
   - **Note:** Please remember the **File** and **Position** details from the above output. You will need these values when configuring the slave server.
 
- ## Configuration on the Master server:
  - Log in to MariaDB shell with the following command:
    
    ```bash
    sudo mysql -u root -p
    ```
      - Provide your root password when prompted, then stop the slave threads as shown below:
        ```sql
        MariaDB [(none)]> stop slave;
        ```
      - Next, run the following command to set up the slave to replicate the master:
        ```sql
        MariaDB [(none)]> CHANGE MASTER TO MASTER_HOST = '192.168.1.2', MASTER_USER = 'master1', MASTER_PASSWORD = 'your-password', MASTER_LOG_FILE = 'mysql- bin.000002', MASTER_LOG_POS = 315;
        ```
      - Next, start the slave threads and exit from the MariaDB shell as shown below:
        ```sql
        MariaDB [(none)]> start slave;
        ```
- #### Check Slave status on both the servers ```MariaDB [(none)]> show slave status\G;```. If no error comes the master-master setup is configured successfully.
- ## Test Database Replication
  At this point, you have configured master-master replication. Now, it’s time to test replication between master to slave.
  - On the master server, log in to the MariaDB shell with the following command:
    ```bash
    sudo mysql -u root -p
    ```
    - Provide your root password when prompted.
    - See the databases existing in master server.
      ```sql
      MariaDB [(none)]> show databases;
      +--------------------+
      | Database           |
      +--------------------+
      | Nginx              |
      | information_schema |
      | mysql              |
      | performance_schema |
      | test               |
      | test1              |
      +--------------------+
      ```
    - Create a database with name ```masterside``` as shown below:
      ```sql
      MariaDB [(none)]> create database masterside;
      Query OK, 1 row affected (0.000 sec)

      MariaDB [(none)]> show databases;
      +--------------------+
      | Database           |
      +--------------------+
      | Nginx              |
      | information_schema |
      | masterside         |
      | mysql              |
      | performance_schema |
      | test               |
      | test1              |
      +--------------------+
      ```
  - On the another master(slave) server, log in to the MariaDB shell with the following command:
    ```bash
    sudo mysql -u root -p
    ```
    - Next, run the following command to check whether the database is replicated:
      ```sql
      MariaDB [(none)]> show databases;
      +--------------------+
      | Database           |
      +--------------------+
      | Nginx              |
      | information_schema |
      | masterside         |
      | mysql              |
      | performance_schema |
      | test               |
      | test1              |
      +--------------------+
      ```
     - Create a database with name ```slaveside``` as shown below:
        ```sql
        MariaDB [(none)]> create database slaveside;
        Query OK, 1 row affected (0.000 sec)
        MariaDB [(none)]> show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | Nginx              |
        | information_schema |
        | masterside         |
        | mysql              |
        | performance_schema |
        | test               |
        | test1              |
        | slaveside          |
        +--------------------+
        ```
  - On the master server, log in to the MariaDB shell with the following command, to check whether the new database is replicated or not:
    ```bash
    sudo mysql -u root -p
    ```
    - Next, run the following command to check whether the database is replicated:
      ```sql
      MariaDB [(none)]> create database slaveside;
      Query OK, 1 row affected (0.000 sec)
      MariaDB [(none)]> show databases;
      +--------------------+
      | Database           |
      +--------------------+
      | Nginx              |
      | information_schema |
      | masterside         |
      | mysql              |
      | performance_schema |
      | test               |
      | test1              |
      | slaveside          |
      +--------------------+
      ```
    
