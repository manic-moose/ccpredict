import csv
from utils import DataUtils as dutils
import logging

module_logger = logging.getLogger("ccpredict.DataFormatter")


class DataFormatter:

    # list of paths to csv files
    dataFiles = []

    # dataHash->{csv file name}->[array of data rows]
    dataHash = {}

    def __init__(self, datafiles):
        if (isinstance(datafiles, list)):
            self.dataFiles = datafiles
        else:
            self.dataFiles = []
            self.dataFiles.append(datafiles)
        self.dataFiles = datafiles
        self.logger = logging.getLogger("ccpredict.DataFormatter.DataFormatter")

    def printDataFiles(self):
        for fileName in self.getDataFiles():
            print(fileName)

    def getDataForCsv(self, fileName):
        if fileName in self.getDataHash():
            return self.getDataHash()[fileName]
        else:
            self.logger.error("Invalid filename " + fileName + " Key not present in dataHash")
            raise KeyError

    def getDataFiles(self):
        return self.dataFiles

    def getDataHash(self):
        return self.dataHash

    def parseDataFiles(self):
        for fileName in self.getDataFiles():
            try:
                csvfile = open(fileName, "rt")
                csvRows = csv.DictReader(csvfile)
                csvRowArray = []
                for row in csvRows:
                    csvRowArray.append(row)
                self.dataHash[fileName] = csvRowArray
                csvfile.close()
            except FileNotFoundError:
                self.logger.error("Cannot find file: " + fileName)

    # This will simply substitute out commas in all the data
    # if the value is a number. Definition of a number is that
    # it passes isNumber check after commas deleted
    def cleanCommasFromNumericalValues(self):
        for csvFileKey in self.getDataFiles():
            csvFileDataRows = self.getDataHash()[csvFileKey]
            for dataRowIndex in range(0, len(csvFileDataRows)):
                dataRow = csvFileDataRows[dataRowIndex]
                for rowKey in dataRow.keys():
                    rowValue = dataRow[rowKey]
                    if (isinstance(rowValue, str)):
                        rowValueCommaRemoved = rowValue.replace(",", "")
                        if (dutils.isNumber(rowValueCommaRemoved)):
                            dataRow[rowKey] = rowValueCommaRemoved

    def getPredictionFormattedDataFromCsv(self, csvKey, pointsOfHistory, dependentVariableKeyName):
        dataRows = self.getDataHash()[csvKey]
        assert(len(dataRows) > pointsOfHistory)
        dataPointCount = len(dataRows) - pointsOfHistory
        for dataPointNumber in range(0, dataPointCount):
            rowIndexStart = dataPointNumber
            for rowIndex in range(rowIndexStart, rowIndexStart + pointsOfHistory):
                pass

    # Formats all data in the dataHash using LOCF to
    # remove any non-numeric data
    def formatAllDataForLastObservationCarriedForward(self):
        for fileName in self.getDataFiles():
            self.formatCsvDataForLastObservationCarriedForward(fileName)

    # Replaces any values in the data that isn't a numerical value
    # with the last observation. If the missing/non-numeric data is
    # in the first row, then the data is replaced with 0
    def formatCsvDataForLastObservationCarriedForward(self, csvKey):
        dataRows = self.getDataHash()[csvKey]
        # Check first row to verify it has complete data
        # If any is missing in the first row, LOCF won't have any data to refer
        # back to. For this corner case, I'm just going to write 0 to any
        # missing data. This leaves the potential for 0's to get carried
        # forward if data is missing in the next row as well, but that
        # should be low risk since I need to check the data first anyways. I will
        # print a warning to catch this situation anyways
        if (len(dataRows) > 0):
            firstDataRow = dataRows[0]
            for dataRowKey in firstDataRow.keys():
                value = firstDataRow[dataRowKey]
                if (not dutils.isNumber(value)):
                    self.logger.warning("Replacing first row data with 0 for csvFile " + csvKey + " and data key: " + dataRowKey)
                    firstDataRow[dataRowKey] = "0"
            for dataRowIndex in range(1, len(dataRows)):
                self.formatRowForLastObservationCarriedForward(dataRows[dataRowIndex-1], dataRows[dataRowIndex])

    @staticmethod
    def formatRowForLastObservationCarriedForward(lastRow, thisRow):
        for dataRowKey in thisRow.keys():
            thisValue = thisRow[dataRowKey]
            if (not dutils.isNumber(thisValue)):
                try:
                    lastValue = lastRow[dataRowKey]
                    if (dutils.isNumber(lastValue)):
                        thisRow[dataRowKey] = lastValue
                    else:
                        module_logger.error("Could not complete LOCF replacement. Previous row data not valid")
                        module_logger.error("Previous row contains value " + lastValue + " for key " + dataRowKey)
                        raise ValueError
                except KeyError:
                    module_logger.error("Could not complete LOCF replacement. Previous row missing data key")
                    raise KeyError
