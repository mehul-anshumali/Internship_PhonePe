# :dart: Week 1 Tasks Lists 

## Install VBox
Follow this detailed post to downlaod and install Virtual Box on your system - :point_right: https://data-flair.training/blogs/install-virtualbox/

## Download and Install Ubuntu Server Focal Fossia 20.04
Follow this youtube tutorial to install Ubuntu Server 20.04 on your Virtual Box - :point_right: https://www.youtube.com/watch?v=XPqLGYUpGQA

## Create users who are a part of internship. Create a group named 'intern' and add users to that group.
To create a user or add a new user, enter the following command in your shell
```
sudo adduser <username>
sudo adduser mehulanshumali
```

To create a group, enter the following command in your shell
```
sudo addgroup <groupname>
sudo addgroup intern
```
To add user to a group, enter the following command in your shell
```
sudo adduser <username> <groupname>
sudo adduser mehulanshumali intern
```

## Add 2 disks each of 10GB each to this VM. Create a LVM using these two disks and create XFS filesystem on it. Mount this on /data directory and make sure that mount persists across reboots.

## Add another 10GB disk to the VM. Add it to the existing LVM.

## Run a HTTP server on this VM. Make sure that the server starts automatically when the system starts.

## Using packer automate the entire setup.
