import logging
import unittest
from App.meter import Meter
from App.support import Support
import pika


class testMeter(unittest.TestCase):
    logger = logging.getLogger("log.log")
    brokeHost = 'localhost'
    brokePort = 5672
    brokeCredentials = pika.PlainCredentials('guest','guest')
    brokerQueue = "Massage"
    supportFunction = Support()

    def test_connection(self):
        """
        Test the connection
        :return:
        """
        try:
            Meter.connection(self)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_publish_massage(self):
        """
        Test to publish massage
        :return:
        """
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest','guest'))
        )
        channel = connection.channel()
        channel.queue_declare(queue="Massage")
        channel.confirm_delivery()
        powerValue = 50
        try:
            Meter.publish_massage(self,channel,powerValue)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


    def publish_massage(self,channel, powerValue):
        """
        Published the random power value of meter.
        :return:
        """
        try:
            channel.basic_publish(exchange='',routing_key=self.brokerQueue,body=f"{powerValue}",mandatory=True,properties=pika.BasicProperties( delivery_mode = 2, ))
            channel.close()

        except pika.exceptions.UnroutableError:
            self.logger.error("Massage can not be send.")
        except KeyboardInterrupt as error:
            self.logger.info("User terminates the process")


if __name__ == "__main__":
    unittest.main()


