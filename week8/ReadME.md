# Week 8 Tasks List
```
This week you will be monitoring the setup for the datastore you worked on last week.
```
- Setup collectd to monitor various metrics for operating system and one of the following datastores ES/RMQ/AS.
- Setup influxdb on a vm.
- Send collectd metrics to influxdb.
- Plot these metrics on a grafana dashboards.
- Setup riemann on a vm.
- Write a script to collect the metrics previously collected by collectd and send it to riemann.
- The metrics should go to influxdb from riemann.
- Metrics such as disk usage/ram usage/HWM etc should have a threshold (80%) and should send a critical alert to riemann once the threshold is breached.
