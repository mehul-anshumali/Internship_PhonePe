# Run a http server on this VM . Make sure that the server starts automatically when the system starts.
- ## Install the Apache2 web server software as follows.
  ```
  sudo apt install apache2
  ```
- ## Managing the Apache in Ubuntu 20.04
  ```
  sudo systemctl stop apache2      #stop apache2
  sudo systemctl start apache2     #start apache2
  sudo systemctl restart apache2   #restart apache2
  sudo systemctl reload apache2    #reload apache2
  sudo systemctl disable apache2   #disable apache2
  sudo systemctl enable apache2    #enable apache2
  ```
- ## Configuring Apache in Ubuntu 20.04
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
 
