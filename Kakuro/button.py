import pygame
from Kakuro.settings import *
from Kakuro.display import *


class Buttton:
    def __init__(self, xleft, yleft, w, h, color, text, size_of_letters):
        """
        :param xleft: coordinate of left
        :param yleft:
        :param w:
        :param h:
        :param color:
        :param text:
        :param size_of_letters:
        """
        self.x = xleft
        self.y = yleft
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.size = size_of_letters
        self.positionOfText = 0

    def show(self):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        self.positionOfText = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        text_display(self.text, self.size, black, self.positionOfText)

    def change_color(self, color):
        self.color = color

    def backlight(self, mouse):
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.change_color(highlight_green)
            self.show()
            return True
        else:
            return False

    def is_clicked(self, mouse):
        if pygame.event.peek(pygame.MOUSEBUTTONDOWN)and self.x + self.w > mouse[0] > self.x \
                and self.y + self.h > mouse[1] > self.y:
            pygame.event.clear()
            return True
        else:
            return False
