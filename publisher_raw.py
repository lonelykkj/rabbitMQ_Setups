import pika 


connection_parameters = pika.ConnectionParameters(
    host='localgost',
    port=5672,
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange='data_exchange',
    routing_key='',
    body='Hello World!',
    properties=pika.BasicProperties(
        delivery_mode=2  
    )
)