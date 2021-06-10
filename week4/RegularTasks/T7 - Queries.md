# Use MariaDB Queries to provide the stats below

 - **Summary for the day/week/month:**
 
    - highest requested host
    
    ```sql
    MariaDB [Nginx]> select distinct(substring_index(time,':',1)) as date, host, count(*) as times from ngnix_access_log group by date, host;
    ```
    ```sql
    +-------------+----------------------+-------+
    | date        | host                 | times |
    +-------------+----------------------+-------+
    | 06/Mar/2021 | api.ppops.com        |  3174 |
    | 06/Mar/2021 | appone.ppops.com     |  3288 |
    | 06/Mar/2021 | apptwo-new.ppops.com |  3075 |
    | 06/Mar/2021 | apptwo.ppops.com     |  3126 |
    | 06/Mar/2021 | prod.ppops.pm5       |  3300 |
    | 07/Mar/2021 | api.ppops.com        |  5790 |
    | 07/Mar/2021 | appone.ppops.com     |  5883 |
    | 07/Mar/2021 | apptwo-new.ppops.com |  5623 |
    | 07/Mar/2021 | apptwo.ppops.com     |  5725 |
    | 07/Mar/2021 | prod.ppops.pm5       |  5900 |
    | 08/Mar/2021 | api.ppops.com        |  1216 |
    | 08/Mar/2021 | appone.ppops.com     |  1238 |
    | 08/Mar/2021 | apptwo-new.ppops.com |  1258 |
    | 08/Mar/2021 | apptwo.ppops.com     |  1186 |
    | 08/Mar/2021 | prod.ppops.pm5       |  1256 |
    | 12/Feb/2021 | api.ppops.com        |   635 |
    | 12/Feb/2021 | appone.ppops.com     |   653 |
    | 12/Feb/2021 | apptwo-new.ppops.com |   635 |
    | 12/Feb/2021 | apptwo.ppops.com     |   676 |
    | 12/Feb/2021 | prod.ppops.pm5       |   635 |
    +-------------+----------------------+-------+
    20 rows in set (0.150 sec)
    ```
    
    - highest requested upstream_ip
      ```sql
      MariaDB [Nginx]> select distinct(substring_index(time,':',1)) as date, upstream_ip_port, count(*) as times from ngnix_access_log group by date, upstream_ip_port limit 10;
      ```
      ```sql
      +-------------+------------------+-------+
      | date        | upstream_ip_port | times |
      +-------------+------------------+-------+
      | 06/Mar/2021 | 10.77.22.10:443  |   426 |
      | 06/Mar/2021 | 10.77.22.10:80   |   501 |
      | 06/Mar/2021 | 10.77.22.10:8443 |   471 |
      | 06/Mar/2021 | 10.77.22.11:443  |   501 |
      | 06/Mar/2021 | 10.77.22.11:80   |   462 |
      | 06/Mar/2021 | 10.77.22.11:8443 |   471 |
      | 06/Mar/2021 | 10.77.22.12:443  |   480 |
      | 06/Mar/2021 | 10.77.22.12:80   |   408 |
      | 06/Mar/2021 | 10.77.22.12:8443 |   402 |
      | 06/Mar/2021 | 10.77.22.13:443  |   447 |
      +-------------+------------------+-------+
      ```
    
    - highest requested path (upto 2 subdirectories ex: /check/balance)
      ```sql
      MariaDB [Nginx]> select distinct(substring_index(time,':',1)) as date, path, count(*) as times from ngnix_access_log group by date, path limit 10;
      ```
      ```sql
      +-------------+--------------------------------------------------------------------------+-------+
      | date        | path                                                                     | times |
      +-------------+--------------------------------------------------------------------------+-------+
      | 06/Mar/2021 | /check/balance/24%20hour/encompassing                                    |     3 |
      | 06/Mar/2021 | /check/balance/24%20hour/toolset                                         |     3 |
      | 06/Mar/2021 | /check/balance/24/7                                                      |     6 |
      | 06/Mar/2021 | /check/balance/24/7/Persevering                                          |     3 |
      | 06/Mar/2021 | /check/balance/24/7/portal_implementation                                |     3 |
      | 06/Mar/2021 | /check/balance/3rd%20generation                                          |     3 |
      | 06/Mar/2021 | /check/balance/3rd%20generation%206th%20generation/zero%20administration |     3 |
      | 06/Mar/2021 | /check/balance/3rd%20generation_utilisation                              |     3 |
      | 06/Mar/2021 | /check/balance/4th%20generation-Phased-Implemented                       |     3 |
      | 06/Mar/2021 | /check/balance/5th%20generation                                          |     3 |
      +-------------+--------------------------------------------------------------------------+-------+
      ```
  
  - **Total requests per status code (Ex: count of requests returning 404/401/502/504/500/200)**
    ```sql
    MariaDB [Nginx]> select distinct(statusCode), count(*) as count from ngnix_access_log group by statusCode;
    ```
    ```sql
    +------------+-------+
    | statusCode | count |
    +------------+-------+
    | 100        |   548 |
    | 200        | 43826 |
    | 201        |   500 |
    | 203        |   571 |
    | 204        |   626 |
    | 205        |   570 |
    | 301        |   464 |
    | 302        |   585 |
    | 304        |   510 |
    | 400        |   522 |
    | 401        |   419 |
    | 403        |   519 |
    | 404        |   522 |
    | 405        |   440 |
    | 406        |   521 |
    | 416        |   533 |
    | 500        |   521 |
    | 501        |   501 |
    | 502        |   641 |
    | 503        |   519 |
    | 504        |   414 |
    +------------+-------+
    21 rows in set (0.068 sec)
    ```
  - **Top requests**
    - top 5 requests by upstream_ip
    
      ```sql
      MariaDB [Nginx]> select distinct(upstream_ip_port), host,count(*) as count from ngnix_access_log group by upstream_ip_port order by count desc limit 5;
      ```
      ```sql
      +------------------+----------------------+-------+
      | upstream_ip_port | host                 | count |
      +------------------+----------------------+-------+
      | 10.77.22.10:80   | api.ppops.com        |  1701 |
      | 10.77.27.14:8443 | apptwo-new.ppops.com |  1683 |
      | 10.77.22.11:443  | apptwo.ppops.com     |  1675 |
      | 10.77.22.12:443  | apptwo-new.ppops.com |  1603 |
      | 10.77.22.11:80   | prod.ppops.pm5       |  1598 |
      +------------------+----------------------+-------+
      5 rows in set (0.123 sec)
      ```
      
    - top 5 requests by host
      
      ```sql
      MariaDB [Nginx]> select distinct(host), path,count(*) as count from ngnix_access_log group by host order by count desc limit 5;
      ```
      ```sql
      +----------------------+---------------------------------------------------------+-------+
      | host                 | path                                                    | count |
      +----------------------+---------------------------------------------------------+-------+
      | prod.ppops.pm5       | /check/balance/Re-engineered/Graphic%20Interface        | 11091 |
      | appone.ppops.com     | /recharge/phone/parallelism%20Optimized/homogeneous     | 11062 |
      | api.ppops.com        | /myapi/consumers/definition/Operative/solution-oriented | 10815 |
      | apptwo.ppops.com     | /recharge/phone/Reactive-functionalities/optimal        | 10713 |
      | apptwo-new.ppops.com | /myapi/consumers/encoding/Reverse-engineered/logistical | 10591 |
      +----------------------+---------------------------------------------------------+-------+
      5 rows in set (0.118 sec)
      ```
      
    - top 5 requests by bodyBytesSent
      
      ```sql
      MariaDB [Nginx]> select distinct(bodyBytesSent),host ,path,count(*) as count from ngnix_access_log group by bodyBytesSent order by count desc limit 5;
      ```
      ```sql
      +---------------+------------------+-----------------------------------------------------+-------+
      | bodyBytesSent | host             | path                                                | count |
      +---------------+------------------+-----------------------------------------------------+-------+
      | 38            | appone.ppops.com | /check/balance/strategy/standardization/web-enabled |   179 |
      | 70            | appone.ppops.com | /myapi/consumers/transitional/multimedia            |   160 |
      | 51            | apptwo.ppops.com | /recharge/dth/next%20generation%20Automated         |   158 |
      | 61            | appone.ppops.com | /myapi/kyc/Multi-tiered-User-friendly               |   157 |
      | 60            | apptwo.ppops.com | /check/balance/Synergistic/Universal                |   157 |
      +---------------+------------------+-----------------------------------------------------+-------+
      ```
      
    - top 5 requests by path (upto 2 subdirectories ex: /check/balance)
      
      ```sql
      MariaDB [Nginx]> select distinct(path),host,ip ,count(*) as count from ngnix_access_log group by path order by count desc limit 5;
      ```
      ```sql
      +-------------------------------------+------------------+----------------+-------+
      | path                                | host             | ip             | count |
      +-------------------------------------+------------------+----------------+-------+
      | /recharge/phone/bandwidth-monitored | prod.ppops.pm5   | 129.253.196.12 |    47 |
      | /recharge/dth/empowering            | apptwo.ppops.com | 121.47.30.21   |    45 |
      | /myapi/kyc/needs-based              | apptwo.ppops.com | 100.174.92.102 |    38 |
      | /recharge/dth/info-mediaries        | appone.ppops.com | 129.208.149.18 |    37 |
      | /check/balance/transitional         | apptwo.ppops.com | 140.173.243.15 |    35 |
      +-------------------------------------+------------------+----------------+-------+
      5 rows in set (0.364 sec)
      ```
      
    - top 5 requests with the highest response time
      
      ```sql
      MariaDB [Nginx]> select distinct(responseTime), host as requested_by, ip as from_ip from ngnix_access_log order by CAST(responseTime as decimal(5,3)) desc limit 5;
      ```
      ```sql
      +--------------+------------------+-----------------+
      | responseTime | requested_by     | from_ip         |
      +--------------+------------------+-----------------+
      | 19.998       | prod.ppops.pm5   | 93.253.163.77   |
      | 19.978       | api.ppops.com    | 245.47.77.99    |
      | 19.975       | api.ppops.com    | 250.110.178.176 |
      | 19.969       | appone.ppops.com | 64.26.144.139   |
      | 19.960       | prod.ppops.pm5   | 197.149.212.133 |
      +--------------+------------------+-----------------+
      5 rows in set (0.205 sec)
      ```
      
    - get top 5 requests returning 200/5xx/4xx per host
      
      ```sql
      MariaDB [Nginx]> select distinct(host), statusCode , count(*) as count from ngnix_access_log group by host order by count desc;
      ```
      ```sql
      +----------------------+------------+-------+
      | host                 | statusCode | count |
      +----------------------+------------+-------+
      | prod.ppops.pm5       | 200        | 11091 |
      | appone.ppops.com     | 200        | 11062 |
      | api.ppops.com        | 200        | 10815 |
      | apptwo.ppops.com     | 500        | 10713 |
      | apptwo-new.ppops.com | 200        | 10591 |
      +----------------------+------------+-------+
      5 rows in set (0.114 sec)
      ```
  - **Find the time last 200/5xx/4xx was received for a particular host**
  
  - **Get all request for the last 10 minutes**
  
  - **Get all the requests taking more than 2/5/10 secs to respond.**
   ```sql
   MariaDB [Nginx]> select distinct(responseTime), host as requested_by, ip as from_ip from ngnix_access_log where CAST(responseTime as decimal(5,3)) > 2 order by CAST(responseTime as decimal(5,3)) asc limit 10;
   ```
   ```sql
   +--------------+----------------------+-----------------+
   | responseTime | requested_by         | from_ip         |
   +--------------+----------------------+-----------------+
   | 2.002        | apptwo-new.ppops.com | 206.231.222.78  |
   | 2.005        | api.ppops.com        | 214.20.39.165   |
   | 2.014        | prod.ppops.pm5       | 169.213.80.192  |
   | 2.022        | appone.ppops.com     | 108.228.137.121 |
   | 2.023        | apptwo.ppops.com     | 21.146.140.86   |
   | 2.024        | prod.ppops.pm5       | 57.70.201.116   |
   | 2.037        | apptwo-new.ppops.com | 157.221.60.36   |
   | 2.039        | appone.ppops.com     | 125.172.169.110 |
   | 2.042        | prod.ppops.pm5       | 151.197.55.243  |
   | 2.062        | appone.ppops.com     | 213.179.135.131 |
   +--------------+----------------------+-----------------+
   ```
  
  - **Get all the requests in the specified timestamp (Ex: from 06/Mar/2021:04:48 to 06/Mar/2021:04:58)**
   ```sql
   MariaDB [Nginx]> select host, ip, path, time,count(*) as count from ngnix_access_log where time between '06/Mar/2021:00:00:00' and '06/Mar/2021:23:55:55' group by host order by count desc;
   ```
   ```sql
   +----------------------+---------------+---------------------------------------------------------+----------------------------+-------+
   | host                 | ip            | path                                                    | time                       | count |
   +----------------------+---------------+---------------------------------------------------------+----------------------------+-------+
   | prod.ppops.pm5       | 0.134.114.15  | /check/balance/Re-engineered/Graphic%20Interface        | 06/Mar/2021:07:27:39 +3970 |  3300 |
   | appone.ppops.com     | 0.10.20.123   | /recharge/phone/parallelism%20Optimized/homogeneous     | 06/Mar/2021:07:31:36 +3670 |  3288 |
   | api.ppops.com        | 0.125.114.184 | /myapi/consumers/definition/Operative/solution-oriented | 06/Mar/2021:07:16:58 +5870 |  3174 |
   | apptwo.ppops.com     | 0.105.114.213 | /recharge/phone/Reactive-functionalities/optimal        | 06/Mar/2021:07:18:51 +5170 |  3126 |
   | apptwo-new.ppops.com | 0.10.237.185  | /myapi/kyc/migration%20orchestration                    | 06/Mar/2021:07:28:01 +0170 |  3075 |
   +----------------------+---------------+---------------------------------------------------------+----------------------------+-------+
   ```
