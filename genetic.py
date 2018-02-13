from population import Population
from math import floor
from random import randint

target = []
popmax = 50
mutationRate = 0.01
population = None

def setup():
    global target
    global population
    for x in range(1000):
        gen = {
            "r": floor(randint(0, 255)),
            "g": floor(randint(0, 255)),
            "b": floor(randint(0, 255))
        }
        target.append(gen)

    # print(target)

    population = Population(target, mutationRate, popmax)
    population.calcFitness()

def life():
    while population.isFinished() == False:
        population.calcFitness()
        population.naturalSelection()
        population.generate()
        population.evaluate()

        if population.generations%5 == 0:
            print(population.generations)
            # print(population.best)

    print('Finish')
    print(population.generations)
    # print(population.best)

setup()
life()
