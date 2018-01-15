import unittest
from data import DataFormatter as df
import os


class MyTestCase(unittest.TestCase):

    DEFAULT_TEST_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test_data", "waves_price.csv"))

    def test_getDataFiles(self):
        zeroDataFiles = df.DataFormatter([])
        self.assertEqual(zeroDataFiles.getDataFiles(), [])
        singleDataFile = df.DataFormatter(["x"])
        self.assertEqual(singleDataFile.getDataFiles(), ["x"])
        multipleDataFiles = df.DataFormatter(["abc", "xyz", "test3"])
        self.assertEqual(multipleDataFiles.getDataFiles(),["abc", "xyz", "test3"])

    def test_parseDataFiles(self):
        dataFormatter = df.DataFormatter([self.DEFAULT_TEST_FILE])
        dataFormatter.parseDataFiles()
        dataHashRows = dataFormatter.getDataHash()[self.DEFAULT_TEST_FILE]
        firstRow = dataHashRows[0]
        self.assertEqual(firstRow['Open'], '3.52')
        anotherRow = dataHashRows[26]
        self.assertEqual(anotherRow['Volume'], '6,289,170')

    def test_getPredictionFormattedDataFromCsv(self):
        dataFormatter = df.DataFormatter([self.DEFAULT_TEST_FILE])
        dataFormatter.parseDataFiles()
        dataFormatter.getPredictionFormattedDataFromCsv(self.DEFAULT_TEST_FILE, 5, "High")

    def test_formatRowForLastObservationCarriedForward(self):
        thisRow = {}
        lastRow = {}
        df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        self.assertDictEqual(thisRow, lastRow)
        thisRow["SomeKey"] = "3"
        df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        self.assertEqual(thisRow["SomeKey"], "3")
        thisRow["SomeKey"] = "x"
        with self.assertRaises(KeyError):
            df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        lastRow["SomeKey"] = "y2"
        with self.assertRaises(ValueError):
            df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        lastRow["SomeKey"] = "7"
        df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        self.assertDictEqual(lastRow,thisRow)
        lastRow["SomeOtherKey"] = "87"
        df.DataFormatter.formatRowForLastObservationCarriedForward(lastRow, thisRow)
        self.assertEqual(thisRow["SomeKey"], lastRow["SomeKey"])
        self.assertEqual(thisRow["SomeKey"], "7")

    def test_formatCsvDataForLastObservationCarriedForward(self):
        testFile0 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test_data", "waves_price_locf_1.csv"))
        dataFormatter0 = df.DataFormatter([testFile0])
        dataFormatter0.parseDataFiles()
        dataFormatter0.cleanCommasFromNumericalValues()
        dataFormatter0.formatCsvDataForLastObservationCarriedForward(testFile0)
        csv0Data = dataFormatter0.getDataForCsv(testFile0)
        self.assertEqual(csv0Data[0]["Low"], "0")
        self.assertEqual(csv0Data[1]["Close"], "3.69")
        self.assertEqual(csv0Data[1]["Low"], "0")


if __name__ == '__main__':
    unittest.main()
