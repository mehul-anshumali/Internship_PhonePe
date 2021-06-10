# Setup this server using Docker:
- Run the docker command:
  ```bash
  $ docker build --tag python-webserver .
  $ docker run -d -p 80:5001 python-webserver
  ```
