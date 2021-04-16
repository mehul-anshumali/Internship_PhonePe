# Truncate the partitions from week 21 to 25
- Week 21 to 25 no data is available in log file.
- So, I am truncating ```week6```.

  ```
  MariaDB [Nginx]> alter table ngnix_access_log truncate partition week6;
  ```
