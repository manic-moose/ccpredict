import csv

class DataFormatter:

    dataFiles = []
    dataHash = {}

    def __init__(self, datafiles):
        self.dataFiles = datafiles

    def printDataFiles(self):
        for fileName in self.getDataFiles():
            print(fileName)

    def getDataFiles(self):
        return self.dataFiles

    def getDataHash(self):
        return self.dataHash

    def parseDataFiles(self):
        for fileName in self.getDataFiles():
            with open(fileName, "rt") as csvfile:
                csvRows = csv.DictReader(csvfile)
                csvRowArray = []
                for row in csvRows:
                    csvRowArray.append(row)
                self.dataHash[fileName] = csvRowArray

    def getPredictionFormattedDataFromCsv(self, csvKey, pointsOfHistory, dependentVariableKeyName):
        dataRows = self.getDataHash()[csvKey]
        assert(len(dataRows) > pointsOfHistory)
        dataPointCount = len(dataRows) - pointsOfHistory
        for dataPointNumber in range(0, dataPointCount):
           pass