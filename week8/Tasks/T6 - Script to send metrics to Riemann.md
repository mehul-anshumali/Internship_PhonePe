# Write a script to collect the metrics previously collected by collectd and send it to riemann.
- Script :- https://github.com/mehul-anshumali/Internship_PhonePe/tree/main/week8/Tasks/scripts
  
- In this script, I used the ```psutil``` module to collect the operating system metrcics like ```cpu_usage```, ```disk_usage```, ```ram_usage```, etc. and to collect datastore ```RabbitMQ``` metrics, I used the ```RabbitMQ managagement HTTP API```. 
- For sending the metrcis to ```Riemann```, used the ```Bernhard``` riemann-client. 
  
