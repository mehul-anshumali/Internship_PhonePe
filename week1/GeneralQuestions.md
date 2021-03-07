# :rocket: General Questions Lists  :rocket:
### :fire: Find the processes running on a linux machine.
The most common way to list processes currently running on your system is to use the ```ps``` command. Used without any options, the ps command displays only processes that are started from the current shell.
To get information about all processes running on the system, use ```ps -a```.\
To get get more clear idea about processes running on the system use a,u and x options with ps. This displays all processes running for all users on your system, along with useful information such as the username of the process′ owner, CPU loads, the starting time of the process, the command that initiated the process, etc.
```ps -aux```
```
a : Select all processes
u : Select all processes on a terminal, including those of other users
x : Select processes without controlling ttys
```
### :fire: Find the users currently logged in.
By using ```who``` command you can see the logged in user.
If you want to see the list of users currently logged in you have to give option ```a``` with ```who``` command: ```who -a```.
Others command are also available they are ```w```, ```users```.
### :fire: Find the uptime of the machine.
You can check system uptime by using command ```uptime```. It displays how long the system has been running.
### Find the RAM usage.
To display free memory size in MB (megabytes). You can use the ```free -h``` command. 
### :fire: Find the disk usage.
The ```df``` command shows the amount of disk space used and available on file systems. You can use ```h``` option with it check the disk usage in more understandable from ```df -h```.
### :fire: Find the inode usage.
The ```df -i``` command shows the usage and availability of inodes. You can use ```h``` option with it check the disk usage in more understandable from ```df -ih```.
### :fire: Find the ulimit of a user.
Limits are categorized as either soft or hard:
Soft limit – All users can change soft limits, up to max set by the hard limits. Pass the -S option to the ulimit.
Hard limit – Only root users allowed to change esource hard limits. Pass the -H option to the ulimit.
Command to view all soft and hard limits for the current user: 
```
ulimit -Sa ## Show soft limit ##
ulimit -Ha ## Show hard limit ##
```
### :fire: Find the ulimit of a process.
You can check the ulimits for any process ID by reading ```/proc/<pid>/limits```, where <pid> is replaced by the numeric pid of the process.
  ```
  cat /proc/<pid>/limits
  ```

### :fire: Find the file description used by a process.

### :fire: Find the top 5 process by memory usage.
### :fire: Find the top 5 process by CPU usage.
### :fire: Find the top 5 process by network usage.
### :fire: Find the top 5 usage by disk iops usage.
### :fire: Find the network traffic and bandwidth usage of the machine.
### :fire: Given a file as input, find the processes using that file.
### :fire: List files opened by processes (ex: sshd, httpd).
### :fire: List processes listening on a specific port (ex: PORT 22)
### :fire: Find the status of a service (ex: httpd)
### :fire: Find zombie processes on a machine.
### :fire: Find the environment variables on a machine.
### :fire: Display processes started by a user.
### :fire: Kill a process.
### :fire: List open ports.
### :fire: Find the permission set for a file.
