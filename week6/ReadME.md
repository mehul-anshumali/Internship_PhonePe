# Week 6 Tasks List
```
This week's agenda is:
- To understand the use/function/working of various data stores.
- Find out various settings/configurations available and apply the most optimum settings.
- Learn about how these systems work wrt the CAP theorem
- Learn about the various monitoring APIs/endpoints/commands exposed by these tools
- And gain maintenance and debugging knowledge.
```
  - ## Elasticsearch:
    - Install and configure 1 node elasticsearch cluster version 7.8.0
    - The ES cluster should be on TLS and have a username/password
    - Data should be persisted on disk
    - Check the various jvm options and come up with the appropriate heap and GC settings for your cluster (https://github.com/elastic/elasticsearch/blob/master/distribution/src/config/jvm.options)
    - Add 2 more nodes to the cluster without restarting elasticsearch service on first one
    - Create 3 indices (books details, author details, publishing company details) on the cluster, set the number of shards to be 3 for each index
    - Insert at least 10 documents per index.
    - The publishing company documents should be parent for the book details documents.
    - Take backup of all the indices
    - Delete all the indices
    - Restore them 
    
  - #### Additional task:
    - Upgrade elasticsearch to version 7.12 without losing the data
    - Capture slow logs for all the indices for queries taking longer than 1ms to respond
    - Manually reassign a shard to a different node
    
  - ## RMQ:
    - Install and configure 1 node RMQ cluster version 3.7.9
    - The RMQ cluster should be on TLS and have a username/password
    - Data should be persisted on disk
    - Add 2 more nodes to the cluster without restarting RMQ service on first one
    - Create a vhost and a user with read-write permissions to the vhost
    - Create 2 queues (DATA, DATA_SIDELINE) on the above created vhost
    - Create a publisher and consumer for the DATA queue, the messages which were not consumed by the consumer should move to the DATA_SIDELINE queue after a specific time.
    - Stop the consumer
    - Publish 100 messages to DATA queue
    - The 100 messages should automatically get moved to DATA_SIDELINE queue
    - Stop the publisher
    - Take a dump of the messages in DATA_SIDELINE queue using RMQ API/curl
    - Delete the messages from the DATA_SIDELINE queue using RMQ API/curl
    - Push the messages to DATA queue using RMQ API/curl

  - #### Additional task:
    - Upgrade RMQ to version 3.8.14 without losing the data
    - Create a network partition in RMQ and fix it manually
    - Change RMQ settings so that the network partition gets fixed automatically when the nodes reconnect.

  - ## Aerospike:
    - Install and configure 1 node Aerospike cluster version 4.8.0.6
    - The AS cluster should have a username/password
    - Data should be persisted on disk
    - Add 2 more nodes to the cluster without restarting AS service on first one
    - Create a namespace Orders
    - Write a program using an AS client to write and read the data from AS
    - The namespace should have the following sets (buyer details, product details)
    - Each set should have 3000 records.
    - The records should have an expiry of 24h
    - Shut down one of the nodes, optimise the AS cluster such that the data migration is faster
    - Bring back the node,start inserting 1000 records in the AS cluster while the data migration is going on.
    - Observe the ops/sec, read/write latencies and migration speed.

  - #### Additional tasks:
    - Upgrade AS to version 4.9 without loosing the data
    - Increase the memory assigned to the namespace by 25%
