# L3 + GRE Tunnel
- Create L3 connectivity between all 3 Hosts, Each host will form BGP with its corresponding router and advertise its own loopback ip
  ```
  Host 1: 10.10.1.1/32
  Host 2: 10.10.1.2/32
  Host 3: 10.10.1.3/32
  ```
![image](https://user-images.githubusercontent.com/44754882/118077605-0dbe2000-b3d2-11eb-9e23-1a6280768d8f.png)
<hr>

- ## VM's configuration:
    Host | Interface | IP/mask | Adapter No. - Name
    :--: | :--: | :--: | :--:
    R4 | `swp1`<br> `swp2` <br> `swp3` | `172.10.0.1/30` <br> `172.10.0.5/30` <br> `172.10.0.9/30` | `Adapter 2 - intnet-1`, <br> `Adapter 3 - intnet-2`, <br> `Adapter 4 - intnet-3`
    R1 | `swp1` <br> `swp2` | `172.10.0.2/30` <br> `172.10.0.13/30` | `Adapter 2 - intnet-1`, <br> `Adapter 3 - h1`
    R2 | `swp1` <br> `swp2` | `172.10.0.6/30` <br> `172.10.0.17/30` | `Adapter 2 - intnet-2`, <br> `Adapter 3 - h2`
    R3 | `swp1` <br> `swp2` | `172.10.0.10/30` <br> `172.10.0.21/30` | `Adapter 2 - intnet-3`, <br> `Adapter 3 - h3`   
    H1 | `enp0s8` <br> `enp0s9` | `10.10.1.1/32` <br> `172.10.0.14/30` | `Adapter 2 - intnet`, <br> `Adapter 3 - h1`
    H2 | `enp0s8` <br> `enp0s9` | `10.10.1.2/32` <br> `172.10.0.18/30` | `Adapter 2 - intnet`, <br> `Adapter 3 - h2`
    H3 | `enp0s8` <br> `enp0s9` | `10.10.1.3/32` <br> `172.10.0.22/30` | `Adapter 2 - intnet`, <br> `Adapter 3 - h3`
    
- ## HOST 1, 2, and 3 with FRR:
  - Installing FRR: 
  ```bash
  $ sudo curl -s https://deb.frrouting.org/frr/keys.asc | sudo apt-key add -
  $ FRRVER="frr-stable"
  $ sudo echo deb https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | sudo tee -a /etc/apt/sources.list.d/frr.list
  $ sudo apt update && sudo apt install frr frr-pythontools
  ```
  - Enable BGP:
    - Edit the `/etc/frr/daemons` file:
      ```
      bgpd=yes
      ```
  - Restart the FRR.

- ## L3 Connectivity:

  - ### On `R1`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp2 ip address 172.10.0.13/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp neighbor 172.10.0.14 remote-as 1
    $ net del bgp ipv4 unicast network 172.10.0.0/30
    $ net add bgp redistribute connected
    $ net commit
    ```
  - ### On `R2`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp2 ip address 172.10.0.17/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp neighbor 172.10.0.18 remote-as 1
    $ net del bgp ipv4 unicast network 172.10.0.4/30
    $ net add bgp redistribute connected
    $ net commit
    ```
  - ### On `R3`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp2 ip address 172.10.0.21/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp neighbor 172.10.0.22 remote-as 1
    $ net del bgp ipv4 unicast network 172.10.0.8/30
    $ net add bgp redistribute connected
    $ net commit
    ```
  - ### On `H1`:
    ```
    $ sudo vtysh
    ```
    ```
    H1# configure terminal 
    H1(config)# router bgp 1
    H1(config-router)# neighbor 172.10.0.13 remote-as 1
    H1(config-router)# address-family ipv4 unicast 
    H1(config-router-af)# network 10.10.1.1/32
    H1(config-router-af)# end
    ```
  - ### On `H2`:
    ```
    $ sudo vtysh
    ```
    ```
    H2# configure terminal 
    H2(config)# router bgp 2
    H2(config-router)# neighbor 172.10.0.17 remote-as 2
    H2(config-router)# address-family ipv4 unicast
    H2(config-router)# network 10.10.1.2/32
    H2(config-router)# end
    ```
  - ### On `H3`:
    ```
    $ sudo vtysh
    ```
    ```
    H3# configure terminal 
    H3(config)# router bgp 3
    H3(config-router)# neighbor 172.10.0.21 remote-as 3
    H3(config-router)# address-family ipv4 unicast
    H3(config-router)# network 10.10.1.3/32
    H3(config-router)# end
    ```
  - ### Testing:
    - Check the `BGP` summary:
      ```bash
      H1# show bgp summary
      ```
    - Check the routes:
      ```bash
      H1# show ip route 
      ```
    - #### Ping and check the connectivity between the `H1`, `H2`, and `H3`.
    
- ## GRE Tunnel:
  - Enable the IP Forwarding:
    - Edit the file ```/etc/sysctl.conf```
      ```
      net.ipv4.ip_forward=1
      ```
    - Save and ```sudo sysctl -p```
  - On H1:
    ```bash
    sudo ip tunnel add gre1 mode gre local 10.10.1.1 remote 10.10.1.3 ttl 255
    sudo ip addr add 192.168.100.1 dev gre1
    sudo ip link set gre1 up
    ```
  - On H3: 
    ```bash
    sudo ip tunnel add gre1 mode gre local 10.10.1.3 remote 10.10.1.1 ttl 255
    sudo ip addr add 192.168.100.2 dev gre1
    sudo ip link set gre1 up
    ```
 - **Testing**:
   ```Ping between 192.168.100.1 and 100.2```
   
