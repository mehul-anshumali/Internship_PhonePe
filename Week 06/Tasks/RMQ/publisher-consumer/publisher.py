import pika as p, sys, time

def main():  
    credentials = p.PlainCredentials('mehul', 'mehul')
    parameters = p.ConnectionParameters(host='192.168.178.128', 
                                        port='5672', 
                                        virtual_host='testvhost', 
                                        credentials=credentials)
    connection = p.BlockingConnection(parameters)

    channel = connection.channel()

    queue_status = channel.queue_declare(queue='DATA', durable=True)

    channel.exchange_declare(exchange='testExchange',
                            exchange_type='direct',
                            durable=True)
    
    channel.queue_bind(exchange='testExchange', 
                    queue='DATA', 
                    routing_key='testRoute')
    
    # msg = ' '.join(sys.argv[1:]) or 'Hello'

    msg_props = p.BasicProperties(delivery_mode=2)

    # Choice to send publish mesage
    sendChoice = input('Want to publish messages (Y/N):')

    if sendChoice == 'Y' or sendChoice == 'y':
        print('Publishing messages.....')
        time.sleep(0.3)
        for i in range(1,101):
            msg = f'Hello {i}'
            channel.basic_publish(body=msg,
                                exchange='testExchange',
                                routing_key='testRoute',
                                properties=msg_props)

            print(f'[x] Sent \'{msg}\' message...')

    elif sendChoice == 'N' or sendChoice == 'n':
        print('Closing connection...')
        connection.close()

    else:
        print("Please enter correct choice to send message ... Quiting this process :(")

    # Choice to check queue is empty or not 
    queueStatusChoice = input('Want to check whether queue is empty or not (Y/N):')

    if queueStatusChoice == 'Y' or queueStatusChoice == 'y':
        if queue_status.method.message_count == 0:
            print('Queue empty')
        else:
            print('Queue is not empty')

    elif queueStatusChoice == 'N' or queueStatusChoice == 'n':
        print('Quiting... :(')

    else:
        print("Please enter correct choice... Quiting this process :(")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


