import pygame
from Kakuro.settings import *
from Kakuro.display import *


class SumOfColumn:
    def __init__(self, x, y, z, number, orientation):
        self.x = x
        self.y = y
        self.z = z
        self.number = number
        self.orientation = orientation

    def show(self):
        pygame.draw.polygon(gameDisplay, black, [self.x, self.y, self.z], 1)
        t = text_object(str(self.number), 25, black)
        rect = t.get_rect()
        if self.orientation == 'column':
            rect.center = (self.x[0] + (self.z[0] - self.x[0])/3, self.x[1] + 4*(self.y[1] - self.x[1]) / 5)
        else:
            rect.center = (self.y[0] - (self.y[0] - self.x[0])/3, self.x[1] + 3*(self.z[1] - self.x[1]) / 10)
        gameDisplay.blit(t, rect)

    def update(self, number):
        self.number += number
