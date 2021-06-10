# Send collectd metrics to influxdb.
- ## Login to InfluxDB server:
  - #### Login to the influxdb shell:
    ```
    $ sudo influx
    ```
    - Create a user and a database:
      ```
      > CREATE USER admin WITH PASSWORD 'admin' WITH ALL PRIVILEGES

      > CREATE DATABASE collectd
      ```
  - #### Open this ```/etc/influxdb/influxdb.conf``` file.
    - Find the ``[collectd]``` section and add the below contents: 
      ```
      [Collectd]
      enabled = true
      bind-address = ":25826"
      database = "collectd"
      typesdb = "/usr/share/collectd/types.db"
      ```
   - Create a directory:
     ```
     sudo mkdir /usr/share/collectd
     ```
   - Get the ```types.db``` file in that directory:
     ```
     sudo wget -P /usr/share/collectd https://raw.githubusercontent.com/collectd/collectd/master/src/types.db
     ```
- ## Login to collectd server:
  - #### Edit the ```nano /etc/collectd/collectd.conf``` file.
    - Add the below content:
      - Uncomment the ```LoadPlugin network```.
      ```
      <Plugin network>
        <Server "INFLUXDB_IP" "25826">
        </Server>
        ReportStats true
      </Plugin>
      ```
- ## Testing - To see the collectd metrics in influxdb.
  - Login to influxdb server:
    - Login to influx shell:
      ```
      $ sudo influx
      ```
    - Perform the below steps:
      ```
      Connected to http://localhost:8086 version 1.8.4
      InfluxDB shell version: 1.8.4
      > USE collectd
      Using database collectd
      > SHOW MEASUREMENTS
      name: measurements
      name
      ——
      cpu_value
      memory_value
      ...
      > SELECT * FROM cpu_value LIMIT 5
      ....
      ```
