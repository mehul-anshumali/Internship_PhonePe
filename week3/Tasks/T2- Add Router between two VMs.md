# Create 3 VMs and establish connectivity between them
  ```
  VM1 <-> VM2
  VM3 <-> VM2
  VM1<->VM3 ( via VM2 as router )
  ```
<hr> 

- Install seperately three VMs or you can also clone the main VM to generate multiple VMs. 
  - While cloning make sure that you choose the ```Generate new MAC addresses for all network adapters``` in MAC Address Policy.

- If you're cloning and want to change the Hostname you can change it by using the following command:
  ```
  $ sudo hostnamectl set-hostname <host-name>
  $ sudo hostnamectl set-hostname vm1
  ```
  ```
  $ sudo nano /etc/hosts/
  ```
  - Replace the default hostname of cloned machine to your hostname in this file.

- Go to settings of each VM, under the network tab add new adapter by ```Enabling network adapter``` and change the Attached Network from ```NAT``` to ```Internal Network```,
  you can give any name such that two VMs are in different network and one VM will act as a Router. 
  
- To make it possible I am enabling 1 network adapter in VM1 i.e ```neta```, 2 network adapters in VM2 i.e ```neta``` and ```netb``` and 1 network adapter in VM3 i.e ```netb```.
- Login into your VM. Check which names are assigned to it by using ```ip a ``` command. 
- Head over to the ```/etc/netplan``` directory. You will find a YAML configuration file which you will use to configure the IP address.
  ```
  $ sudo nano /etc/netplan/00-installer-config.yaml
  ```
  - Assigned the ip's to adapters.
 - Next, save the file and run the netplan command below to save the changes.
   ```
   $ sudo netplan apply
   ```
- The .yaml for will look something like this. 
  - For VM1:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.1.1/24]  
    ```
  - For VM2:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.1.10/24]
        
    network:
    version: 2
    ethernets:
      enp0s9:
        dhcp4: false
        addresses: [192.168.2.10/24]
    ```
  - For VM3:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.2.1/24]  
    ```
- After assigning the we have to add the static routes in the .yaml file to make it persistent.
  - Edit your .yaml file in VM1:
    ```
    routes:
    - to: 192.168.2.0/24
      via: 192.168.1.10
    ```
  - Edit your .yaml file in VM3:
    ```
    routes:
    - to: 192.168.1.0/24
      via: 192.168.2.10
    ```
- Final configuration will look like this in .yaml file.
  - VM1:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.1.1/24]  
        routes:
        - to: 192.168.2.0/24
          via: 192.168.1.10
    ```
  - VM2:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.1.10/24]
        
    network:
    version: 2
    ethernets:
      enp0s9:
        dhcp4: false
        addresses: [192.168.2.10/24]- 
    ```
  - VM3:
    ```
    network:
    version: 2
    ethernets:
      enp0s8:
        dhcp4: false
        addresses: [192.168.2.1/24]  
        routes:
        - to: 192.168.1.0/24
          via: 192.168.2.10
    ```
- Now, try to ping the IPs in the alternative VMs.
  ```
  In VM1:
  $ ping 192.168.2.1
  
  In VM2:
  $ ping 192.168.1.1
  ```
  - These commands show the packets received or loss. If packet loss (preferebly 0% packet loss), is there then it confirms that these two VMs are communicating with each other.
