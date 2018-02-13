from DNA import DNA
from math import floor
from random import randint

class Population(object):
    """docstring for Population."""
    def __init__(self, target, mRate, numPoblacion):
        self.muestreo = 30
        self.arrBest = []
        self.best_fitness = 0
        self.population = []
        self.matingPool = []
        self.finished = False
        self.generations = 0

        self.target = target
        self.mRate = mRate
        self.best = None

        for x in range (numPoblacion):
            self.population.append(DNA(len(self.target)))


    def calcFitness(self):
        self.best = None
        for _dna in self.population:
            _dna.calcFitness(self.target)
            if self.best and _dna.fitness > self.best.fitness:
                self.best_fitness = self.best.fitness
                self.best = _dna
            elif self.best == None:
                self.best = _dna
        if len(self.arrBest) > self.muestreo:
            self.arrBest.pop(0)
        self.arrBest.append(self.best)

    def getBestFitness(self):
        return self.best_fitness

    def naturalSelection(self):
        self.matingPool = []
        maxFitness = 0
        for _dna in self.population:
            if _dna.fitness > maxFitness:
                maxFitness = _dna.fitness
                self.best = _dna.genes

            fitness = self.custom_map(_dna.fitness, 0, maxFitness, 0, 1)
            n = floor(fitness * 100)
            # print("numero")
            # print(n)

            for val in range(n):
                self.matingPool.append(_dna)

    def generate(self):
        for x in range (len(self.population)):
            a = floor(randint(0, len(self.matingPool)-1))
            b = floor(randint(0, len(self.matingPool)-1))
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mRate, self.target)
            self.population[x] = child
        self.generations += 1

    def evaluate(self):
        for i in range(len(self.population)):
            count = 0
            for j in range(len(self.target)):
                if self.population[i].genes[j]["r"] == self.target[j]["r"] and self.population[i].genes[j]["g"] == self.target[j]["g"] and self.population[i].genes[j]["b"] == self.target[j]["b"]:
                    count += 1
            if count == len(self.target):
                self.finished = True

    def isFinished(self):
        return self.finished

    def dibujar(self):
        pass

    def custom_map(self, value, start1, stop1, start2, stop2):
        param1 = (100/(stop1 - start1) * value)/100
        res = (start2 + (100/(stop2 - start2))*param1)/100
        return res
