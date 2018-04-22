import quantumrandom

from com.prime.graphics.RasterLoader import rasterTo1DArray
from com.prime.intelligence.NeuronSeries import NeuronSeries


class Brain:
    networkType = ""
    learningRate = 0.0
    momentumDelta = 0.0
    inputData = []
    neuronSeries = []

    def __init__(self, filename, networkType, learningRate, momentumDelta, *args):
        self.networkType = networkType
        self.learningRate = learningRate
        self.momentumDelta = momentumDelta
        self.inputData = rasterTo1DArray(filename)

        if (len(args) > 0):
            if (networkType == "BP"):
                """args[0] => numHiddenLayers"""
                self.neuronSeries = [None] * (1 + args[0] + 1)
                hiddenLayers = args[0]
                for n in range(0, hiddenLayers + 1):
                    self.neuronSeries[n] = NeuronSeries(self, n + 1, len(self.inputData))

    def getQuantumRandomSeed(self):
        return quantumrandom.get_data()

    def getNeuronSeries(self, COLUMN_INDEX):
        return self.neuronSeries[COLUMN_INDEX]

    def getInputs(self):
        return self.inputData
