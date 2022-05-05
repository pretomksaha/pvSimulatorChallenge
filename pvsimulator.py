import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

def callback(ch,method,properties,body):
    print("[x] Received %r" %body)

channel.basic_consume(queue='hello',on_message_callback=callback, auto_ack=True)

print('[*] waiting for messages to exit press ctrl +c')
channel.start_consuming()