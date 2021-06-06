# Week 12 Tasks List
```
Assignment for this week will be a complete app deployment using Mesos - Marathon 
```
Overall deployment and setup will look somewhat like this:

![image](https://user-images.githubusercontent.com/44754882/120912881-90c05680-c6b0-11eb-939e-7dd2df8dc41d.png)

- Create a Docker container running a python webserver, that listens on port 80 and returns the string "Hello world" for any requests.
- Create three VMs and setup the following:
  - Mesos master, Marathon, and Zookeeper on VM1
  - Mesos slave and Docker on VM2
  - Traefik on VM3
- Configure Traefik to get its data from Marathon.
- Deploy the docker container that you created in #1 to run as a Marathon app and it should be reachable using the Traefik.
- Setup VM4, install Nginx on it. Create a self-signed SSL Certificate and set up a proxy using Nginx which listens on port 443 with SSL enabled and forwards the requests to Traefik.
```
P.S: All the 4 VMs will be connected to using BGP and will talk to each other using their loopback ips. This is how VMs will be connected
```
![image](https://user-images.githubusercontent.com/44754882/120912954-19d78d80-c6b1-11eb-882c-a7e027457ead.png)

