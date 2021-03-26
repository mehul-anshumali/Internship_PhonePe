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
