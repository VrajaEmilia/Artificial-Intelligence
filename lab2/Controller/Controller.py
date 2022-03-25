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
    def ManhattanDist(x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)


    def searchAStar(self,initialX, initialY, finalX, finalY):
        # TODO
        #implement the search function and put it in controller
        #returns a list of moves as a list of pairs [x,y]

        if not self.__drone.isValid(self.__map,finalX,finalY):
            return None

        found = False
        visited = []
        prev = {}
        prev[(initialX,initialY)] =(None,None)
        toVisit = [(initialX,initialY)]
        steps = {}
        steps[(initialX, initialY)] = 0

        while len(toVisit)!=0 and not found:
            (x,y) = toVisit.pop(0)
            visited.append((x,y))
            if (x,y) == (finalX,finalY):
                found = True
            else:
                aux = []
                for d in directions:
                    nextX = x + d[0]
                    nextY = y + d[1]
                    if self.__drone.isValid(self.__map, nextX, nextY) and (nextX, nextY) not in visited:
                        if (nextX,nextY) not in toVisit:
                            aux.append((nextX, nextY))
                            prev[(nextX, nextY)] = (x, y)
                            steps[(nextX, nextY)]= steps[(x, y)] + 1
                        else:
                            if steps[(nextX, nextY)] > steps[(x,y)] + 1:
                                toVisit.remove((nextX, nextY))
                                aux.append((nextX, nextY))
                                prev[(nextX, nextY)] = (x, y)
                                steps[(nextX, nextY)] = steps[(x, y)] + 1

                toVisit = toVisit+aux
                toVisit.sort(key=lambda coord: self.ManhattanDist(coord[0], coord[1], finalX, finalY)+steps[coord])
        if found:
            return self.path(prev, finalX, finalY)
        else:
            return None

    def searchGreedy(self,initialX, initialY, finalX, finalY):
        # TODO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        if not self.__drone.isValid(self.__map,finalX,finalY):
            return None

        found = False
        visited = []
        prev = {}
        prev[(initialX, initialY)] = (None, None)
        toVisit = [(initialX, initialY)]
        while len(toVisit)!=0 and not found:
            (x, y) = toVisit.pop(0)
            visited.append((x, y))
            if (x, y) == (finalX, finalY):
                found = True
            else:
                aux = []
                for d in directions:
                    nextX = x + d[0]
                    nextY = y + d[1]
                    if self.__drone.isValid(self.__map, nextX,nextY) and (nextX, nextY) not in visited:
                        aux.append((nextX, nextY))
                        prev[(nextX, nextY)] = (x, y)
                toVisit.extend(aux)
                toVisit.sort(key=lambda coord: self.ManhattanDist(coord[0], coord[1], finalX, finalY))
                #print(toVisit)
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




