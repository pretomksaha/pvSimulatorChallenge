from meter import Meter
from pvsimulator import PVsimulator
import logging

def main():
    logger= logging.getLogger(filename='log.log', encoding='utf-8', level=logging.INFO,
                              format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    meter =Meter()
    pvsimulator= PVsimulator()
    meter.connection()
    pvsimulator.connection()



if __name__ == "__main__":
    main()