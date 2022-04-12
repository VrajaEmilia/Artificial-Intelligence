import time
from repository import *
import random
import numpy

class controller():
    def __init__(self):
        self.__repository = repository()

    def iteration(self, population):
        # args - list of parameters needed to run one iteration
        # a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        nextGen = Population(self.__repository.getMap())
        selection = population.selection(int(population.getSize() / 2))
        while nextGen.getSize()<population.getSize():
            firstParent = selection[randint(0, len(selection)-1)]
            secondParent = selection[randint(0, len(selection)-1)]

            while firstParent == secondParent:
                secondParent = selection[randint(0, len(selection)-1)]

            offspring1,offspring2 = firstParent.crossover(secondParent)

            offspring1.mutate()
            offspring2.mutate()

            offspring1.fitness()
            offspring2.fitness()

            if offspring1.getFitness()>offspring2.getFitness():
                nextGen.addIndividual(offspring1)

            else:
                nextGen.addIndividual(offspring2)

        return nextGen

    def run(self, noIterations, populationSize,individualSize,seed):
        # args - list of parameters needed in order to run the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information need it for the satistics
        best = None
        avg = 0
        random.seed(seed)
        # return the results and the info for statistics
        population = self.__repository.createPopulation([populationSize,individualSize])
        for individual in population.getIndividuals():
            individual.fitness()

        self.__repository.add_population(population)
        for i in range(noIterations-1):
            nextGen = self.iteration(population)
            self.__repository.add_population(nextGen)
            avg = numpy.average(nextGen.getListOfFitness())
            best = nextGen.selection(1)[0]

        return best,avg

    def solver(self, populationSize,individualSize,noIterations,seeds):
        # args - list of parameters needed in order to run the solver
        bestIndivduals = []
        avgs = []
        start = time.time()
        for i in range(len(seeds)):
            best,avg = self.run(noIterations,populationSize,individualSize,seeds[i])
            bestIndivduals.append(best)
            avgs.append(avg)
        end = time.time()
        return end-start,avgs,bestIndivduals

    def randomMap(self):
        self.__repository.randomMap()

    def getMap(self):
        return self.__repository.getMap()
