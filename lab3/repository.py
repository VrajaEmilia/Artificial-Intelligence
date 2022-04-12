# -*- coding: utf-8 -*-

import pickle
from domain import *


class repository():
    def __init__(self):
        self.__populations = []
        self.cmap = Map()

    def createPopulation(self, args):
        # args = [populationSize, individualSize] -- you can add more args    
        return Population(self.cmap,args[0], args[1])

    def add_population(self, population):
        self.__populations.append(population)

    def getMap(self):
        return self.cmap

    # TO DO : add the other components for the repository:
    #    load and save from file, etc

    def randomMap(self):
        self.cmap.randomMap()
