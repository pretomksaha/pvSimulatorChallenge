from meter import Meter
from pvsimulator import PVsimulator
import logging


def meter():
    meter = Meter()
    meter.connection()


def pv_simulator():
    pvsimulator = PVsimulator()
    pvsimulator.connection()


def main():
    logging.basicConfig(filename='../log.log', filemode="a", level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    meter()
    pv_simulator()


if __name__ == "__main__":
    main()