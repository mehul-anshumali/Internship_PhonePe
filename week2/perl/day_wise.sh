#!/bin/bash
logfile=/Users/mehul.intern/development/bash/scripts/access.log
logfile1=/home/mehul/learning_stuff/bash/first/access.log
write_file=record.txt

printf "<br/>Highest Requested Hosts, Upstream IP's and Paths Date-Wise<br/>"
printf "=================================================<br/>"
highest_requested (){
    date=$1
	cat $logfile | grep $date | awk '{print $NF}' | sort | uniq -c | sort -r | head -1 > $write_file
    host_times=$(awk '{print $1}' $write_file)
	host_name=$(awk '{print $2}' $write_file)
    
    cat $logfile | grep $date | awk '{print $9}' | sort | uniq -c | sort -r | head -1 > $write_file
    upstream_ip_times=$(awk '{print $1}' $write_file)
	upstream_ip=$(awk '{print $2}' $write_file)

    cat $logfile | grep $date | awk '{print $5}' | sort | uniq -c | sort -nr | head -1 > $write_file
    path_times=$(awk '{print $1}' $write_file)
    path=$(awk '{print $2}' $write_file)

  
    printf "<br/>+++++++++++++++++++<br/> On \"$date\"<br/>+++++++++++++++++++<br/><br/>"
    printf "\"$host_name\" was the highest requested upstream_ip and it was requested $host_times times.<br/><br/>"
	printf "\"$upstream_ip\" was the highest requested upstream_ip and it was requested $upstream_ip_times times.<br/><br/>"
    printf "\"$path\" was highest requested path and it was requested $path_times times.<br/><br/>"
    printf "<br/><br/>"
}

# Function Call- highest requested(date)
# highest_requested 12/Feb/20
# highest_requested 06/Mar/2021
# highest_requested 07/Mar/2021
#highest_requested 08/Mar/2021
