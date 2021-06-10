# On an another VM install MariaDB and configure it as the slave of the MariaDB installed in above step.

- ## Install MariaDB
  Follow the task one and install the MariaDB :point_right: <a href="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week4/T1%20-     %20MariaDB%20Installation%2C%20User%20and%20Database%20creation.md">MaridDB Installation</a>.

- ## Configure Master Server
  First configure the 1st VM as a master server before configuring the slave server.
  - You will need to enable binary logging and replication on the master server. To do so, open the file **/etc/mysql/mariadb.conf.d/50-server.cnf** with your preferred  text editor:
    ```bash
    sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
    ```
    - Find the line bind-address and change the value to ```VMs IP``` to allow inbound connections.
      ```
      bind-address = 192.168.1.1
      ```
      Next, find the ```server-id``` and uncomment it and set its value to 1.
      ```
      server-id = 1
      ```
      > **server-id must be different and unique for each server**
  
      Below the server-id uncomment the ```log_bin = /var/log/mysql/mysql-bin.log```
  
      Add the below lines,
      ```
      log_bin_index =/var/log/mysql/mysql-bin.log.index
<!--       relay_log = /var/log/mysql/mysql-relay-bin -->
<!--       relay_log_index = /var/log/mysql/mysql-relay-bin.index -->
      ```
  - Save and close the file when you are finished. Then, restart the MariaDB service to implement the changes:
    ```bash
    sudo systemctl restart mariadb
    ```
  - Next, you will need to create a replication user. The slave server will use this user to log into the master server and request binary logs.
  
  - First, log in to MariaDB shell with the following command:
    ```bash
    sudo mysql -u root -p
    ```
    - Provide your root password when prompted, then create a user with the following command:
      ```sql
      MariaDB [(none)]> CREATE USER 'your-username'@'%' identified by 'your-password';
      ```
    - Next, grant the replication slave privilege to this user with the following command:
      ```sql
      MariaDB [(none)]> GRANT REPLICATION SLAVE ON *.* TO 'your-username'@'%';
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
        | mysql-bin.000001 |      919 |              |                  |
        +------------------+----------+--------------+------------------+
        ```
        
     - Next, exit from the MariaDB shell with the following command:
     ```sql
     MariaDB [(none)]> exit;
     ```
   - **Note:** Please remember the **File** and **Position** details from the above output. You will need these values when configuring the slave server.
 - ## Configure Slave Server
   First configure the 1st VM as a master server before configuring the slave server.
    - You will need to enable binary logging and replication on the master server. To do so, open the file **/etc/mysql/mariadb.conf.d/50-server.cnf** with your preferred  text editor:
      ```bash
      sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
      ```
      - Find the line bind-address and change the value to ```VMs IP``` to allow inbound connections.
        ```
        bind-address = 192.168.1.2
        ```
        Next, find the ```server-id``` and uncomment it and set its value to 1.
        ```
        server-id = 2
        ```
        > **server-id must be different and unique for each server**

        Below the server-id uncomment the ```log_bin = /var/log/mysql/mysql-bin.log```

        Add the below lines,
        ```
<!--         log_bin_index =/var/log/mysql/mysql-bin.log.index -->
        relay_log = /var/log/mysql/mysql-relay-bin
        relay_log_index = /var/log/mysql/mysql-relay-bin.index
        ```
    - Save and close the file when you are finished. Then, restart the MariaDB service to implement the changes:
      ```bash
      sudo systemctl restart mariadb
      ```
    - Next, log in to MariaDB shell with the following command:
      ```bash
      sudo mysql -u root -p
      ```
        - Provide your root password when prompted, then stop the slave threads as shown below:
          ```sql
          MariaDB [(none)]> stop slave;
          ```
        - Next, run the following command to set up the slave to replicate the master:
          ```sql
          MariaDB [(none)]> CHANGE MASTER TO MASTER_HOST = '192.168.1.1', MASTER_USER = 'your-username', MASTER_PASSWORD = 'your-password', MASTER_LOG_FILE = 'mysql- bin.000001', MASTER_LOG_POS = 919;
          ```
        - Next, start the slave threads and exit from the MariaDB shell as shown below:
          ```sql
          MariaDB [(none)]> start slave;
          MariaDB [(none)]> show slave status\G;
          ```
          ```
          *************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.1.1
                  Master_User: master
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 919
               Relay_Log_File: mysql-relay-bin.000002
                Relay_Log_Pos: 945
          Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
          ```
         - Next, exit from the MariaDB shell with the following command:
           ```sql
           MariaDB [(none)]> exit;
           ```
- ## Test Database Replication
  At this point, you have configured master-slave replication. Now, it’s time to test replication between master to slave.
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
      +--------------------+
      ```
      As you can see no user-defined databases are there, then create a database with name ```test``` as shown below:
      ```sql
      MariaDB [(none)]> create database test;
      ```
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
      +--------------------+
      ```
  - On the slave server, log in to the MariaDB shell with the following command:
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
      | mysql              |
      | performance_schema |
      | test               |
      +--------------------+
      ```
    - Create a database name ```test1``` see if it replicates on master server or not. If not then master-slave setup is successfully configured.
