# NAT on router VM

- Create 3 VMs and connect them as #2

- Router VM (i.e VM2) will accept connections on its own IP and port 2222 and forward the packets to VM3 on port 22
example: 
```
VM1 connects to VM2 port 2222
VM2 forwards the traffic to VM3 port 22
```
**```Result, VM1 is connected to VM3`s port 22 ( via VM2`s port 2222)```**
<hr>

- Port Fowarding using iptables:
  - On VM2:
    ```
    $ sudo iptables -t nat -A PREROUTING -p tcp --dport 2222 -j DNAT --to-destination 192.168.1.10:22
    $ sudo iptables -A FORWARD -p tcp -d 192.168.3.1 --dport 22 -j ACCEPT
    ```
  - Make Persistent:
    ```
    $ sudo apt install iptables-persistent
    $ sudo nano /etc/iptables/rules.v4
    $ sudo iptables-save > /etc/iptables/rules.v4
    ```
