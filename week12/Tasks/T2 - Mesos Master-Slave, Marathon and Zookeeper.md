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


