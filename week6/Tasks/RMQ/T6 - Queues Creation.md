# Create 2 queues (DATA, DATA_SIDELINE) on the above created vhost.
- To create queue use ```rabbitmqadmin``` utility:

  - Create ```DATA``` queue: 

   ```
   $ ./rabbitmqadmin -u testuser -p testpassword --vhost testvhost declare queue name=DATA durable=true
   ```
  - Create ```DATA_SIDELINE``` queue:
    
    ```
    $ ./rabbitmqadmin -u testuser -p testpassword --vhost testvhost declare queue name=DATA_SIDELINE durable=true
    ```
  - List queues:
    ```
    $ ./rabbitmqadmin -u testuser -p testpassword list queues
    ```
- ## Setup HA-Policy.
  - Setup ha policy named ```ha-all``` which all queues on the RabbitMQ cluster will be mirroring to all nodes on the cluster.
  
    ```
    $ sudo rabbitmqctl set_policy -p testvhost ha-all ".*" ‘{"ha-mode":"all"}'
    ```
 
