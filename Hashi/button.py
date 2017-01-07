import pygame
from Hashi.settings import *
from Hashi.display import *


class Button:
    def __init__(self,xleft, yleft, width, height, color, text, sizeOfLetters,i):
        self.x = xleft
        self.y = yleft
        self.w = width
        self.h = height
        self.color = color
        self.text = text
        self.size = sizeOfLetters
        self.is_cliked = False
        self.position = i

    def show(self):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        self.positionOfText = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        textDisplay(self.text, self.size, dark_violet, self.positionOfText)

    def changeColor(self,color):
        self.color = color

    def backlight(self, mouse):
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.changeColor(bright_violet)
            self.show()

    def isClicked(self, mouse):
        if pygame.event.peek(pygame.MOUSEBUTTONDOWN) and self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.event.clear()
            return True
        else:
            return False