# Plot these metrics on a grafana dashboards.
- ## Install Grafana:
  - ### Add Repository:
    ```
    sudo echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list 
    ```
  - ### Import GPG key:
    ```
    sudo wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
    ```
  - ### Update apt index and install Grafana:
    ```
    sudo apt-get update && apt-get install grafana
    ```
  - ### Start the Grafana service:
    ```
    sudo systemctl start grafana.service
    ```
  #### Browse to ```http://your-ip:3000``` and login with ```admin:admin```.
- ## Add the Data Source:
  <p align="center">
    <img src="https://user-images.githubusercontent.com/44754882/116513959-f5d1a100-a8e7-11eb-9873-df702c5123d5.png" height=800>
  </p>

- ## Plotting the metrices:
  - Go to dashboard, create an empty panel.
    - Give query as of your choice to plot the metrics.
    - Mine was:- ``` SELECT mean("value") FROM "df_value" WHERE ("host" = 'ubuntu1') AND time >= now() - 6h GROUP BY time(20s) fill(null) ```
    - Apply and save.
