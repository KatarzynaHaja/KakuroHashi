import pygame
from Kakuro.display import *

class Node:
    def __init__(self, number, left, top):
        self.hidden_number = number
        self.number = ""
        self.font = pygame.font.SysFont('Arial', 15)
        self.color = (0,0,0)
        self.left = left
        self.top = top
        self.height = 40
        self.width = 40
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def show(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 1)
        t = textObject(str(self.number), 20, self.color)
        rect = t.get_rect()
        rect.center = (self.left + (self.width/2), self.top + (self.height/2))
        gameDisplay.blit(t, rect)

    def add_number(self, event):
        char = event.unicode
        if char:  # stop emtpy space for shift key adding to list
            self.str_list.append(char)

    def is_selected(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return True
            else:
                    return False







