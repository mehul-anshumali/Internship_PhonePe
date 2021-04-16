# Create a vhost and a user with read-write permissions to the vhost.
- To create ```vhost``` we need rabbitmq utility called ```rabbitmqadmin```
  - Get ```rabbitmqadmin``` utility:
    ```
    $ curl -o rabbitmqadmin http://youri-ip:15672/cli/rabbitmqadmin
    ``` 
  - Ensure that executable bit is set:
    ```
    $ chmod +x rabbitmqadmin
    ```
  - Create vhost - ```testvhost```.
    ```
    $ ./rabbitmqadmin -u mehul -p mehul declare vhost name=testvhost
    ```
    where, ```-u mehul``` - management user and ```-p mehul``` - management password.
  
  - Create user - ```testuser``` with password - ```testpassword```.
    ```
    $ sudo rabbitmqctl add_user testuser testpassword
    ```
  - Adding ```testuser``` to ```testvhost``` with read-write permissions.
    ```
    $ sudo rabbitmqctl set_permissions testuser --vhost testvhost ".*" ".*" ".*"
    $ sudo rabbitmqctl set_user_tags testuser management
    ```
  - List users and vhosts:
    ```
    $ ./rabbitmqadmin -u mehul -p mehul list vhosts
    $ ./rabbitmqadmin -u mehul -p mehul list users
    ```
    
    
