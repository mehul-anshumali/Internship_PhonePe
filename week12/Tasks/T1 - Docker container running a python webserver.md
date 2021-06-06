# Create a Docker container running a python webserver, that listens on port 80 and returns the string "Hello world" for any requests.
- Download the python-webserver from 👉 :- <a href="https://github.com/mehul-anshumali/Internship_PhonePe/tree/main/week12/Tasks/python-webserver">👨‍💻
- ## Build and run the docker image:
  ```bash
  $ docker build --tag python-webserver .
  $ docker run -d -p 80:5001 python-webserver
  ```
