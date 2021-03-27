# Take Physical backup from one node to a local or remote location and start a docker on it and compare the checksum of the table.
- ## BackUp
  - Logical backups consist of the SQL statements necessary to restore the data, such as CREATE DATABASE, CREATE TABLE and INSERT.
  - Physical backups are performed by copying the individual data files or directories.
  - **Physical BackUp**
    - Taking Physical Backup using ```mariabackup```.
      - First get the ```mariadb-backup``` package.
        ```
        sudo apt-get mariadb-backup
        ```
      - Take the full backup on the joiner node, type the following command:
        ```
        mariabackup --backup \
          --target-dir=/home/mehul/backup/
          --user=root \
        ```
        ```--backup```:- specifies that we are doing the backup
 
        ```--target-dir```:-specifies the target directory(backup directory)
