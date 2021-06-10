# Dynamic routing
Implement #2 and #3, with BGP as routing ( using software FRR )

**```Run the same tests as of #2 and #3```**
<hr>

- Configuration on VM1:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname vm2
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 100
   neighbor 192.168.10.2 remote-as 200
   !
   address-family ipv4 unicast
    network 192.168.1.0/24
    neighbor 192.168.10.2 prefix-list ROUTE in
    neighbor 192.168.10.2 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE seq 5 permit any
  !
  line vty
  !
  end
  ```

- Configuration on VM2:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname vm2
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 200
   neighbor 192.168.10.1 remote-as 100
   neighbor 192.168.10.4 remote-as 300
   !
   address-family ipv4 unicast
    neighbor 192.168.10.1 prefix-list ROUTE in
    neighbor 192.168.10.1 prefix-list ROUTE out
    neighbor 192.168.10.4 prefix-list ROUTE in
    neighbor 192.168.10.4 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE seq 5 permit any
  !
  line vty
  !
  end
  ```

- Configuration on VM3:
  ```
  Building configuration...

  Current configuration:
  !
  frr version 7.5.1
  frr defaults traditional
  hostname vm2
  no ipv6 forwarding
  service integrated-vtysh-config
  !
  router bgp 300
   neighbor 192.168.10.3 remote-as 200
   !
   address-family ipv4 unicast
    network 192.168.2.0/24
    neighbor 192.168.10.3 prefix-list ROUTE in
    neighbor 192.168.10.3 prefix-list ROUTE out
   exit-address-family
  !
  ip prefix-list ROUTE seq 5 permit any
  !
  line vty
  !
  end
  ```
