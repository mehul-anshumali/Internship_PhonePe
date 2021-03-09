# :rocket: General Questions Lists  :rocket:
### :round_pushpin: Find the processes running on a linux machine. 
The most common way to list processes currently running on your system is to use the ```ps``` command. Used without any options, the ps command displays only processes that are started from the current shell.
To get information about all processes running on the system, use ```ps -a```.\
To get get more clear idea about processes running on the system use a,u and x options with ps. This displays all processes running for all users on your system, along with useful information such as the username of the process′ owner, CPU loads, the starting time of the process, the command that initiated the process, etc.
```ps -aux```
```
a : Select all processes
u : Select all processes on a terminal, including those of other users
x : Select processes without controlling ttys
```
### :round_pushpin: Find the users currently logged in.
By using ```who``` command you can see the logged in user.
If you want to see the list of users currently logged in you have to give option ```a``` with ```who``` command: ```who -a```.
Others command are also available they are ```w```, ```users```.
### :round_pushpin: Find the uptime of the machine.
You can check system uptime by using command ```uptime```. It displays how long the system has been running.
### :round_pushpin: Find the RAM usage.
To display free memory size in MB (megabytes). You can use the ```free -h``` command. 
### :round_pushpin: Find the disk usage.
The ```df``` command shows the amount of disk space used and available on file systems. You can use ```h``` option with it check the disk usage in more understandable from ```df -h```.
### :round_pushpin: Find the inode usage.
The ```df -i``` command shows the usage and availability of inodes. You can use ```h``` option with it check the disk usage in more understandable from ```df -ih```.
### :round_pushpin: Find the ulimit of a user.
Limits are categorized as either soft or hard:
Soft limit – All users can change soft limits, up to max set by the hard limits. Pass the -S option to the ulimit.
Hard limit – Only root users allowed to change esource hard limits. Pass the -H option to the ulimit.
Command to view all soft and hard limits for the current user: 
```
ulimit -Sa ## Show soft limit ##
ulimit -Ha ## Show hard limit ##
```
### :round_pushpin: Find the ulimit of a process.
You can check the ulimits for any process ID by reading ```/proc/<pid>/limits```, where <pid> is replaced by the numeric pid of the process.
  ```
  cat /proc/<pid>/limits
  ```

### :round_pushpin: Find the file description used by a process.

### :round_pushpin: Find the top 5 process by memory usage.
### :round_pushpin: Find the top 5 process by CPU usage.
### :round_pushpin: Find the top 5 process by network usage.
### :round_pushpin: Find the top 5 usage by disk iops usage.
### :round_pushpin: Find the network traffic and bandwidth usage of the machine.
### :round_pushpin: Given a file as input, find the processes using that file.
### :round_pushpin: List files opened by processes (ex: sshd, httpd).

### :round_pushpin: List processes listening on a specific port (ex: PORT 22)
To find the process/service listening on a particular port, type (specify the port).

```
lsof -i :80
```

OR

```
ss -ltnp | grep -w ':80' 

l – tells netstat to only show listening sockets.
t – tells it to display tcp connections.
n – instructs it show numerical addresses.
p – enables showing of the process ID and the process name.
grep -w – shows matching of exact string (:80).

```
### :round_pushpin: Find the status of a service (ex: httpd)
Command to check status:

```
sudo systemctl status [service_name]

sudo systemctl status apache2
```

### :round_pushpin: Find zombie processes on a machine.
Pipe the output of the ps command through grep to list out any process whose STAT is Z (for zombie).

```
ps aux | grep 'Z'

```

### :round_pushpin: Find the environment variables on a machine.
By using ```printenv``` command we can see the environment variables.

```printenv```

### :round_pushpin: Display processes started by a user.
To view only the processes owned by a specific user, use the following command:

```top -U [username]```

```top -U mehul```

Replace the [username] with the required username

If you want to use ps then

```ps -u [username]```

### :round_pushpin: Kill a process.
### :round_pushpin: List open ports.
```ss``` command will list all the open TCP and UDP ports:
```ss -lntu```
```
-l – prints only listening sockets
-n – shows port number
-t – enables listing of tcp ports
-u – enables listing of udp ports
```
### :round_pushpin: Find the permission set for a file.
