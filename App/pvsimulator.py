import logging
import os
import pika
from support import Support
from dotenv import load_dotenv
load_dotenv()

class PVsimulator():

    def __init__(self):
        self.logger = logging.getLogger("log.log")
        self.brokeHost = os.getenv('BROKER_HOST')
        self.brokePort = os.getenv('BROKER_POST')
        self.brokeCredentials = pika.PlainCredentials(os.getenv('USER_NAME'), os.getenv('PASSWORD'))
        self.brokerQueue = os.getenv('BROKER_QUEUE')
        self.supportFunction=Support()


    def connection(self):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.brokeHost)
            )

            channel = connection.channel()
            channel.queue_declare(queue=self.brokerQueue)

            channel.basic_consume(queue=self.brokerQueue, on_message_callback=self.receivePower, auto_ack=True)
            channel.start_consuming()
        except pika.exceptions.ConnectionClosedByBroker:
            self.logger.error("The connection  is terminated by Broker.")
        except pika.exceptions.ChannelError:
            self.logger.error("There has an connection problem.")
        except KeyboardInterrupt as error:
            channel.stop_consuming()
            connection.close()
            self.logger.info("User terminates the process")


    def receivePower(self,channel,method,properties,body):
        try:
            self.logger.info("Massage received.")
            powerValue= float(body)
            pvPowerValue= self.supportFunction.powerGenerate()
            self.supportFunction.writeCSC(powerValue,pvPowerValue)

        except KeyboardInterrupt as error:
            self.logger.info("User terminates the process")




