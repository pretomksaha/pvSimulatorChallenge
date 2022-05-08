import logging
import unittest
from App.pvsimulator import PVsimulator
from App.support import Support
import pika


class testSimulator(unittest.TestCase):

    logger = logging.getLogger("log.log")
    brokeHost = 'localhost'
    brokePort = 5672
    brokeCredentials = pika.PlainCredentials('guest', 'guest')
    brokerQueue = "Massage"
    supportFunction = Support()

    def test_connection(self):
        """
        Test the connection
        :return:
        """
        try:
            PVsimulator.connection(self)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_receivePower(self):
        """
        Test the receive data from
        :return:
        """
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
        )
        channel = connection.channel()
        channel.queue_declare(queue="Massage")
        try:
            channel.basic_consume(queue=self.brokerQueue, on_message_callback=PVsimulator.receivePower, auto_ack=True)
            channel.start_consuming()
            channel.stop_consuming()
            connection.close()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def receivePower(self, channel, method, properties, body):
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
            powerValue = float(body)
            pvPowerValue = self.supportFunction.powerGenerate()
            self.supportFunction.writeCSC(powerValue, pvPowerValue)

        except KeyboardInterrupt as error:
            self.logger.info("User terminates the process")


if __name__ == "__main__":
    unittest.main()
