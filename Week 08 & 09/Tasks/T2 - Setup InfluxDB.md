# Setup influxdb on a VM.
- ## Add Repository:
  ```
  sudo echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | tee /etc/apt/sources.list.d/influxdb.list
  ```
- ## Import GPG key:
  ```
  sudo curl -sL https://repos.influxdata.com/influxdb.key | apt-key add -
  ```
- ## Update apt index and install InfluxDB:
  ```
  sudo apt-get update && sudo apt-get install influxdb
  ```
- ## Start the influxdb service
  ```
  sudo systemctl start influxdb.service
  ```

