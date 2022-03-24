from Controller.Controller import Controller
from Domain.Drone import Drone
from Domain.Map import Map
from View.GUI import GUI

if __name__ == "__main__":
    # call the main function
    d = Drone(0,0)
    m = Map()
    cntrl = Controller(d,m)
    gui = GUI(cntrl)
    gui.main()