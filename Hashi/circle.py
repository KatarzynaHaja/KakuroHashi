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


    def show(self):
        pygame.draw.circle(gameDisplay, black, (self.x, self.y), 30, 1)
        textDisplay(str(self.number), 30, black, (self.x, self.y))

    def getEnd(self):  # skad linie mamy prowadzic
        return (self.x + self.r, self.y)

    def getStart(self):
        return (self.x - self.r, self.y)


    def addBridge(self, secondCircle):
        bridge = Bridge(self, secondCircle)
        self.bridges.append(bridge)
        bridge.show()




