from color import *
from math import floor, fabs
from random import randint

class DNA(object):
    """docstring for DNA."""

    def __init__(self, num):
        # super(DNA, self).__init__()
        self.fitness = 0
        self.genes = [newColor() for a in range(num)]

    def mostrar(self):
        # print([{repr(self.genes[i][j])} for j in range (len(self.genes[i])) for i in range (len(self.genes))])
        for i in range (len(self.genes)):
            print(repr(self.genes[i]))

    def calcFitness(self, target):
        score = 0
        # score += sum(list(map(lambda x : 100 - floor((fabs(x[0] - x[1])/255)*100), zip(self.genes[i][j], target[i][j]))))
        for i in range (len(self.genes)):
            score += 100 - floor((fabs(self.genes[i]["r"] - target[i]["r"])/255)*100)
            score += 100 - floor((fabs(self.genes[i]["g"] - target[i]["g"])/255)*100)
            score += 100 - floor((fabs(self.genes[i]["b"] - target[i]["b"])/255)*100)
        self.fitness = score / (3 * len(self.genes))

    def crossover(self, partnerB):
        midpoint = floor(randint(0, len(self.genes)))
        for i in range(len(self.genes)):
            if i > midpoint:
                self.genes[i] = partnerB.genes[i]
        return self

    def mutate(self, mRate, target):
        for i in range (len(self.genes)):
            if randint(0, 1) < mRate:
                self.genes[i] = newColor(self.genes[i], target[i])
