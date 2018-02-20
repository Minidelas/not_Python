import pygame, sys
from population import Population
from math import floor
from random import randint

target = []
popmax = 50
mutationRate = 0.01
population = None
grid_length = 25
DIST_ = 2

def randomRGB():
    return { "r": floor(randint(0, 255)), "g": floor(randint(0, 255)), "b": floor(randint(0, 255)) }

def setup():
    global target
    global population
    target = [[randomRGB() for x in range(grid_length)] for y in range(grid_length)]

    population = Population(target, mutationRate, popmax)
    population.calcFitness()

def life():
    pygame.init()
    size = width, height = 4000, 400

    background_color = 255, 255, 255
    global screen
    screen = pygame.display.set_mode(size)

    while population.isFinished() == False:
        population.calcFitness()
        population.naturalSelection()
        population.generate()
        population.evaluate()

        if population.generations%5 == 0:
            print(population.generations)

        screen.fill(background_color)
        pintar(target)
        counter = 1

        for _dna in population.population:
            pintar(_dna.genes, (grid_length * counter) + (DIST_ * counter))
            counter += 1

        pygame.display.flip()

def pintar(genes, pos = 0):
    for x in range(len(genes)):
        for y in range(len(genes[x])):
            color = genes[x][y]['r'], genes[x][y]['g'], genes[x][y]['b']
            rect_w_color = pygame.Rect((DIST_*x) + (pos * DIST_), DIST_*y, DIST_, DIST_)
            pygame.draw.rect(screen, color, rect_w_color)

setup()
life()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

print(population)
