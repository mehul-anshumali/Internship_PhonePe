# The metrics should go to influxdb from riemann.
- ## Create a new database(```riemann_db```) in influxdb, login to influx shell:
  ```sql
  > CREATE DATABASE riemann_db
  ```
- ## Edit the ```riemann.config``` file, located at ```/etc/riemann/riemann.config```
  ```bash
  sudo nano /etc/riemann/riemann.config
  ```
  - Add the below lines:
    ```clojure
    (def send-to-influxdb (
    influxdb {
        :version :0.9
        :host "192.168.66.44"
        :db "riemann_db"
        :port 8086

    })
    )
    
    
    (streams
      send-to-infuxdb)
    ```
- ## The riemann configuration file will look like this:
  ```clojure
  ; -*- mode: clojure; -*-
  ; vim: filetype=clojure
  (def send-to-influxdb (
      influxdb {
          :version :0.9
          :host "192.168.66.44"
          :db "riemann_db"
          :port 8086

      })
  )
  (logging/init {:file "/var/log/riemann/riemann.log"})

  ; Listen on the local interface over TCP (5555), UDP (5555), and websockets
  ; (5556)
  (let [host "0.0.0.0"]
    (tcp-server {:host host})
    (udp-server {:host host})
    (ws-server  {:host host}))

  ; Expire old events from the index every 5 seconds.
  (periodically-expire 5)

  (let [index (index)]
    ; Inbound events will be passed to these streams:
    (streams
      (default :ttl 60
        ; Index all events immediately.
        (where (= (:service) "disk_usage")
         (adjust [:service str " Gb"]
                 (scale (/ 1024 1024 1024) )))
        index
        send-to-influxdb
        ;#(info %)
        ; Log expired events.
        (expired
          (fn [event] (info "expired" event))))))
  ```
