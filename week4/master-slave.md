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
