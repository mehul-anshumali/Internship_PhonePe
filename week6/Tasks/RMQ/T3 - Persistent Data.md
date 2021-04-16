# Data should be persisted on disk.
- For data to be persistent on disk 
  - At the time of creation of queue make ```Durable = True``` & 
  - At the times of publishing messages make the ```delivery_mode = 2```.
 
Reference :- https://kousiknath.medium.com/dabbling-around-rabbit-mq-persistence-durability-message-routing-f4efc696098c
