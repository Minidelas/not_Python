from color import *
from math import floor, fabs
from random import randint

class DNA(object):
    """docstring for DNA."""

    def __init__(self, num):
        # super(DNA, self).__init__()
        self.fitness = 0
        self.genes = [[newColor() for a in range(num)] for a in range(num)]

    def calcFitness(self, target):
        score = 0
        # score += sum(list(map(lambda x : 100 - floor((fabs(x[0] - x[1])/255)*100), zip(self.genes[i][j], target[i][j]))))
        for i in range(len(self.genes)):
            for j in range(len(self.genes[i])):
                score += 100 - floor((fabs(self.genes[i][j]["r"] - target[i][j]["r"])/255)*100)
                score += 100 - floor((fabs(self.genes[i][j]["g"] - target[i][j]["g"])/255)*100)
                score += 100 - floor((fabs(self.genes[i][j]["b"] - target[i][j]["b"])/255)*100)
        self.fitness = score / (3 * len(self.genes))

    def crossover(self, partnerB):
        for i in range(len(self.genes)):
            midpoint = floor(randint(0, len(self.genes[i])))
            for j in range(len(self.genes[i])):
                if j > midpoint:
                    self.genes[i][j] = partnerB.genes[i][j]
        return self

    def mutate(self, mRate, target):
        for i in range (len(self.genes)):
            for j in range (len(self.genes[i])):
                if randint(0, 1) < mRate:
                    self.genes[i][j] = newColor(self.genes[i][j], target[i][j])
