# R1, R2, R3 will form BGP with R4.
![image](https://user-images.githubusercontent.com/44754882/118435456-a0293100-b6fc-11eb-9984-1fb7d47a42c9.png)

  - Change the hostname of Cumulus VX by using the command:
    ```nclu
    $ net add hostname R1
    $ net pending
    $ net commit
    ```
    **NOTE:** The command prompt in the terminal doesn’t reflect the new hostname until you either log out of the switch or start a new shell.
    - The `net pending` command helps you verify the changes before applying them.
    - The `net commit` command helps you push the changes to the configuration.
  - ### VM's configuration:
    Host | Interface | IP/mask | Adapter No. - Name
    :--: | :--: | :--: | :--:
    R4 | `swp1`<br> `swp2` <br> `swp3` | `172.10.0.1/30` <br> `172.10.0.5/30` <br> `172.10.0.9/30` | `Adapter 2 - intnet-1` <br> `Adapter 3 - intnet-2` <br> `Adapter 4 - intnet-3`
    R1 | `swp1` | `172.10.0.2/30` | `Adapter 2 - intnet-1`
    R2 | `swp1` | `172.10.0.6/30` | `Adapter 2 - intnet-2`
    R3 | `swp1` | `172.10.0.10/30` | `Adapter 2 - intnet-3`
    
  - ### On `R4`:
    - Assiging `IP's` to interfaces: 
    ```nclu
    $ net add interface swp1 ip address 172.10.0.1/30
    $ net add interface swp2 ip address 172.10.0.5/30
    $ net add interface swp3 ip address 172.10.0.9/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp autonomous-system 4
    $ net add bgp neighbor 172.10.0.2 remote-as 1
    $ net add bgp neighbor 172.10.0.6 remote-as 2
    $ net add bgp neighbor 172.10.0.10 remote-as 3
    $ net commit
    ```
  - ### On `R1`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp1 ip address 172.10.0.2/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp autonomous-system 1
    $ net add bgp neighbor 172.10.0.1 remote-as 4
    $ net add bgp ipv4 unicast network 172.10.0.0/30
    $ net commit
    ```
  - ### On `R2`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp1 ip address 172.10.0.6/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp autonomous-system 2
    $ net add bgp neighbor 172.10.0.5 remote-as 4
    $ net add bgp ipv4 unicast network 172.10.0.4/30
    $ net commit
    ```
  - ### On `R3`:
    - Assiging `IP's` to interface: 
    ```nclu
    $ net add interface swp1 ip address 172.10.0.10/30
    $ net commit
    ```
    - Forming `BGP`:
    ```nclu
    $ net add bgp autonomous-system 3
    $ net add bgp neighbor 172.10.0.9 remote-as 4
    $ net add bgp ipv4 unicast network 172.10.0.8/30
    $ net commit
    ```
  - ### Testing:
    - Check the `BGP` summary:
      ```nclu
      $ net show bgp summary
      ```
    - Check the routes:
      ```nclu
      $ net show route 
      ```
    - #### Ping and check the connectivity between the `R1`, `R2`, `R3`, and `R4`.
    
