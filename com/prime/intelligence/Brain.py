import quantumrandom

from com.prime.graphics.RasterLoader import rasterTo1DArray
from com.prime.intelligence.NeuronSeries import NeuronSeries


class Brain:
    networkType = ""
    learningRate = 0.0
    momentumDelta = 0.0
    inputData = []
    neuronSeries = []
    expectedOutputs = []

    def __init__(self, filename, networkType, learningRate, momentumDelta, expectedOutputs, *args):
        self.networkType = networkType
        self.learningRate = learningRate
        self.momentumDelta = momentumDelta
        self.inputData = rasterTo1DArray(filename)
        self.expectedOutputs = expectedOutputs

        if (len(args) > 0):
            if (networkType == "BP"):
                """args[0] => numHiddenLayers"""
                self.neuronSeries = [None] * (1 + args[0] + 1)
                hiddenLayers = args[0]
                """Setup Input Layer + Hidden Layer"""
                self.neuronSeries[0] = NeuronSeries(self, "INPUT", 0, len(self.inputData))
                for n in range(0, hiddenLayers):
                    self.neuronSeries[n + 1] = NeuronSeries(self, "HIDDEN", n + 1, len(self.inputData))

                self.neuronSeries[len(self.neuronSeries) - 1] = NeuronSeries(self, "OUTPUT", len(self.neuronSeries) - 1,
                                                                             len(expectedOutputs))

        print(self.printSelf())

    def getQuantumRandomSeed(self):
        return quantumrandom.get_data()

    def getNeuronSeries(self, COLUMN_INDEX):
        return self.neuronSeries[COLUMN_INDEX]

    def getInputs(self):
        return self.inputData

    def printSelf(self):
        print("Brain:", len(self.neuronSeries), "columns")
        return 0
