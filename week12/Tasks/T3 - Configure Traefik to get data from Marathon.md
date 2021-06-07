# Configure Traefik to get its data from Marathon.

- In [traefik.toml](https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week12/Tasks/Traefik/traefik.toml) added **marathon provider** to get data from marathon.
  ```
  [providers.marathon]
  endpoint = "http://192.168.67.48:8080"
  exposedByDefault = true
  watch = true
  respectReadinessChecks = true
  ```
- Save and Restart `docker traefik` image:
  ```
  sudo docker restart traefik
  ```
  
