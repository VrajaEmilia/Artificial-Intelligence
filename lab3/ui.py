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
class UI:
    def __init__(self, controller):
        self.commands = {
            1: self.create_random_map,
            2: self.load_map,
            3: self.save_map,
            4: self.visualise_map,
            5: self.parameters_setup,
            6: self.solver,
            7: self.statistics,
            8: self.drone_moving_on_path
        }
        self.__controller = controller

    @staticmethod
    def print_menu():
        print("\nCommands:")
        print(" 0. exit\n"
              "Map:\n"
              " 1. create random map\n"
              " 2. load a map\n"
              " 3. save a map\n"
              " 4. visualise map\n"
              "EA:\n"
              " 5. parameters setup\n"
              " 6. run the solver\n"
              " 7. visualise the statistics\n"
              " 8. view the drone moving on a path\n")

    def create_random_map(self):
        self.__controller.randomMap()
        print("Random map generated")

    def load_map(self):
        file = input("please enter the file path:")
        self.__controller.getMap().loadMap(file)
        print("Map loaded")

    def save_map(self):
        file = input("file for saving the map:")
        self.__controller.getMap().saveMap(file)
        print("Map saved to file")

    def visualise_map(self):
        visualiseMap(self.__controller.getMap())

    def parameters_setup(self):
        pass

    def statistics(self):
        pass

    def solver(self):
        pass

    def drone_moving_on_path(self):
        pass


def main():
    cntrl = controller("args")
    ui = UI(cntrl)
    while True:
        ui.print_menu()
        try:
            opt = int(input(">>>"))
            if opt == 0:
                return
            elif opt < 0 or opt > 7:
                print("Non existent command")
            elif 0 <= opt <= 7:
                ui.commands[opt]()
        except ValueError:
            print("Invalid command")


if __name__ == "__main__":
    main()
