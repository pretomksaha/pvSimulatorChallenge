import pika
from support import Support

class pvsimulator():

    def __init__(self):
        self.brokeHost = 'localhost'
        self.brokePort = ''
        self.brokeCredentials = pika.PlainCredentials('', '')
        self.brokerQueue=''


    def connection(self):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
            )

            channel = connection.channel()
            channel.queue_declare(queue=self.brokerQueue)

            channel.basic_consume(queue=self.brokerQueue, on_message_callback=self.receivePower, auto_ack=True)
            channel.start_consuming()
            print('[*] waiting for messages to exit press ctrl +c')
        except pika.exceptions.ConnectionClosedByBroker:
            print("The connection  is terminated by Broker.")


    def receivePower(self,channel,method,properties,body):
        powerValue= float(body)
        pvPowerValue= Support.powerGenerate()
        Support.writeCSC(powerValue,pvPowerValue)
        channel.basic_ack(delivery_tag = method.delivery_tag)


