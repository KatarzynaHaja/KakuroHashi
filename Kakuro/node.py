import pygame
from Kakuro.display import *


class Node:
    def __init__(self, number, left, top):
        self.hidden_number = number
        self.number = ""
        self.font = pygame.font.SysFont('Arial', 15)
        self.color = (0, 0, 0)
        self.left = left
        self.top = top
        self.height = 40
        self.width = 40
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.selected = False
        self.list_of_numbers = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5,
                                pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9}

    def show(self):
        if self.selected:
            pygame.draw.rect(gameDisplay, self.color, self.rect, 2)
        else:
            pygame.draw.rect(gameDisplay, self.color, self.rect, 1)
        t = text_object(str(self.hidden_number), 25, self.color)
        rect = t.get_rect()
        rect.center = (self.left + (self.width/2), self.top + (self.height/2))
        gameDisplay.blit(t, rect)

    def add_number(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.number = ""
        elif event.key in self.list_of_numbers.keys():
            self.number = self.list_of_numbers[event.key]

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if self.selected:
                self.add_number(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.selected = True
                else:
                    self.selected = False
