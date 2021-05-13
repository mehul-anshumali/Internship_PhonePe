# EVPN / Vxlan
![image](https://user-images.githubusercontent.com/44754882/118077052-fdf20c00-b3d0-11eb-82de-39b42769c40f.png)

- ### VM's configuration:
    Host | Interface | IP/mask | Adapter No. - Name
    :--: | :--: | :--: | :--:
    R4 | `swp1`<br> `swp2` <br> `swp3` | `172.10.0.1/30` <br> `172.10.0.5/30` <br> `172.10.0.9/30` | `Adapter 2 - intnet-1`, <br> `Adapter 3 - intnet-2`, <br> `Adapter 4 - intnet-3`
    R1 | `swp1` <br> `lo` | `172.10.0.2/30` <br> `10.10.1.11/32` | `Adapter 2 - intnet-1`, <br> `Adapter 3 - h1`
    R2 | `swp1` <br> `lo` | `172.10.0.6/30` <br> `10.10.1.12/32` | `Adapter 2 - intnet-2`, <br> `Adapter 3 - h2`
    R3 | `swp1` <br> `lo` | `172.10.0.10/30` <br> `10.10.1.13/32` | `Adapter 2 - intnet-3`, <br> `Adapter 3 - h3`
    H1 | `enp0s8` | `10.3.1.1/24` <br> `Gateway: 10.3.1.11` | `Adapter 2 - h1`
    H2 | `enp0s8` | `10.3.1.2/24` <br> `Gateway: 10.3.1.11` | `Adapter 2 - h2`
    H3 | `enp0s8` | `10.3.1.3/24` <br> `Gateway: 10.3.1.11` | `Adapter 2 - h3`

- ### On `R4`:
  ```nclu
  $ net add bgp l2vpn evpn neighbor 172.10.0.2 activate
  $ net add bgp l2vpn evpn neighbor 172.10.0.6 activate
  $ net add bgp l2vpn evpn neighbor 172.10.0.10 activate
  $ net commit
  ```
- ### On `R1`:
  ```nclu
  $ net add loopback lo ip address 10.10.1.11/32
  $ net commit
  
  $ net add bridge bridge ports swp2
  $ net add interface swp2 bridge access 14
  $ net add vlan 100 ip address 10.3.1.11/24
  $ net commit

  $ net add vxlan vni-1014 vxlan id 1014
  $ net add vxlan vni-1014 bridge access 14
  $ net add vxlan vni-1014 vxlan local-tunnelip 10.10.1.11
  $ net add vxlan vni-1014 bridge learning off
  $ net add vxlan vni-1014 mtu 9152
  $ net commit

  $ net add bgp evpn neighbor 172.10.0.1 activate
  $ net add bgp evpn advertise-all-vni
  $ net commit
  ```
- ### On `R2`:
  ```nclu
  $ net add loopback lo ip address 10.10.1.12/32
  $ net commit
  
  $ net add bridge bridge ports swp2
  $ net add interface swp2 bridge access 14
  $ net add vlan 100 ip address 10.3.1.11/24
  $ net commit

  $ net add vxlan vni-1014 vxlan id 1014
  $ net add vxlan vni-1014 bridge access 14
  $ net add vxlan vni-1014 vxlan local-tunnelip 10.10.1.12
  $ net add vxlan vni-1014 bridge learning off
  $ net add vxlan vni-1014 mtu 9152
  $ net commit

  $ net add bgp evpn neighbor 172.10.0.5 activate
  $ net add bgp evpn advertise-all-vni
  $ net commit
  ```
- ### On `R3`:
  ```nclu
  $ net add loopback lo ip address 10.10.1.13/32
  $ net commit
  
  $ net add bridge bridge ports swp2
  $ net add interface swp2 bridge access 14
  $ net add vlan 100 ip address 10.3.1.11/24
  $ net commit

  $ net add vxlan vni-1014 vxlan id 1014
  $ net add vxlan vni-1014 bridge access 14
  $ net add vxlan vni-1014 vxlan local-tunnelip 10.10.1.13
  $ net add vxlan vni-1014 bridge learning off
  $ net add vxlan vni-1014 mtu 9152
  $ net commit

  $ net add bgp evpn neighbor 172.10.0.9 activate
  $ net add bgp evpn advertise-all-vni
  $ net commit
  ```
- ## Testing Commands:
  ```
  $ net show bridge vlan
  $ net show bgp evpn summary 
  $ net show bgp evpn vni 
  $ net show bgp evpn route 
  $ net show evpn mac vni 1014
  ```
- Now, try to ping the between the Hosts.
  ```bash
  Host1:
  $ ping 10.3.1.2
  $ ping 10.3.1.3
  ```
 




