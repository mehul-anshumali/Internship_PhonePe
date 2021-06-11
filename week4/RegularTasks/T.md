In this task, we have 2 parts:
# Tasks
1. Take a physical backup of one node and start a docker on it
2. Upgrade the Galera cluster version from 10.5.6 to 10.5.9

## Physical Backup & Docker
> physical backup using `mariabackup` sst method

* We are going to use `mariabackup manual sst` technique for creating a physical backup of one of our nodes, my preference is `node3`.

* First of all we need two nodes (one from the cluster `node3` and another is an standalone node which can be used to deploy mariadb as a `docker container`), these are known as
    * Donor Node : `node3` | 192.168.1.3
    * Joiner Node : standalone node - `docker-node` | 192.168.1.4

* Now, for storing the physical backup in `node3` and initiating the backup using `mariabackup`, we do
    ```bash
    $ sudo mkdir /home/mehul/pbackup
    $ sudo mariabackup --backup --galera-info --target-dir=/home/mehul/pbackup \
        --user mariabackup --password mypassword
    ```
* Stop the `mariadb` server and check the status
    ```bash
    $ sudo systemctl stop mariadb
    $ sudo systemctl status mariadb
    ```
    
* Now in Joiner node - `docker-node`, we create the directory and copy the backup from `node3` (donor) to `docker-node` (joiner) using rsync or scp
    * In `docker-node` :
        ```bash
        $ sudo mkdir /home/mehul/backup
        ```
    * In `node3` :
        ```bash
        $ rsync -av /home/mehul/pbackup/ mehul@192.168.1.4:/home/mehul/backup/
      ```
* We now have the work with `docker`, so install it and pull `mariadb v10.5.6` to create a container with the name `maria-dock-node`,
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install docker.io
    $ docker pull mariadb:10.5.6
    $ docker images                     
    
    #creating a container
    $ docker run --name maria-dock-node -d -e MYSQL_ROOT_PASSWORD=root mariadb:10.5.6
    $ docker ps -a                     
    ```


* Now we can login to the `mysql` shell in the docker container or open up a bash terminal, so for `mysql` shell,
    ```bash
    $ docker inspect maria-dock-node | grep IPAddress       #to get the IP of the docker to login remotely
    $ mysql -u root -p -h 172.17.0.2                     #172.17.0.2 was my output for my previous command
    ```
    and for bash,
    ```bash
    $ docker exec -it maria-dock-node bash
    ```

* Now we need to copy that backup from `/home/mehul/backup` from `docker-node` host to the docker container `maria-dock-node`,
    ```bash
    $ sudo docker cp /home/mehul/backup/ maria-dock-node:/home/backup/
    $ sudo docker exec -it maria-dock-node bash     
    $ ls /home/backup                           #list the files and compare with the host backup files to verify the copy operation
    ```
* In joiner node, we may have to remove any kind of existing file in our `datadir` i.e `/var/lib/mysql/`
    ```bash
    rm -Rf /var/lib/mysql/*
    ```
* In joiner node - `docker-node`, before restoring the backup, we need to prepare it
    ```bash
    mariabackup --prepare \
        --target-dir=/home/backup \
        --user mariabackup --password mypassword
    ```
* Now, we require to restore the backup so, in `maria-dock-node` we can use either `cp` command to just copy all files into `/var/lib/mysql` directory or use `mariabackup` with the option `--copy-back` / `--move-back`,
    ```bash
    mariabackup --copy-back --target-dir=/home/backup/
    ```

* Now verify all the contents of database by loging into the `mysql` shell inside docker container either by running
    ```bash
    mysql -u root -p
    ```
    from `maria-dock-node`'s bash or
    ```bash
    mysql -uroot -p -h 172.17.0.2
    ```
    from 'docker-node` i.e host's bash and check the databases, tables, and their checksum to ensure all the contents of database are successfully restored on a docker container.
