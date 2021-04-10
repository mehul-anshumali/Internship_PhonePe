# Mount /var/log on a seperate mount.
  Create and add a new disk to OS. Using LVM attach this disk. Mount this disk using ext4 file system. 
  Configure the OS for single user mode. By typing the command: ```init 1```.
  Move the ```/var/log``` content to new mounted directory. Let’s say newly mounted directory is ```/mnt/tmp_vol```.
  ```
  mv /var/log/* /mnt/tmp_vol/
  ```
  Now, we will configure new disk to mount On boot.
  First we will un-mount the volume:
  ```
  umount /mnt/tmp_vol
  ```
  Next we add an entry to the /etc/fstab file to mount this volume to /var/log on bootup:
  ```sudo nano /etc/fstab ``` then add this line ```/dev/vg_log/lv_log /var/log ext4 defaults 0 0```

  Now reload the fstab file to mount the volume:

  ```mount -a```

  Configure OS For Multi User Mode And Reboot.```init 5```  ```reboot```

  <img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/var_task.png">
