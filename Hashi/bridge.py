import pygame
from Hashi.display import *
class Bridge():
    def __init__(self, fromCircle, toCircle):
        self.circle1 = fromCircle
        self.circle2 = toCircle

    def show(self):
        pygame.draw.line(gameDisplay, black, self.circle1.getEnd(), self.circle2.getStart())

