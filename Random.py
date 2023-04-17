class PseudoRandom:
    def __init__(self,seed):
        self.seed = seed
        self.next = seed

    def getSeed(self):
        return self.seed

    def rand(self):
        self.next = self.next * 1103515245 + 12345
        return (self.next//65536) % 32768

    def randminmax(self,min,max):
        return (self.rand() % (max - min +1)) + min