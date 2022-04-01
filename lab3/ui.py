# -*- coding: utf-8 -*-


# imports
from gui import *
from controller import *
from repository import *
from domain import *


# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATENTION! the function doesn't check if the path passes trough walls
def menu():
    print("\nCommands:")
    print(" 0. exit\n"
          "Map:\n"
          " 1. create random map\n"
          " 2. load a map\n"
          " 3. save a map\n"
          " 4. visualise map\n"
          "EA:\n"
          " 4. parameters setup\n"
          " 5. run the solver\n"
          " 6. visualise the statistics\n"
          " 7. view the drone moving on a path\n")


def main():
    while True:
        menu()
        try:
            opt = int(input(">>>"))
            if opt == 0:
                return
            if opt < 0 or opt > 7:
                print("Non existent command")
        except:
            print("Invalid command")


if __name__ == "__main__":
    main()