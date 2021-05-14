# VRF - Virtual Routing and Forwarding
- All 3 Hosts will form BGP with its corresponding Routers
- Host 1 and Host 2 will belong to VRF1
- Host 3 will belong to VRF 2
  ```
  Test case: ( Hosts within the same vrf will be able to ping each other )

  Host 1 will be able to ping the loopback IP of Host 2 and vice versa
  Host 3 will not be reachable from host 1 and host 2
  ```
- Move host 2 to VRF 2, and repeat the tests
<hr>

- ## Host 1 and Host 2 will belong to VRF1 & Host 3 will belong to VRF 2
  - ### On `R4`:
    - #### Create two VRF's i.e. `VRF1` & `VRF2`:
      ```nclu
      $ net add vrf VRF1 vrf-table auto 
      $ net add vrf VRF2 vrf-table auto
      $ net commit
      ```
    - #### Add interfaces to respective VRF's:
      - Adding HOST1 and HOST2 to same VRF. i.e `VRF1`:
        ```nclu
        $ net add interface swp1 vrf VRF1
        $ net add interface swp2 vrf VRF1
        $ net commit
        ```
      - Adding HOST3 in `VRF2`:
        ```nclu
        $ net add interface swp3 vrf VRF2
        $ net commit
        ```
    - Show VRF's list:
      ```nclu
      $ net show vrf list
      ```
    - #### Remove old BGP configuration:
      ```nclu
      $ net del bgp autonomous-system 4
      $ net commit
      ```
    - #### Add VRF BGP configuration:
      - `VRF1` BGP configuration:
        ```nclu
        $ net add bgp vrf VRF1 autonomous-system 4
        $ net add bgp vrf VRF1 neighbor 172.10.0.2 remote-as 1
        $ net add bgp vrf VRF1 neighbor 172.10.0.6 remote-as 2
        $ net add bgp vrf VRF1 ipv4 unicast network 10.10.1.14/32
        $ net commit
        ```
      - `VRF2` BGP configuration:
        ```nclu
        $ net add bgp vrf VRF2 autonomous-system 4
        $ net add bgp vrf VRF2 neighbor 172.10.0.10 remote-as 3
        $ net add bgp vrf VRF2 ipv4 unicast network 10.10.1.14/32
        $ net commit
        ```
    - ### Testing:
      - Now, try to ping the between the Hosts.
        - **`HOST1` & `HOST2` are able to ping each other but not `HOST3` and vice-versa.**

- ## Move host 2 to VRF 2
  - ## On `R4`:
    - ### Remove the Host2 interface i.e `swp2` from VRF1:
      ```nclu
      $ net del interface swp2 vrf VRF1
      $ net commit
      ```
    - ### Add the Host2 interface in VRF2:
      ```nclu
      $ net add interface swp2 vrf VRF2
      $ net commit
      ```
    - ### Remove the neighbor HOST2 from BGP VRF1 and add it to VRF2:
      ```nclu
      $ net del bgp vrf VRF1 neighbor 172.10.0.6 remote-as 2
      $ net commit
      
      $ net add bgp vrf VRF2 neighbor 172.10.0.6 remote-as 2
      $ net commit
      ```
    - ### Testing:
      - Now, try to ping the between the Hosts.
        - **`HOST1` is not able to ping `HOST2` & `HOST3` and vice-versa.**
