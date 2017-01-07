from Hashi.bridge import *
from Hashi.display import *
import pygame
class Circle():
    def __init__(self, number, x, y):
        self.number = number
        self.bridges = list()
        self.x = x
        self.y = y
        self.r = 30
        self.conections=0
        self.value=0
        self.neighbors_x = list()
        self.neighbors_y = list()
        self.neighbors = list()
        self.close_neighbors = list()
        self.visited = False


    def show(self):
        pygame.draw.circle(gameDisplay, circle_violet, (self.x, self.y), 30, 0)
        textDisplay(str(self.number), 30, dark_violet, (self.x, self.y))

    def getEnd(self):  # skad linie mamy prowadzic
        return (self.x , self.y)

    def getStart(self):
        return (self.x , self.y)

    def set_value(self, value):
        self.value = value



    def addBridge(self, secondCircle,color):
        bridge = Bridge(self, secondCircle,color)
        self.bridges.append(bridge)
        self.conections+=1
        secondCircle.conections += 1
        bridge.show()


