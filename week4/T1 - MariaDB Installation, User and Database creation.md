# On a standalone VM, install MariaDB 10.5.6 and create a user same as your laptop login user then, create database Nginx and restore the SQL file attached in the mail.

- ## Install MariaDB 10.5.6 on Ubuntu 20.04 (Focal Fossa)
  To install MariaDB 10.5.6 on Ubuntu 20.04, you need to add MariaDB repository on to the system. Then the installation of MariaDB 10.5.6 on Ubuntu 20.04 will be done from the APT repository added without any issues.

  - **Update System**

    Ensure your system is updated and install software-properties-common package.
    ```
    sudo apt update && sudo apt upgrade
    sudo apt -y install software-properties-common
    ```
  - **Import MariaDB gpg key**

    Run the command below to add Repository Key to the system:
    ```
    sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'
    ```
  - **Add MariaDB APT repository**

    After importation of repository GPG key, add the APT repository by running the following command:
    ```
    sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://archive.mariadb.org/mariadb-10.5.6/repo/ubuntu/ focal main'
    ```
  - **Install MariaDB Server on 20.04 Linux**

    The last step is the installation of MariaDB Server:
    ```
    sudo apt update
    sudo apt install mariadb-server mariadb-client
    ```
    Hit the **y** key to accept installation of MariaDB 10.5.6 on Ubuntu 20.04 Linux.

  - **Secure MariaDB Server on 20.04 Linux**
    ```
    sudo mysql_secure_installation
    ``` 
  - **Checking Status**
    The database service should be started automatically after installation.
    ```
    sudo systemctl status mysql
    ```
  - **Login to MariaDB Shell**
    Test login to **MariaDB** shell using mysql command:
    ```
    sudo mysql -u root -p
    ```
  - **Check version using the command**
    ```
    MariaDB [(none)]> SELECT VERSION();
    +-----------------------------------------+
    | VERSION() |
    +-----------------------------------------+
    | 10.5.6-MariaDB-1:10.5.6+maria~focal     |
    +-----------------------------------------+
    1 row in set (0.000 sec)
    MariaDB [(none)]>
    ```
- ## Create New MariaDB User

  To create a new MariaDB user, type the following command:
  ```
  CREATE USER 'mehul'@'%' IDENTIFIED BY 'your-password';
  ```
  Once you create user1, check its status by entering:
  ```
  MariaDB [(none)]> SELECT User FROM mysql.user;
  +-------------+
  | User        |
  +-------------+
  | mehul       |
  | mariadb.sys |
  | mysql       |
  | root        |
  +-------------+
  4 rows in set (0.001 sec)
  ```
- ## Create database named Nginx
  To create a database, type the following command:
  ```
  MariaDB [(none)]> CREATE DATABASE Nginx;
  ```
  To show the list of databases, type the following command:
  ```
  SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | Nginx              |
  | information_schema |
  | mysql              |
  | performance_schema |
  +--------------------+
  4 rows in set (0.000 sec)
  ```
- ## Restoring the SQL file in database Nginx
  To restore the any file inside the database, type the following command:
  ```
  sudo mysql -u root -p <database_name> < <filename.sql>

  sudo mysql -u root -p Nginx < ngnix_access_log.sql;
  ```
