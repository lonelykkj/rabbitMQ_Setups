# app/config.py

RABBITMQ_CONFIG = {
    'host': 'localhost',
    'port': 5672,
    'username': 'guest',
    'password': 'guest',
    'queue': 'data_queue',
    'exchange': 'data_exchange',
    'routing_key': ''
}
