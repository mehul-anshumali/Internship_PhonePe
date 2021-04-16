import pika as p, sys, os, time


def main():
    credentials = p.PlainCredentials('mehul', 'mehul')
    parameters = p.ConnectionParameters(host='192.168.178.128', 
                                        port='5672', 
                                        virtual_host='testvhost', 
                                        credentials=credentials)

    connection = p.BlockingConnection(parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange='testExchange',
                            exchange_type='direct',
                            durable=True)

    channel.queue_declare(queue='DATA', durable=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.queue_bind(exchange='testExchange', 
                    queue='DATA', 
                    routing_key='testRoute')

    def msg_callback(ch, method, properties, body):
        print(f"[x] Received \'{body.decode()}\' ")
        time.sleep(0.3)
        print("[x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='DATA', on_message_callback=msg_callback)

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



