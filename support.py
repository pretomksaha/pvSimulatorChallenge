import os
from csv import writer
import random
from datetime import datetime

class Support():

    def __init__(self):
        self.minWatt = int(os.getenv('MIN_WATTS'))
        self.maxWatt = int(os.getenv('MAX_WATTS'))
        self.listOutput = []

    def powerGenerate(self):
        generatePower=random.uniform(self.minWatt,self.maxWatt)
        return generatePower

    def writeCSC(self, powerValue, pvPowerValue):

        sumMeterPV = powerValue+pvPowerValue
        self.listOutput.append(f'timestamp:{datetime.now()}')
        self.listOutput.append(f'meter power value:{powerValue} W')
        self.listOutput.append(f'PV power value:{pvPowerValue} W')
        self.listOutput.append(f'The sum of the powers (meter + PV):{sumMeterPV} W')

        with open('event.csv', 'a', newline='') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(self.listOutput)

            # Close the file object
            f_object.close()

