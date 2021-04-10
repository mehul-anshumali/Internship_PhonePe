# Add another 10GB disk to the VM. Add it to the existing LVM.
  We will add 10GB disk from virtual box and after this we will first create the physical volume of newly added disk i.e ```/dev/sdd```.
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
