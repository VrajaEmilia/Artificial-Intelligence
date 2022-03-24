import pygame

from Domain.const import *

class Controller:
    def __init__(self,drone,map):
        self.__drone = drone
        self.__map = map

    def getDrone(self):
        return self.__drone

    def getMap(self):
        return self.__map

    @staticmethod
    def heuristicF(x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def searchAStar(self,mapM, droneD, initialX, initialY, finalX, finalY):
        # TODO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]

        pass

    def searchGreedy(self,initialX, initialY, finalX, finalY):
        # TODO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        found = False
        visited = []
        prev = {}
        prev[(initialX, initialY)] = (None, None)
        toVisit = [(initialX, initialY)]
        while toVisit and not found:
            (x, y) = toVisit.pop(0)
            visited.append((x, y))
            if (x, y) == (finalX, finalY):
                found = True
            else:
                aux = []
                for d in directions:
                    if self.__drone.isValid(self.__map, x + d[0], y + d[1]) and (x + d[0], y + d[1]) not in visited:
                        aux.append((x + d[0], y + d[1]))
                        prev[(x + d[0], y + d[1])] = (x, y)
                toVisit.extend(aux)
                # toVisit.sort(lambda coord: heuristicF(coord[0], coord[1], finalX, finalY))
                # toVisit = sorted(toVisit, lambda coord: heuristicF(coord[0],coord[1],finalX,finalY))
                toVisit.sort(key=lambda coord: self.heuristicF(coord[0], coord[1], finalX, finalY))
        if found:
            return self.path(prev, finalX, finalY)
        else:
            return None

    def path(self,prev, finalX, finalY):
        path = [(finalX, finalY)]
        (x, y) = prev[(finalX, finalY)]
        while (x, y) != (None, None):
            path.append((x, y))
            (x, y) = prev[(x, y)]
        path.reverse()
        return path

    @staticmethod
    def dummysearch():
        # example of some path in test1.map from [5,7] to [7,11]
        return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]

    def displayWithPath(self,image, path):
        mark = pygame.Surface((20, 20))
        mark.fill(GREEN)
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))

        return image




