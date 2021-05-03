# Setup collectd to monitor various metrics for operating system and one of the following datastores ES/RMQ/AS.
- ## Setup Collectd
  - ### Install Collectd Service
    ```
    $ sudo apt-get install collectd
    ```
  - ### Install Collectd-Web and Dependencies
    ```
    $ sudo apt-get install git
    $ sudo apt-get install librrds-perl libjson-perl libhtml-parser-perl
    ```
  - ### Import Collectd-Web Git Repository and Modify Standalone Python Server
    ```
    $ cd /usr/local/
    $ git clone https://github.com/httpdss/collectd-web.git
    $ cd collectd-web/
    $ ls
    $ chmod +x cgi-bin/graphdefs.cgi
    ```
    - #### In order to access Collectd-web interface from a remote browser, you need to edit the runserver.py script and change the ```127.0.1.1``` IP Address to ```0.0.0.0```, in order to bind on all network interfaces IP Addresses.

      ```
      $ sudo nano runserver.py
      ```
  - ### Run Python CGI Standalone Server and Browse Collectd-web Interface
    ```
    $ sudo python runserver.py &
    ```
    - If it gives error like ``` /usr/bin/env: ‘python’: No such file or directory ``` then perform the below steps:- 
      ```
      $ cd /usr/bin
      $ sudo mv python python.bak
      $ sudo ln -s /usr/bin/python2.7 /usr/bin/python
      ```
      Again run the server by ```sudo python runserver.py &```.
      - If again it gives error like ```install the package Can't locate CGI.pm in @INC (you may need to install the CGI module)...```. Install the following perl module.
        ```
        $ sudo apt-get install libcgi-session-perl
        ```
  - #### Goto web browser type your ip with port 8888 to see the collectd web interface. ```http://ip:8888/```

- ## Setup RMQ with collectd 
  - ### Clone below repository and follow the steps:
    ```
    $ git clone https://github.com/signalfx/collectd-rabbitmq.git /opt/collectd-rabbitmq
    ```
  - ### Perform below steps in ```/etc/collectd/collectd.conf``` file.
    ```
    $ sudo nano /etc/collectd/collectd.conf
    ```
    - Uncomment the line 
      ```
      LoadPlugin python
      ```
    - In the ```<Plugin python>``` add the below lines:
      ```
      <Plugin python>
        ModulePath "/opt/collectd-rabbitmq"
        Import rabbitmq
        <Module rabbitmq>
          Username "your-username" 
          Password "your-password"
          Host "your-ip"
          Port "15672"
          CollectChannels false
          CollectConnections false
          CollectExchanges true
          CollectNodes true
          CollectQueues true
          VerbosityLevel "trace"
        </Module>
      </Plugin>
      ```

      - #### ```your-username``` and ```your-password``` all these will be your RabbitMQ management plugin credentials.
      ```
      The following boolean configuration options may be added to enable collection of specific statistics:

      CollectChannels - enables collection of channel statistics
      CollectConnections - enables collection of connection statistics
      CollectExchanges - enables collection of exchange statistics
      CollectNodes - enables collection of node statistics
      CollectQueues - enables collection of queue statistics
      ```
  - #### Go to collecd web interface there you will see the RabbitMQ metrics.
