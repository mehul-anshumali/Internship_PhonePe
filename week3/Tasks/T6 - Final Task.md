# Given Topoly Implementation
```
Establish BGP Sessions between below pairs:
    1. vm-1 <-> vm-router
    2. vm-2 <-> vm-router
    3. vm-3 <-> vm-router

Apply Bgp filters as follows
    1. vm-router orginates and sends default route to vm-1 , vm-2 and vm-3
    2. Each of the vms ( vm1, 2, 3 ) will accept only default route from its bgp peer ( vm-router) 
       and advertise their own loopback(IP on its lo interface ) to vm-router
    3. vm-router to accept /32 IPs that belong to subnet (10.1.1.0/24) and reject all other routes

Test case:
    1. On vm1, ping 10.1.1.3 and 10.1.4 should work
    2. On vm2, ping 10.1.1.2 and 10.1.1.4 should work
    3. On vm3, ping 10.1.1.2 and 10.1.1.3 should work
```
<hr>

- ### Configuration on VM1:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname ubuntu
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 200
   neighbor 172.10.0.1 remote-as 100
   !
   address-family ipv4 unicast
    network 10.1.1.2/32
    neighbor 172.10.0.1 prefix-list ROUTE0 in
    neighbor 172.10.0.1 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE0 seq 5 permit 0.0.0.0/0
  ip prefix-list ROUTE seq 5 permit 10.1.1.0/24 ge 32 le 32
  !
  line vty
  !
  end
  ```
- ### Configuration on VM - Router: 
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname ubuntu
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 100
   neighbor 172.10.0.2 remote-as 200
   neighbor 172.10.0.6 remote-as 300
   neighbor 172.10.0.10 remote-as 400
   !
   address-family ipv4 unicast
    network 10.1.1.1/32
    neighbor 172.10.0.2 default-originate
    neighbor 172.10.0.2 prefix-list ROUTE in
    neighbor 172.10.0.2 prefix-list ROUTE0 out
    neighbor 172.10.0.6 default-originate
    neighbor 172.10.0.6 prefix-list ROUTE in
    neighbor 172.10.0.6 prefix-list ROUTE0 out
    neighbor 172.10.0.10 default-originate
    neighbor 172.10.0.10 prefix-list ROUTE in
    neighbor 172.10.0.10 prefix-list ROUTE0 out
   exit-address-family
  !
  ip prefix-list ROUTE seq 5 permit 10.1.1.0/24 ge 32 le 32
  ip prefix-list ROUTE0 seq 5 permit 0.0.0.0/0
  !
  line vty
  !
  end
  ```
- ### Configuration on VM2:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname ubuntu
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 300
   neighbor 172.10.0.5 remote-as 100
   !
   address-family ipv4 unicast
    network 10.1.1.3/32
    neighbor 172.10.0.5 prefix-list ROUTE0 in
    neighbor 172.10.0.5 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE0 seq 5 permit 0.0.0.0/0
  ip prefix-list ROUTE seq 5 permit 10.1.1.0/24 ge 32 le 32
  !
  line vty
  !
  end
  ```
- ### Configuration on VM3:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname ubuntu
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 400
   neighbor 172.10.0.9 remote-as 100
   !
   address-family ipv4 unicast
    network 10.1.1.4/32
    neighbor 172.10.0.9 prefix-list ROUTE0 in
    neighbor 172.10.0.9 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE0 seq 5 permit 0.0.0.0/0
  ip prefix-list ROUTE seq 5 permit 10.1.1.0/24 ge 32 le 32
  !
  line vty
  !
  end
  ```
