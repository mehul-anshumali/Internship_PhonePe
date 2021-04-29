# Setup collectd to monitor various metrics for operating system and one of the following datastores ES/RMQ/AS.
- ## Install Collectd Service
  ```
  $ sudo apt-get install collectd
  ```
- ## Install Collectd-Web and Dependencies
  ```
  $ sudo apt-get install git
  $ sudo apt-get install librrds-perl libjson-perl libhtml-parser-perl
  ```
- ## Import Collectd-Web Git Repository and Modify Standalone Python Server
  ```
  $ cd /usr/local/
  $ git clone https://github.com/httpdss/collectd-web.git
  $ cd collectd-web/
  $ ls
  $ chmod +x cgi-bin/graphdefs.cgi
  ```
  - ### In order to access Collectd-web interface from a remote browser, you need to edit the runserver.py script and change the ```127.0.1.1``` IP Address to ```0.0.0.0```, in order to bind on all network interfaces IP Addresses.
  
    ```
    $ sudo nano runserver.py
    ```
- ## Run Python CGI Standalone Server and Browse Collectd-web Interface
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
