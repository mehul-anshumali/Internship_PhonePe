```
MariaDB [(none)]> create database test;
Query OK, 1 row affected (0.000 sec)

master side 

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)


```

```
master
MariaDB [(none)]> create database test1;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test1              |
+--------------------+
4 rows in set (0.000 sec)

slave 
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
| test1              |
+--------------------+
5 rows in set (0.000 sec)

```
## Master Master
```
master
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test1              |
+--------------------+
4 rows in set (0.000 sec)

MariaDB [(none)]> create database master-side;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '-side' at line 1
MariaDB [(none)]> create database masterside;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| master1side        |
| masterside         |
| mysql              |
| performance_schema |
| test1              |
+--------------------+
6 rows in set (0.000 sec)

MariaDB [(none)]> 


master1
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
| test1              |
+--------------------+
5 rows in set (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| masterside         |
| mysql              |
| performance_schema |
| test               |
| test1              |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> create database master1side;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> 

```


```VM1
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password: 
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 2     |
+--------------------+-------+

VM2
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password: 
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 2     |
+--------------------+-------+

after adding vm3 node
VM1
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password: 
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
VM2
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password: 
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
VM3
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
Enter password: 
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size | 3     |
+--------------------+-------+
```
## Backing Up and Upgrade

```
mariabackup --backup \
      --user=root \
      --target-dir=/home/mehul/backup/
```
The backup must be prepared:
```
mariabackup --prepare \
     --target-dir=/home/mehul/backup/
```

Stop the server process using the systemctl command:
```
sudo systemctl stop mariadb
```
Uninstall all of the MariaDB Community Server packages.
```
sudo apt remove "mariadb-*"
```
Uninstall the Galera package as well.
```
sudo apt remove galera-4
```
```
sudo apt remove galera
```
Before proceeding, verify that all MariaDB Community Server packages are uninstalled. The following command should not return any results:
```
apt list --installed | grep -i -E "mariadb|galera"
```
Gives some warning ignore*

### Install the New Version
Configure the APT package repository.
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
After this, it will give some error like,
```
[error] The following package is needed by the script, but not installed:
            apt-transport-https
        Please install and rerun the script.
```
To resolve this issue 
```
sudo apt-get install -f apt-transport-https
```
Again run 
```
sudo ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.5"
```

```
sudo apt update && sudo apt upgrade

```
Install MariaDB Community Server and package dependencies:
```
sudo apt install mariadb-server mariadb-backup
```
Upgrading the Data Directory
```
sudo mariadb-upgrade
```
Testing
```
sudo mariadb
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
