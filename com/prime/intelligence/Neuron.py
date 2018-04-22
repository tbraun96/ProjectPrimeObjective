from com.prime.intelligence.Brain import Brain

INPUT_TYPE = "INPUT"
HIDDEN_TYPE = "HIDDEN"
OUTPUT_TYPE = "OUTPUT"


class Neuron:
    brain = Brain()
    COLUMN_INDEX = 0
    ROW_INDEX = 0
    NEURON_TYPE = ""

    def __init__(self, COLUMN_INDEX, ROW_INDEX, NEURON_TYPE, brain):
        self.brain = brain
        self.COLUMN_INDEX = COLUMN_INDEX
        self.ROW_INDEX = ROW_INDEX
        self.NEURON_TYPE = NEURON_TYPE
