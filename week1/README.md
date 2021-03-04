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
### About LVM 
LVM (Logical Volume Manager) is a device mapper framework that provides logical volume management for the kernel. It is a tool for logical volume management which includes allocating disk, stripping, mirroring, and resizing logical volumes. With this, a hard disk or a set of hard disks is allocated to on or more physical volumes.

LVM functions by layering abstractions on top of physical storage devices. The basic layers that LVM uses, starting with the most primitive, are.
  i) Physical Volume (pv),
  ii) Volume Group (vg), and
  iii) Logical Volumne (lv)

### Creating and Managing LVM
Our first step is scan the system for block devices that LVM can see and manage. You can do this by the folllowing command:
```
sudo lvmdiskscan
```
<!--- Add the output of lvmdiskscan --->
After seeing the physical volume our next step is to see how many disks are available to manage and to add it to the physical volume.You can do this by the folllowing command:
```
sudo fdisk -l
```
<!--- Add the output of fdisk --->
#### Mark the Physical Devices as Physical Volumes
Now that we know the disks we want to use, we can mark them as physical volumes within LVM using the ```pvcreate``` command:
```
sudo pvcreate /dev/ /dev/
```
<!--- Add the output of pvcreate --->
This will write an LVM header to the devices to indicate that they are ready to be added to a volume group.

You can verify that LVM has registered the physical volumes by typing:
```
sudo pvs
```
<!--- Add the output --->
OR 
```
sudo pvscan
```
<!--- Add the output --->
OR 
```
sudo pvdisplay
```
<!--- Add the output --->

#### Add the Physical Volumes to a Volume Group
Now that we have created physical volumes from our devices, we can create a volume group. We will have to select a name for the volume group, which we’ll keep generic. We wil call it ```newVG```.

To create the volume group and add our physical volumes to it, type the following command:
```
sudo vgcreate newVG /dev/ /dev/
```


## Add another 10GB disk to the VM. Add it to the existing LVM.

## Run a HTTP server on this VM. Make sure that the server starts automatically when the system starts.

## Using packer automate the entire setup.
