import logging
import os
import time

import pika
from support import Support
from dotenv import load_dotenv
load_dotenv()


class Meter():
    """
    Meter class represent as meter which take a reading of power and publish the power value throw broker rabbitmq.
    """
    def __init__(self):
        self.logger = logging.getLogger("../log.log")
        self.brokeHost = os.getenv('BROKER_HOST')
        self.brokePort = os.getenv('BROKER_POST')
        self.brokeCredentials = pika.PlainCredentials(os.getenv('USER_NAME'), os.getenv('PASSWORD'))
        self.brokerQueue = os.getenv('BROKER_QUEUE')
        self.supportFunction = Support()

    def connection(self):
        """
        Establishing connection between broker and meter.
        :return:
        """
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.brokeHost,port=self.brokePort,credentials=self.brokeCredentials)
            )
            channel = connection.channel()
            channel.queue_declare(queue=self.brokerQueue)
            channel.confirm_delivery()
            self.logger.info("Connection established")
            powerValue= self.supportFunction.powerGenerate()
            self.publish_massage(channel,powerValue)
        except pika.exceptions.ConnectionClosedByBroker:
            self.logger.error("The connection  is terminated by Broker.")
        except pika.exceptions.ChannelError:
            self.logger.error("There has an connection problem.")
        except KeyboardInterrupt as error:
            self.logger.info("User terminates the process")

    def publish_massage(self,channel, powerValue):
        """
        Published the random power value of meter.
        :return:
        """
        while(True):
            try:
                channel.basic_publish(exchange='',routing_key=self.brokerQueue,body=f"{powerValue}",mandatory=True,properties=pika.BasicProperties( delivery_mode = 2, ))
                time.sleep(2)

            except pika.exceptions.UnroutableError:
                self.logger.error("Massage can not be send.")
                continue
            except KeyboardInterrupt as error:
                self.logger.info("User terminates the process")
                break