import pika
import sys

# connect to a broker(localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# declare queue
channel.queue_declare(queue='task_queue', durable=True)

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode = 2, # make message persistent
    )
)
print(" [x] Sent 'Hello World!'")
connection.close()