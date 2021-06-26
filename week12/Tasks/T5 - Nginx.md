# Setup VM4, install Nginx on it. Create a self-signed SSL Certificate and set up a proxy using Nginx which listens on port 443 with SSL enabled and forwards the requests to Traefik.

- ## Install Opens-SSL:
  ```
  sudo apt-get install openssl
  ```
- ## Generate Certificate:
  ```
  sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/localhost.key -out /etc/ssl/certs/localhost.crt
  ```
  Show Something like this...
  ```
  Country Name (2 letter code) []:
  State or Province Name (full name) []:
  Locality Name (eg, city) []:
  Organization Name (eg, company) []:
  Organizational Unit Name (eg, section) []:
  Common Name (eg, fully qualified host name) []: your_ip_address
  Email Address []:
  ```
- ## Install Nginx:
  ```
  sudo apt install nginx
  ```
- ## Enable SSL on nginx:
  ```
  sudo unlink /etc/nginx/sites-enabled/default
  ```
  - ### Add new file in `/etc/nginx/sites-available/reverse-proxy.conf` file:
  ```
  server {
        listen 80;
        listen [::]:80;
        listen 443 ssl;

        server_name 192.168.84.150;
        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;
        ssl_certificate /etc/nginx/localhost.crt;
        ssl_certificate_key /etc/nginx/localhost.key;

        location / {
                    proxy_pass http://192.168.84.75; 
    }
  }
  ```
  - ### Copy the configuration from /etc/nginx/sites-available to /etc/nginx/sites-enabled. It is recommended to use a symbolic link:
  ```
  sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
  ```

  - ### Test the Nginx configuration:
    ```
    sudo nginx -t
    ```
  - ### Restat Nginx:
    ```
    sudo systemctl restart nginx
    ```
    Nginx IP :- `192.168.84.150
    <img width="1792" alt="Screenshot 2021-06-26 at 1 55 07 PM" src="https://user-images.githubusercontent.com/44754882/123507279-2b93cb80-d686-11eb-8ffd-bbb83120c7cb.png">


