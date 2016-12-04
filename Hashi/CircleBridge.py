
import pygame
import sys
import random



pygame.init()

size = width, height = 800, 500
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def textObject(text, size, color):
    font = pygame.font.Font(None, size)
    textSurface = font.render(text, True, color)
    return textSurface


def textDisplay(text, size, color, position):
    t = textObject(text, size, color)
    rect = t.get_rect()
    rect.center = position
    gameDisplay.blit(t, rect)

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

    def addBridge(self, secondCircle):
        bridge = Bridge(self, secondCircle)
        self.bridges.append(bridge)
        bridge.show()

    def getEnd(self):  # skad linie mamy prowadzic
        return (self.x + self.r, self.y)

    def getStart(self):
        return (self.x - self.r, self.y)


class Bridge():
    def __init__(self, fromCircle, toCircle):
        self.circle1 = fromCircle
        self.circle2 = toCircle

    def show(self):
        pygame.draw.line(gameDisplay, black, self.circle1.getEnd(), self.circle2.getStart())


c = Circle(10, 100, 100)
c.show()
c2 = Circle(2, 200, 100)
c2.show()
c.addBridge(c2)
