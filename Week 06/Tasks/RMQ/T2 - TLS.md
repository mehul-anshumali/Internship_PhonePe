# The RMQ cluster should be on TLS and have a username/password.
- To have TLS on cluster, we required three certificates .
  - ```ca_certificate.pem```: a certificate authority bundle
  - ```server_certificate.pem```: a certificate (public key) that will be used by the configured node (and/or CLI tools)
  - ```server_key.pem```: a private key that will be used by the configured node (and/or CLI tools)
- Generate the certificates by following below steps:
  ```
  $ git clone https://github.com/michaelklishin/tls-gen tls-gen
  $ cd tls-gen/basic
  $ make PASSWORD=mehul
  $ make verify
  $ make info
  $ ls -l ./result
  ```
- Make a new directory in ```/etc/rabbitmq```
  ```
  $ sudo mkdir ssl
  ```
- Copy these three certificates into this directory ```/etc/rabbitmq/ssl```.
- Configure the ```/etc/rabbitmq/rabbitmq.config``` file.
  ```
  $ sudo nano /etc/rabbitmq/rabbitmq.config
  ```
  - Add the below lines:
    ```
    [
    {rabbit, [
       {ssl_listeners, [5671]},
       {ssl_options, [{cacertfile, "/etc/rabbitmq/ssl/ca_certificate.pem"},
                      {certfile,   "/etc/rabbitmq/ssl/server_certificate.pem"},
                      {keyfile,    "/etc/rabbitmq/ssl/server_key.pem"},
                      {verify,     verify_peer},
                      {fail_if_no_peer_cert, true}]}
     ]}
    ].
    ```
- Generate a new certificate: 
  ```
  $ cat server_certificate.pem server_key.pem > combined_keys.pem
  ```
- Configure the ```/etc/rabbitmq/rabbitmq-env.conf``` file.
  ```
  $ sudo nano /etc/rabbitmq/rabbitmq-env.conf
  ```
  - Add the below lines: 
    ```
    ERL_SSL_PATH="/usr/lib/erlang/lib/ssl-9.2.3.7/ebin/"

    SERVER_ADDITIONAL_ERL_ARGS="-pa $ERL_SSL_PATH \
      -proto_dist inet_tls \
      -ssl_dist_opt server_certfile /etc/rabbitmq/ssl/combined_keys.pem \
      -ssl_dist_opt server_password mehul \
      -ssl_dist_opt server_secure_renegotiate true client_secure_renegotiate true"

    RABBITMQ_CTL_ERL_ARGS="-pa $ERL_SSL_PATH \
      -proto_dist inet_tls \
      -ssl_dist_opt server_certfile /etc/rabbitmq/ssl/combined_keys.pem \
      -ssl_dist_opt server_password mehul \
      -ssl_dist_opt server_secure_renegotiate true client_secure_renegotiate true"
    ```
  
  - #### Transfer/Copy the above generated certificates to other servers. Do not generate new certificates. 
  - #### Perform the above steps to configure other servers.
  
