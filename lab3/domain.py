# -*- coding: utf-8 -*-
import pickle
from random import *
from utils import *
import numpy as np


# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation

class gene:
    def __init__(self):
        self.dir = v[randint(0, 3)]

    def get_coord(self, x, y):
        return x + self.dir[0], y + self.dir[1]


class Individual:
    def __init__(self, map, size=0):
        self.__size = size
        self.__x = [gene() for i in range(self.__size)]
        self.__f = None
        self.__drone = Drone()
        self.__visited = []
        self.__map = map

    def getGenome(self):
        return self.__x

    def setGenome(self,x):
        self.__x = x

    def readUDMSensors(self, x, y):
        sum = 0
        # DOWN
        xaux = x + 1
        while self.__map.isValid(xaux, y):
            if (xaux, y) not in self.__visited:
                self.__visited.append((xaux, y))
                sum += 1
            xaux += 1
        # RIGHT
        yaux = y + 1
        while self.__map.isValid(x, yaux):
            if (x, yaux) not in self.__visited:
                self.__visited.append((x, yaux))
                sum += 1
            yaux += 1
        # UP
        xaux = x - 1
        while self.__map.isValid(xaux, y):
            if (xaux, y) not in self.__visited:
                self.__visited.append((xaux, y))
                sum += 1
            xaux -= 1
        # LEFT
        yaux = y - 1
        while self.__map.isValid(x, yaux):
            if (x, yaux) not in self.__visited:
                self.__visited.append((x, yaux))
                sum += 1
            yaux -= 1

        return sum

    def fitness(self):
        # compute the fitness for the individual
        # and save it in self.__f
        # f(x) = nr casute vazute - penalizare * nr_conflicte
        fitness = self.readUDMSensors(self.__drone.getX(), self.__drone.getY())
        for direction in self.__x:
            x, y = direction.get_coord(self.__drone.getX(), self.__drone.getY())
            self.__drone.makeMove(x, y)
            if self.__map.isValid(x, y):
                fitness += self.readUDMSensors(self.__drone.getX(), self.__drone.getY())
            else:
                fitness -= penalizare
            if self.__drone.getBattery == 0:
                break
        self.__f = fitness

    def mutate(self, mutateProbability=0.04):
        if random() < mutateProbability:
            index = randint(0, self.__size - 1)
            self.__x[index] = gene()

    def crossover(self, otherParent, crossoverProbability=0.8):
        offspring1, offspring2 = Individual(self.__map, self.__size), Individual(self.__map,
                                                                                               self.__size)
        if random() < crossoverProbability:
            index = randint(0, self.__size - 1)
            offspring1.setGenome(self.__x[:index] + otherParent.getGenome()[index:])
            offspring2.setGenome(otherParent.getGenome()[:index] + self.__x[index:])
        return offspring1, offspring2

    def getFitness(self):
        return self.__f

class Population():
    def __init__(self,map, populationSize=0, individualSize=0):
        self.__populationSize = populationSize
        self.__v = [Individual(map, individualSize) for x in range(populationSize)]

    def evaluate(self):
        # evaluates the population
        for x in self.__v:
            x.fitness()

    def selection(self, k=0):
        # perform a selection of k individuals from the population
        # and returns that selection
        return sorted(self.__v,key = lambda x: x.getFitness(),reverse=True)[:k]

    def getSize(self):
        return self.__populationSize

    def getIndividuals(self):
        return self.__v

    def addIndividual(self,individual):
        self.__v.append(individual)
        self.__populationSize+=1

    def getListOfFitness(self):
        fitness = []
        for individual in self.__v:
            fitness.append(individual.getFitness())
        return fitness

class Map():
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        self.surface = np.zeros((self.n, self.m))
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            f.close()

    def saveMap(self, file):
        with open(file, "wb") as f:
            pickle.dump(self, f)
            f.close()

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def isValid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and self.surface[x][y] != 1


class Drone:
    def __init__(self, x=3, y=3, battery=5):
        self.__x = x
        self.__y = y
        self.__battery = battery

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getBattery(self):
        return self.__battery

    def makeMove(self, x, y):
        self.__x = x
        self.__y = y
        self.__battery -= 1
