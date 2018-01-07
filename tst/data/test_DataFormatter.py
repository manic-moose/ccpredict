import unittest
from data import DataFormatter
import os


class MyTestCase(unittest.TestCase):

    DEFAULT_TEST_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test_data", "waves_price.csv"))

    def test_getDataFiles(self):
        zeroDataFiles = DataFormatter.DataFormatter([])
        self.assertEqual(zeroDataFiles.getDataFiles(), [])
        singleDataFile = DataFormatter.DataFormatter(["x"])
        self.assertEqual(singleDataFile.getDataFiles(), ["x"])
        multipleDataFiles = DataFormatter.DataFormatter(["abc", "xyz", "test3"])
        self.assertEqual(multipleDataFiles.getDataFiles(),["abc", "xyz", "test3"])

    def test_parseDataFiles(self):
        dataFormatter = DataFormatter.DataFormatter([self.DEFAULT_TEST_FILE])
        dataFormatter.parseDataFiles()
        dataHashRows = dataFormatter.getDataHash()[self.DEFAULT_TEST_FILE]
        firstRow = dataHashRows[0]
        self.assertEqual(firstRow['Open'], '3.52')
        anotherRow = dataHashRows[26]
        self.assertEqual(anotherRow['Volume'], '6,289,170')

    def test_getPredictionFormattedDataFromCsv(self):
        dataFormatter = DataFormatter.DataFormatter([self.DEFAULT_TEST_FILE])
        dataFormatter.parseDataFiles()
        dataFormatter.getPredictionFormattedDataFromCsv(self.DEFAULT_TEST_FILE, 5, "High")


if __name__ == '__main__':
    unittest.main()
