import logging
import os
import pika
from support import Support
from dotenv import load_dotenv
load_dotenv()

class PVsimulator():
    """
    PVsimulator Class represent as PV simulator which receive the meter power value,
    generate PV power value and store in csv file.
    """
    def __init__(self):
        self.logger = logging.getLogger("log.log")
        self.brokeHost = os.getenv('BROKER_HOST')
        self.brokePort = os.getenv('BROKER_POST')
        self.brokeCredentials = pika.PlainCredentials(os.getenv('USER_NAME'), os.getenv('PASSWORD'))
        self.brokerQueue = os.getenv('BROKER_QUEUE')
        self.supportFunction=Support()


    def connection(self):
        """
        Establishing connection between broker and PV simulator.
        :return:
        """
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.brokeHost,port=self.brokePort,credentials=self.brokeCredentials)
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
        """
        Receive the massage from meter
        :param channel: The channel that is used for connection with broker
        :param method: Get ok
        :param properties: Basic properties
        :param body: The massage in byte
        :return:
        """
        try:
            self.logger.info("Massage received.")
            powerValue= float(body)
            pvPowerValue= self.supportFunction.powerGenerate()
            self.supportFunction.writeCSC(powerValue,pvPowerValue)

        except KeyboardInterrupt as error:
            self.logger.info("User terminates the process")




