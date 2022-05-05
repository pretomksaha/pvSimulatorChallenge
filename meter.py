import random

import pika


class Meter():

    def __init__(self):
        self.brokeHost = 'localhost'
        self.brokePort = ''
        self.brokeCredentials = pika.PlainCredentials('', '')
        self.brokerQueue=''
        self.minWatt=0
        self.maxWatt=9000


    def connection(self):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
            )

            channel = connection.channel()
            channel.queue_declare(queue='hello')
            channel.confirm_delivery()
            powerValue= self.powerGenerate()
            self.publishMassage(channel,powerValue)
        except pika.exceptions.ConnectionClosedByBroker:
            print("The connection  is terminated by Broker.")

    def powerGenerate(self):
        generatePower=random.uniform(self.minWatt,self.maxWatt)
        return generatePower


    def publishMassage(channel,powerValue):
        channel.basic_publish(exchange='',routing_key='hello',body=f"Hello World{powerValue}")

        channel.close()