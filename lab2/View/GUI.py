import time
from random import randint
import pygame
from Domain.const import *


class GUI:
    def __init__(self, controller):
        self.__cntrl = controller

    def main(self):
        self.__cntrl.getMap().loadMap("resources/test1.map")

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("resources/logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Path in simple environment")

        # we position the drone somewhere in the area
        x = randint(0, 19)
        y = randint(0, 19)

        # create drona
        self.__cntrl.getDrone().setX(x)
        self.__cntrl.getDrone().setY(y)

        # create a surface on screen that has the size of 400 x 480
        screen = pygame.display.set_mode((400, 400))
        screen.fill(WHITE)

        # define a variable to control the main loop
        running = True
        finalX = randint(0, 19)
        finalY = randint(0, 19)

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

            screen.blit(self.__cntrl.getDrone().mapWithDrone(self.__cntrl.getMap().image()), (0, 0))
            pygame.display.flip()
        start = time.time()
        path = self.__cntrl.searchGreedy(x, y, finalX, finalY)
        end = time.time()
        print("path from (", x, y, ") to (", finalX, finalY, ") :")
        if path:
            print(path)
        else:
            print("NO PATH")
        print("exec time:", end - start)
        screen.blit(self.__cntrl.displayWithPath(self.__cntrl.getMap().image(RED), path), (0, 0))
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()
