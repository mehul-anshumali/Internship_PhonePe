# Bridge connectivity or L2 connectivity
  Bridge connectivity or L2 connectivity
  ```
  Test for connectivity: two VMs should be able to ping each other
  ```
<hr>

- Install seperately two VMs or you can also clone the main VM to generate multiple VMs. 
  - While cloning make sure that you choose the ```Generate new MAC addresses for all network adapters``` in MAC Address Policy.

- After cloning, login into the system and if you want to change the Hostname you can change it by using the following command:
  ```
  $ sudo hostnamectl set-hostname <host-name>
  $ sudo hostnamectl set-hostname vm1
  ```
  ```
  $ sudo nano /etc/hosts/
  ```
  - Replace the default hostname of cloned machine to your hostname in this file.

- Go to settings of each VM, under the network tab add new adapter by ```Enabling network adapter``` and change the Attached Network from ```NAT``` to ```Internal Network```,
  you can give any name, I am giving ```"neta"``` and save it.

- These two VMs forms a new network named ```"neta"```.

- Now, switched on both the VMs and check its Ethernet adapter name by ```ip addr show```. This command will show the IP assigned to each Ethernet adapter.
  This ethernet adapter named as ```enp0s*```. Mine were ```enp0s3```, ```enp0s8```. 

- The ```enp0s3``` have some IP assigned to it i,e of ```10.0.0.*```. This means that this Ethernet Adapater is of default network Virtual Box has assigned i.e ```NAT``` network.

- So now we will assign the IP of ```neta``` network, ethernet adapted is ```enp0s8```.

- In your terminal, head over to the ```/etc/netplan``` directory. You will find a YAML configuration file which you will use to configure the IP address.
  ```
  $ sudo nano /etc/netplan/00-installer-config.yaml
  ```
  - Add the below commands to this .yaml file, and make sure that the indentation is correct.
  ```
  network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.1.1/24]
        gateway4: 192.168.1.254

  ```
 - Next, save the file and run the netplan command below to save the changes.
 ```
 $ sudo netplan apply
 ```
 - You can thereafter confirm the IP address of your network interface using the ```ip addr show``` command.
 - Repeat the steps for other VM alsoand changed the addresses from ```1.1``` to ```1.2```.
 - Now we have IP assigned to each VM. i.e 
   ``` 
   In VM1: 192.168.1.1
   In VM2: 192.168.1.2
   ```
   
 - Now, try to ping the IPs in the alternative VMs.
  ```
  In VM1:
  $ ping 192.168.1.2
  
  In VM2:
  $ ping 192.168.1.1
  ```
  - These commands show the packets received or loss. If packet loss (preferebly 0% packet loss), is there then it confirms that these two VMs are communicating with each other.
