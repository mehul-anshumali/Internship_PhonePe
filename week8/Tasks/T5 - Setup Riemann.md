# Setup riemann on a vm.
- ## Riemann Installation:
  - ### Install Packages:
    ```
    sudo apt-get -y install default-jre ruby-dev zlib1g-dev build-essential
    ```
  - ### Download .deb file:
    ```
    wget https://github.com/riemann/riemann/releases/download/0.3.6/riemann_0.3.6_all.deb
    ```
  - ### Install .deb file:
    ```
    sudo dpkg -i riemann_0.3.6_all.deb 
    ```
  - ### Install ```riemann-packages```:
    ```
    sudo gem install --no-ri --no-rdoc riemann-client riemann-tools riemann-dash
    ```
- ## Riemann Configuration:
  - ### Edit the ```/etc/riemann/riemann.config``` file:
    ```
    Change the localhost IP i.e. (let [host “127.0.0.1"]) to (let [host "0.0.0.0"]).
    ```
  - ### Create a new file named ```config.rb```.
    - Add the below line :
      ```
      set :bind, "your-ip" # Bind to a different interface
      ```
   - ## Run the ```riemann-dash```:
    ```
    riemann-dash config.rb
    ```
   - ### Go to web browser ```http://your-ip:4567``` to see the riemann dashboard.
   - ## Change the IP address in the address bar in top-right corner of riemann-dashboard.
