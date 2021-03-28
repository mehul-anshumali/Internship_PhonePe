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

