import logging
import os
from csv import writer
import random
from datetime import datetime

class Support():
    """
    Support class has all the supporting methods.
    like: power generator, csv writer
    """

    def __init__(self):
        self.logger = logging.getLogger("../log.log")
        self.minWatt = int(os.getenv('MIN_WATTS'))
        self.maxWatt = int(os.getenv('MAX_WATTS'))
        self.listOutput = []
        self.csvHeader = ['timestamp','meter power value','PV power value','The sum of the powers (meter + PV)']
        self.outputFile='../records.csv'

    def powerGenerate(self):
        """
        Generate a random power in between min and max range
        :return:
        """
        generatePower=random.uniform(self.minWatt,self.maxWatt)
        return generatePower

    def writeCSC(self, powerValue, pvPowerValue):
        """
        store value in CSV
        :param powerValue: the power comes from meter
        :param pvPowerValue: the power comes from PV simulator
        :return:
        """
        try:
            sumMeterPV = powerValue+pvPowerValue
            self.listOutput.append(datetime.now())
            self.listOutput.append(powerValue)
            self.listOutput.append(pvPowerValue)
            self.listOutput.append(sumMeterPV)
            self.logger.info("Massage start to store on CSV")
            if not os.path.exists(self.outputFile):
                with open(self.outputFile, 'a', newline='') as header_object:
                    # Pass this file object to csv.writer()
                    # and get a writer object
                    writer_object = writer(header_object)

                    # Pass the list as an argument into
                    # the writerow()
                    writer_object.writerow(self.csvHeader)

                    # Close the file object
                    header_object.close()

            with open(self.outputFile, 'a', newline='') as f_object:
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(self.listOutput)

                # Close the file object
                f_object.close()
                self.logger.info("Massage stored on CSV successfully")
                self.listOutput=[]

        except:
            self.logger.error("Massage can not store on CSV")

