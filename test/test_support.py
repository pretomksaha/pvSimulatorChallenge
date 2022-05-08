import os
import unittest
import csv
from App.support import Support
import logging

class testSupport(unittest.TestCase):
    minWatt = 0
    maxWatt = 9000
    listOutput = []
    logger = logging.getLogger("log.log")
    csvHeader = ['timestamp', 'meter power value', 'PV power value', 'The sum of the powers (meter + PV)']
    outputFile = 'temp.csv'

    def test_generate_power(self):
        """
        Test to generate power
        :return:
        """

        self.assertLess(Support.powerGenerate(self),9000)

    def test_write_csv(self):
        """
        Test write csv
        :return:
        """
        Support.writeCSC(self,50,100)
        with open('temp.csv', 'r') as csv_file:
            csvreader = csv.reader(csv_file)
            header = next(csvreader)
            self.assertEqual(header,['timestamp', 'meter power value', 'PV power value', 'The sum of the powers (meter + PV)'])

        os.remove('temp.csv')



if __name__ == "__main__":
    unittest.main()