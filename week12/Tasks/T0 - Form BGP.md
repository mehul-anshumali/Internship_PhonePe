# BGP formation between the VM's:

![image](https://user-images.githubusercontent.com/44754882/120913005-789d0700-c6b1-11eb-8cbb-1c768690785f.png)

- ## VM's configuration:
    Host | Interface | IP/mask | Adapter No. - Name
    :--: | :--: | :--: | :--:
    R1 | `enp0s3`<br> `enp0s8` <br> `enp0s9` <br> `enp0s10` <br> `lo` | `172.10.0.1/30` <br> `172.10.0.5/30` <br> `172.10.0.9/30` <br> `172.10.0.13/30` <br> `10.10.1.10/32` | `Adapter 1 - intnet-1` <br> `Adapter 2 - intnet-2` <br> `Adapter 3 - intnet-3` <br> `Adapter 4 - intnet-4` <br> `-`
    VM1 | `enp0s8` <br> `lo` | `172.10.0.2/30` <br> `10.10.1.11/32` | `Adapter 2 - intnet-1` <br> `-`
    VM2 | `enp0s8` <br> `lo` | `172.10.0.6/30` <br> `10.10.1.12/32` | `Adapter 2 - intnet-2` <br> `-`
    VM3 | `enp0s8` <br> `lo` | `172.10.0.10/30` <br> `10.10.1.13/32` | `Adapter 2 - intnet-3` <br> `-`
    VM4 | `enp0s8` <br> `lo` | `172.10.0.14/30` <br> `10.10.1.14/32` | `Adapter 2 - intnet-4` <br> `-`
    
- ## On `R1`:
  ```bash
  $ sudo vtysh
  ```
  ```vtysh
  R1# configure terminal 
  R1(config)# ip prefix-list ROUTE permit any
  R1(config)# router bgp 10
  R1(config-router)# neighbor 172.10.0.2 remote-as 1
  R1(config-router)# neighbor 172.10.0.6 remote-as 2
  R1(config-router)# neighbor 172.10.0.10 remote-as 3
  R1(config-router)# neighbor 172.10.0.14 remote-as 4
  R1(config-router)# address-family ipv4 unicast 
  R1(config-router-af)# network 10.10.1.10/32
  R1(config-router-af)# redistribute connected
  R1(config-router-af)# neighbor 172.10.0.2 prefix-list ROUTE in
  R1(config-router-af)# neighbor 172.10.0.2 prefix-list ROUTE out
  R1(config-router-af)# neighbor 172.10.0.6 prefix-list ROUTE in
  R1(config-router-af)# neighbor 172.10.0.6 prefix-list ROUTE out
  R1(config-router-af)# neighbor 172.10.0.10 prefix-list ROUTE in
  R1(config-router-af)# neighbor 172.10.0.10 prefix-list ROUTE out
  R1(config-router-af)# neighbor 172.10.0.14 prefix-list ROUTE in
  R1(config-router-af)# neighbor 172.10.0.14 prefix-list ROUTE out
  R1(config-router-af)# end
  ```
- ## On `VM1`:
  ```bash
  $ sudo vtysh
  ```
  ```vtysh
  VM1# configure terminal 
  VM1(config)# ip prefix-list ROUTE permit any
  VM1(config)# router bgp 1
  VM1(config-router)# neighbor 172.10.0.1 remote-as 10
  VM1(config-router)# address-family ipv4 unicast 
  VM1(config-router-af)# network 10.10.1.11/32
  VM1(config-router-af)# neighbor 172.10.0.1 prefix-list ROUTE in
  VM1(config-router-af)# neighbor 172.10.0.1 prefix-list ROUTE out
  VM1(config-router-af)# end
  ```
- ## On `VM2`:
  ```bash
  $ sudo vtysh
  ```
  ```vtysh
  VM2# configure terminal 
  VM2(config)# ip prefix-list ROUTE permit any
  VM2(config)# router bgp 2
  VM2(config-router)# neighbor 172.10.0.5 remote-as 10
  VM2(config-router)# address-family ipv4 unicast 
  VM2(config-router-af)# network 10.10.1.12/32
  VM2(config-router-af)# neighbor 172.10.0.5 prefix-list ROUTE in
  VM2(config-router-af)# neighbor 172.10.0.5 prefix-list ROUTE out
  VM2(config-router-af)# end
  ```
- ## On `VM3`:
  ```bash
  $ sudo vtysh
  ```
  ```vtysh
  VM3# configure terminal 
  VM3(config)# ip prefix-list ROUTE permit any
  VM3(config)# router bgp 3
  VM3(config-router)# neighbor 172.10.0.9 remote-as 10
  VM3(config-router)# address-family ipv4 unicast 
  VM3(config-router-af)# network 10.10.1.13/32
  VM3(config-router-af)# neighbor 172.10.0.9 prefix-list ROUTE in
  VM3(config-router-af)# neighbor 172.10.0.9 prefix-list ROUTE out
  VM3(config-router-af)# end
  ```
- ## On `VM4`:
  ```bash
  $ sudo vtysh
  ```
  ```vtysh
  VM4# configure terminal 
  VM4(config)# ip prefix-list ROUTE permit any
  VM4(config)# router bgp 4
  VM4(config-router)# neighbor 172.10.0.13 remote-as 10
  VM4(config-router)# address-family ipv4 unicast 
  VM4(config-router-af)# network 10.10.1.14/32
  VM4(config-router-af)# neighbor 172.10.0.13 prefix-list ROUTE in
  VM4(config-router-af)# neighbor 172.10.0.13 prefix-list ROUTE out
  VM4(config-router-af)# end
  ```
    
    
