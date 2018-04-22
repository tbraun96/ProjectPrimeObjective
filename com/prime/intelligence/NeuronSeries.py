from com.prime.intelligence.Brain import Brain


class NeuronSeries:
    brain = Brain()
    COLUMN_INDEX = 0
    DEPTH = 0
    NEURONS = []

    def __init__(self, brain, COLUMN_INDEX, DEPTH):
        self.brain = brain
        self.COLUMN_INDEX = COLUMN_INDEX
        self.DEPTH = DEPTH
