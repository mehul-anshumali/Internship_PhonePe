# Add 2 more nodes to the cluster without restarting RMQ service on first one.
- ## Setup Hosts File
  - Go to ```/etc/hosts``` and add contents like below:
  
    ```
    $ sudo nano /etc/hosts
    ```
    ```
    192.168.1.11 ubuntu1
    192.168.1.12 ubuntu2
    192.168.1.13 ubuntu3
    ```
    ```ubuntu1, ubuntu2, ubuntu3``` are the hostnames of servers.

- ## Setup RabbitMQ Cluster
  - In order to setup the RabbitMQ cluster, we need to make sure the '.erlang.cookie' file is same on all nodes. This file is located at ```/var/lib/rabbitmq/.erlang.cookie```.
    
    - Copy the ```erlang.cookie``` of first server i.e. ```ubuntu1``` to other servers - ```ubuntu2``` and ```ubuntu3```.
      
      ```
      $ sudo scp /var/lib/rabbitmq/.erlang.cookie mehul@ubuntu2:/var/lib/rabbitmq/
      $ sudo scp /var/lib/rabbitmq/.erlang.cookie mehul@ubuntu3:/var/lib/rabbitmq/
      ```
  - Restart the RabbitMQ service and stop the app on other servers - ```ubuntu2``` and ```ubuntu3```.
    ```
    $ sudo systemctl restart rabbitmq-server
    $ sudo rabbitmqctl stop_app
    ```
  - Now let RabbitMQ server on both nodes join the cluster on ```ubuntu1```, then start the app.
    ```
    $ sudo rabbitmqctl join_cluster rabbit@ubuntu1
    $ sudo rabbitmqctl start_app
    ```
  - When it's complete, check the RabbitMQ cluster status.
    ```
    $ sudo rabbitmqctl cluster_status
    ```
    - The RabbitMQ Cluster has been created, with ubuntu1, ubuntu2, and ubuntu3 as members.
