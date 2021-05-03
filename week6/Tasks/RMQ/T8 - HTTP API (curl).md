- ## Take a dump of the messages in DATA_SIDELINE queue using RMQ API/curl.
  ```bash
  $ curl -u mehul:mehul -H "content-type:application/json" -XPOST http://192.168.178.23:15672/api/queues/testvhost/DATA_SIDELINE/get -d’{"count":15,"ackmode":"ack_requeue_true","encoding":"auto","truncate":50000}' -o messages.json
  ```

- ## Delete the messages from the DATA_SIDELINE queue using RMQ API/curl.
  ```bash
  $ curl -i -u mehul:mehul -H "content-type:application/json" -XDELETE http://192.168.178.23:15672/api/queues/testvhost/DATA_SIDELINE/contents
  ```
