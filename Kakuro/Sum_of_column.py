import pygame
from Kakuro.settings import *
from Kakuro.display import *

class Sum_of_column:
    def __init__(self, x, y, z, number):
        self.x = x
        self.y = y
        self.z = z
        self.number = number

    def show(self):
        pygame.draw.polygon(gameDisplay, black, [self.x, self.y, self.z], 1)
        t = textObject(str(self.number), 25, black)
        rect = t.get_rect()
        rect.center = (self.x[0] + (self.z[0] - self.x[0])/3, self.x[1] + 4*(self.y[1] - self.x[1]) / 5)
        gameDisplay.blit(t, rect)

