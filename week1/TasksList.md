# :dart: Week 1 Tasks Lists 

## Install VBox
Follow this detailed post to download and install Virtual Box on your system - :point_right: https://data-flair.training/blogs/install-virtualbox/

## Download and Install Ubuntu Server Focal Fossia 20.04
Follow this youtube tutorial to install Ubuntu Server 20.04 on your Virtual Box - :point_right: https://www.youtube.com/watch?v=XPqLGYUpGQA

## Create users who are a part of internship. Create a group named 'intern' and add users to that group.
To create a user or add a new user, enter the following command in your shell
```
sudo adduser <username>
sudo adduser mehulanshumali
```
<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/users_list.png" width="600" height="500">

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

<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/group_list.png" width="600" height="500">

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
sudo pvcreate /dev/sdb /dev/sdc
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
sudo vgcreate newVG /dev/sdb /dev/sdc
```
You can verify that VG has created by typing:
```
sudo vgs
```
#### Creating Logical Volumes from the Volume Group
Now that we have a volume group available, we can use it as a pool that we can allocate logical volumes from. We wil call it ```newLV```.

To create the volume group and add our physical volumes to it, type the following command:
```
sudo lvcreate -n newLV -L 19G newVG
```
You can verify that LV has created by typing:
```
sudo lvs
```

#### Format and Mount the Logical Volume
We are mouting this ```newLV``` logical volume by XFS file system. 
So, first we need to install xfs file system utilities.
```
sudo apt-get install xfsprogs
```
Create a directory where this xfs file system will be mounted. We are mounting it in ```/data```.
```
mkdir /data
```
Now, to format our logical volume with the Xfs filesystem, we can type:
```
sudo mkfs.xfs /dev/newVG/newLV
```
After formatting, we mount it to ```/data``` directory:
```
sudo mount xfs /dev/newVG/newLV /data
```
<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/lvm_created.png" width="600" height="500">

To make the mounts persistent, add them to ```/etc/fstab```:
```
sudo nano /etc/fstab
```
```
/dev/newVG/newLV /data xfs defaults 0 0
```
Save ```ctrl+s``` and exit ```ctrl+x```.

Then, type ```mount -a```.

The operating system should now mount the LVM logical volumes automatically at boot.

## Add another 10GB disk to the VM. Add it to the existing LVM.
we will add 10GB disk from virtual box and after this we will first create the physical volume of newly added disk i.e ```/dev/sdd```.
Creating pv of new disk i.e /dev/sdd
```
sudo pvcreate /dev/sdd
```
Then we will the extend the already created vg (```newVG```).
```
sudo vgextend newVG /dev/sdd 
```
After this, we will expand our logical volume. Here I am expanding my lv ```newLV``` maximum (10GB).
```
sudo lvextend -l +9G /dev/newVg/newLV
```
After Extending, we need to re-size the file-system using. As I have used the Xfs file system earlier to create ```newLV``` LV. So we will resize it by using the following command:
```
sudo xfs_growfs /dev/newVG/newLV
```
 
<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/extended_lvm.png">


## Run a HTTP server on this VM. Make sure that the server starts automatically when the system starts.
#### Install the Apache2 web server software as follows.
```
sudo apt install apache2
```
#### Managing the Apache in Ubuntu 20.04
```
sudo systemctl stop apache2      #stop apache2
sudo systemctl start apache2     #start apache2
sudo systemctl restart apache2   #restart apache2
sudo systemctl reload apache2    #reload apache2
sudo systemctl disable apache2   #disable apache2
sudo systemctl enable apache2    #enable apache2
```
#### Configuring Apache in Ubuntu 20.04
```
sudo vim /etc/apache2/apache2.conf 
```
Add below line after ```#ServerRoot "/etc/apache2"```
```
ServerName "your VM ip"
```
```
ServerName 192.168.176.254
```
After adding the server name in the apache configuration, check the configuration syntax for correctness, and restart the service.
```
sudo apache2ctl configtest
sudo systemctl restart apache2
```
 Now when you check the apache2 service status, the warning should not appear.
 ```
 sudo systemctl status apache2
 ```
 Double checking server is runnning or not :
 ```
 curl -I 192.168.176.254
 curl -head 192.168.176.254
 ```
 
 <img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/server_verification.png">
 
 
## Using packer automate the entire setup.
## The users in the group interns should be able to login via private key, and not a password.
Generated the key using ```ssh``` command ```ssh-keygen```.
SSh keygen generates two types of keys public key and private key. And we have to copy public key. So type the followimg command.
```
ssh-copy-id -i ~/.ssh/id_rsa.pub hostname@your-server-ip

ssh-copy-id -i ~/.ssh/id_rsa.pub mehul-intern@192.168.176.254
```
That's it now you can login by using ```ssh mehul-intern@192.168.176.254```

<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/ssh.png">

## Mount /var/log on a seperate mount.

<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/var_task.png">


## The http server should only listen on the VMs IP and not localhost.
