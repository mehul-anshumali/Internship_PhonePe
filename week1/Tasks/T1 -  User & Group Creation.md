# Install VBOX on your laptop
- Downloded & Installed VBox. 
  - 👉 https://www.virtualbox.org/wiki/Downloads
  
# Download Ubuntu Focal ISO
- Downloaded Ubuntu Server 20.04 Focal Fossia.
  - 👉 https://releases.ubuntu.com/20.04/ubuntu-20.04.2-live-server-amd64.iso

# Install Ubuntu Focal ( give 2 cpu cores and 512 MB of RAM . Do not install the GUI. )
  - Installed Ubuntu Server 20.04 Focal Fossia.

# Create users who are a part of internship. Create a group named ```intern``` and add users to that group.
- To create a user or add a new user, enter the following command in your shell:
  ```
  sudo adduser <username>
  sudo adduser mehulanshumali
  ```
  <img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/users_list.png" width="600" height="500">
  
- To create a group, enter the following command in your shell:
  ```
  sudo addgroup <groupname>
  sudo addgroup intern
  ```
- To add user to a group, enter the following command in your shell:
  ```
  sudo adduser <username> <groupname>
  sudo adduser mehulanshumali intern
  ```
  <img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/group_list.png" width="600" height="500">
