# -*- coding: utf-8 -*-


# imports
import traceback


from gui import *
from controller import *
from repository import *
from domain import *
import matplotlib.pyplot as plt

seeds = [60, 40, 81, 60, 39, 7, 48, 80, 76, 62, 20, 51, 6, 4, 64, 95, 27, 91, 71, 75, 98, 45, 79, 55, 24, 72, 79, 23, 37, 63, 23, 78, 15, 64, 6, 33, 97, 41, 75, 14, 15, 75, 11, 90, 66, 71, 18, 2, 45, 55, 36, 47, 46, 79, 60, 16, 83, 91, 30, 50, 76, 85, 30, 51, 95, 39, 10, 94, 9, 86, 31, 77, 44, 95, 73, 34, 80, 63, 35, 88, 27, 40, 64, 47, 28, 62, 69, 12, 74, 37, 16, 67, 9, 40, 84, 89, 97, 82, 100, 18]
populationSize=10
individualSize=6
noIterations=30

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
        self.__avgs = []

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

    @staticmethod
    def dummy_path():
        return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]

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
        individualSize = int(input("individual size="))
        populationSize = int(input("population size="))
        noIterations = int(input("no of iterations="))

    def statistics(self):
        plt.plot(self.__avgs)
        plt.ylabel('stats')
        plt.show()

    def solver(self):
        exec_time, self.__avgs, best=self.__controller.solver(populationSize, individualSize, noIterations, seeds)
        print(exec_time,self.__avgs,numpy.std(self.__avgs))

    def drone_moving_on_path(self):
        movingDrone(self.__controller.getMap(), self.dummy_path())


def main():
    cntrl = controller()
    ui = UI(cntrl)
    while True:
        ui.print_menu()
        try:
            opt = int(input(">>>"))
            if opt == 0:
                return
            elif opt < 0 or opt > 8:
                print("Non existent command")
            elif 0 <= opt <= 7:
                ui.commands[opt]()
        except ValueError:
            traceback.print_exc()
            print("Invalid command")


if __name__ == "__main__":
    main()
