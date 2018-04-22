# from com.prime.intelligence.Brain import Brain


class NeuronSeries:
    #brain = Brain()
    COLUMN_INDEX = 0
    DEPTH = 0
    NEURONS = []
    NEURON_TYPE = ""

    def __init__(self, brain, NEURON_TYPE, COLUMN_INDEX, DEPTH):
        #self.brain = brain
        self.COLUMN_INDEX = COLUMN_INDEX
        self.DEPTH = DEPTH
        self.NEURON_TYPE = NEURON_TYPE
