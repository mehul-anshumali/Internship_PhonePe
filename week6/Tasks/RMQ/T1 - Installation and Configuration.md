# Install and configure 1 node RMQ cluster version 3.7.9.
- ## Install Erlang version between 19.3 - 21.x
  - RabbitMQ requires Erlang to be installed first before it can run.
  - Perform below steps to install Erlang.(Installing v21)
    - Add the Erlang key:
      ```
      $ wget https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
      $ sudo apt-key add erlang_solutions.asc
      ```
    - Add the below repository link in ```/etc/apt/sources.list``` file.
      ```
      deb https://packages.erlang-solutions.com/ubuntu bionic contrib
      ```
    - Create a file ```/etc/apt/preferences.d/erlang``` and add the below contents:
    
      ```
      $ sudo nano /etc/apt/preferences.d/erlang
      ```
      ```
      Package: erlang* esl-erlang
      Pin: version 1:21.3*
      Pin-Priority: 501
      ```
    - Install Erlang:
      ```
      $ sudo apt-get update
      $ sudo apt-get install esl-erlang
      $ sudo ln -s /usr/lib/erlang/bin/erl /usr/local/bin/erl
      ```
- ## Install RMQ 3.7.9
  - Add below repo link in ```/etc/apt/sources.list.d/rabbitmq.list```.
    ```
    deb https://packagecloud.io/rabbitmq/rabbitmq-server/ubuntu/ bionic main
    deb-src https://packagecloud.io/rabbitmq/rabbitmq-server/ubuntu/ bionic main
    ```
  - Add the key
    ```
    $ sudo apt-key adv --keyserver "keyserver.ubuntu.com" --recv-keys "F6609E60DC62814E"
    ```
  - Install extra erlang packages:
    ```
    $ sudo apt-get update -y

    $ sudo apt-get install -y erlang-base \
                            erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                            erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                            erlang-runtime-tools erlang-snmp erlang-ssl \
                            erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl
    ```
  - Install RMQ
    ```
    $ sudo apt-get install rabbitmq-server=3.7.9-1 -y
    ```
- ## Configuration
  - Activate management plugin
    ```
    $ sudo rabbitmq-plugins enable rabbitmq_management
    ```
  - Add User - ```mehul``` and Password - ```mehul``` and giving permissions.
    ```
    $ sudo rabbitmqctl add_user mehul mehul
    $ sudo rabbitmqctl set_user_tags mehul administrator
    $ sudo rabbitmqctl set_permissions -p / mehul ".*" ".*" ".*"
    ```
  - Delete ```guest``` user.
    ```
    $ sudo rabbitmqctl delete_user guest
    ```
    
  - ### Go to browser give ```http://your-ip:15672/``` can able to see the RabbitMQ management UI.    
