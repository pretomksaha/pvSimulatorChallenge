from meter import Meter
from pvsimulator import PVsimulator
import logging


def meter():
    """
    Create a constractor for meter and connect with broker Rabbitmq
    :return:
    """
    meter = Meter()
    meter.connection()


def pv_simulator():
    """
    Create a constractor for PV simulator and connect with broker Rabbitmq
    :return:
    """
    pvsimulator = PVsimulator()
    pvsimulator.connection()


def main():
    """
    Main function configure log file and call (meter, simulator)
    :return:
    """
    logging.basicConfig(filename='log.log', filemode="a", level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    meter()
    pv_simulator()


if __name__ == "__main__":
    main()