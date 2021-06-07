# Deploy the docker container that you created in #1 to run as a Marathon app and it should be reachable using the Traefik.

- Pushed the local docker container to Docker hub.
- JSON file to push app to Marathon `app.json`:
  ```
  {
    "id": "python",
    "instances": 1,
    "cpus": 0.5,
    "mem": 126,
    "container": {
      "type": "DOCKER",
      "docker": {
        "image": "mehulanshumali/python_webserver",
        "network": "BRIDGE",
        "portMappings": [
          {
            "containerPort": 5001,
            "hostPort": 0
          }
        ]
      }
    }
  }
  ```
- Configure `slave-server` to pull docker image:
  ```
  echo 'docker,mesos' > /etc/mesos-slave/containerizers
  echo '10mins' > /etc/mesos-slave/executor_registration_timeout

  $ sudo systemctl restart mesos-slave.service
  ```
- Push the app to marathon:
  ```
  curl -X POST http://192.168.210.48:8080/v2/apps -d @app.json -H "Content-type: application/json"
  ```
