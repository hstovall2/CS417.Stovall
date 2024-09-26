#Hudson Stovall
#CS 417
#Exam 1
#Question 2 Python FreqClass

class FrequencyDistribution:
    def __init__(self, dataList):
        self.dataList = dataList
        self.frequencyTable = {}
    def computeFrequencyTable(self):
        for item in self.dataList:
            if item in self.frequencyTable:
                self.frequencyTable[item] += 1
            else:
                self.frequencyTable[item] = 1
    def printFrequencyTable(self):
        for item, count in self.frequencyTable.items():
            print(f'{item}: {count}')

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
fd = FrequencyDistribution(data)
fd.computeFrequencyTable()
fd.printFrequencyTable()
