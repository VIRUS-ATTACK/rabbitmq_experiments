import pika
import sys

# connect to a broker(localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# declare queue
channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent 'Hello World!'")
connection.close()