# Create three VMs and setup the following,
- Mesos master, Marathon, and Zookeeper on VM1
- Mesos slave and Docker on VM2
- Traefik on VM3
<hr>

- ### Install `java` dependencies:
  ```bash
  sudo apt-get update
  sudo apt install openjdk-16-jre-headless -y 
  sudo apt install openjdk-11-jre-headless -y 

  ```
- ## Mesos master, Marathon, and Zookeeper on VM1:
  - ### Install Mesos: 
    - Install dependencies: 
      ```bash
      sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping
      sudo apt-get install libcurl4-openssl-dev
      ```
    - Install the deb package:
      ```bash
      sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb
      ```
      **if find an error for `libevent-dev` package, then:**
      ```bash
      sudo apt-get --fix-broken install
      ```
  - ### Configuration for `mesos-master`:
    - Add `1` to the quorom file:
      ```bash
      sudo nano /etc/mesos-master/quorum
      ```
    - Add IP and hostname:
      ```bash
      sudo vim /etc/mesos-master/ip
      cp /etc/mesos-master/ip /etc/mesos-master/hostname
      ```
    - Make sure the mesos-slave doesn't start on boot:
      ```
      echo manual | sudo tee /etc/init.d/mesos-slave.override
      ```
  - ### Install Marathon:
    - Add repo key: 
      ```bash
      sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
      DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
      CODENAME=xenial
      ```
    - Add marathon repository:
      ```
      echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | sudo tee /etc/apt/sources.list.d/mesosphere.list
      sudo apt-get -y update
      ```
    - Install marathon:
      ```
      sudo apt-get install marathon
      ```
<<<<<<< HEAD
  - ### Install Zookeeper:
    ```
    sudo apt-get install zookeeper
    ```
  - ### Configuration on `mesos-master` server:
    - Open the file and the `master-ip`:
      ```
      sudo nano /etc/mesos/zk
      ```
      ```
      zk://192.168.67.48:2181/mesos
      ```
    - Enter an unique id `1-255` for each `mesos-master`, in our case - `1` in myid file:
      ```
      sudo vim /etc/zookeeper/conf/myid
      ```
      ```
      1
      ```
    - Open the zookeeper configuration file and add the master's ip:
      ```
      sudo nano /etc/zookeeper/conf/zoo.cfg
      ```
      ```
      server.1=192.168.67.48:2888:3888
      ```
    - Open the quorum configuration file and `1` to it:
      ```
      sudo nano /etc/mesos-master/quorum
      ```
      ```
      1
      ```
    - Configure the Hostname and IP Address:
      ```
      sudo nano /etc/mesos-master/ip
      ```
      - Add `master-ip`.
      ```
      sudo cp /etc/mesos-master/ip /etc/mesos-master/hostname
      ```
    - Enter required configuration lines:
      ```
      sudo nano /etc/default/marathon 
      ```
      ```
      MARATHON_MASTER="zk://192.168.67.48:2181/mesos"
      MARATHON_ZK="zk://192.168.67.48:2181/marathon"
      MARATHON_HOSTNAME="192.168.67.48"
      ```
    - Make sure the `mesos-slave` doesn't start on boot:
      ```
      echo manual | sudo tee /etc/init.d/mesos-slave.override
      ```
    - Start `zookeeper` service:
      ```
      sudo cd /usr/share/zookeeper/bin
      sudo ./zkServer.sh status
      sudo ./zkServer.sh start
      ```
    - Start `mesos-master` service:
      ```
      sudo service mesos-master restart
      ```
    - `Marathon` - change the java to version 11
      ```
      sudo update-alternatives --config java       #select java11
      ```
      ```
      sudo service marathon restart
      ```
  - #### Verify the setup by accessing both `mesos-master's` & `marathon's` dashboard.
    - `mesos-master`: 192.168.67.48:5050
    - `marathon`: 192.168.67.48:8080
- ## Mesos slave and Docker on VM2:
  - ### Install Mesos: 
    - Install dependencies: 
      ```bash
      sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping
      sudo apt-get install libcurl4-openssl-dev
      ```
    - Install the deb package:
      ```bash
      sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb
      ```
      **if find an error for `libevent-dev` package, then:**
      ```bash
      sudo apt-get --fix-broken install
      ```
  - ### Configuration on `mesos-slave` server:
    - Open the file and the `master-ip`:
      ```
      sudo nano /etc/mesos/zk
      ```
      ```
      zk://192.168.67.48:2181/mesos
      ```
    - Configure the Hostname and IP Address: #enter slave ip.
      ```
      sudo nano /etc/mesos-slave/ip
      ```
      - Add `slave-ip`.
      ```
      sudo cp /etc/mesos-master/ip /etc/mesos-slave/hostname
      ```
    - Make sure the `mesos-master` doesn't start on boot:
      ```
      echo manual | sudo tee /etc/init/mesos-master.override
      ```
    - Restart `mesos-slave` service:
      ```
      sudo service mesos-slave restart
      ```
- ## Traefik on VM3:
  - ### Installing **traefik** on `VM3` requires **docker**:
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    $ echo \
      "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    $ sudo apt-get update
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```
    - Verify that Docker Engine is installed correctly by running the hello-world image.
      ```
      $ sudo docker run hello-world
      ```
  - ### Configuration:
    - #### Install apache-utils for using using _letsencrypt_ for basic authentication before accessing **traefik dashboard**, use _htpasswd_ utility to generate authentication details.
      ```bash
      $ sudo apt-get install -y apache2-utils
      $ htpasswd -nb <username> <password>
      # copy the encrypted username:password
      ```
    - Add the `toml` configuration for **traefik** to make it available through ports `80` & `433`, and configure `marathon` as **provider** - [traefik.toml](https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week12/Tasks/Traefik/traefik.toml).
    - Use the _encrypted authentication details_ generated before and create [traefik_secure.toml](https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week12/Tasks/Traefik/traefik_secure.toml) file.
    - Create a network interface for docker named **web** to be used by traefik container,
      ```
      sudo docker network create web
      ```
    - Create a file named `acme.json`, and assign `600` permissions, once this json file moves to docker container the ownership will get changed to **root** automatically.
      ```
      touch acme.json
      chmod 600 acme.json
      ```
    - Create a `traefik` container using all these configurations,
      ```
      sudo docker run -d \
       -v /var/run/docker.sock:/var/run/docker.sock \
       -v $PWD/traefik.toml:/traefik.toml \
       -v $PWD/traefik_secure.toml:/traefik_secure.toml \
       -v $PWD/acme.json:/acme.json \
       -p 80:80 \
       -p 443:443 \
       --network web \
       --name traefik \
        traefik:v2.4
      ```

  - Check docker **processes** to verify that container is running usinf `docker ps`, and if running successfully, verify the setup by accessing `<BridgeIP>:80` or `<BridgeIP>:443` for checking the traefik **dashboard**.


