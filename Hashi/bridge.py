import pygame
from Hashi.display import *
class Bridge():
    def __init__(self, fromCircle, toCircle , color,value):
        self.circle1 = fromCircle
        self.circle2 = toCircle
        self.color = color
        self.number = value

    def show(self):
        if self.circle1.x  == self.circle2.x:
            if self.circle1.y > self.circle2.y:
                pygame.draw.line(gameDisplay, self.color,(self.circle1.x, self.circle1.y - self.circle1.r), (self.circle2.x , self.circle2.y + self.circle2.r))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x, self.circle2.y - self.circle2.r),(self.circle1.x, self.circle1.y + self.circle1.r))
        if self.circle1.y == self.circle2.y:
            if self.circle1.x > self.circle2.x:
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y),(self.circle2.x + self.circle2.r, self.circle2.y))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y),(self.circle1.x + self.circle1.r, self.circle1.y))


    def show_more(self):
            if self.circle1.x == self.circle2.x:
                if self.circle1.y > self.circle2.y:
                    pygame.draw.line(gameDisplay, self.color, (self.circle1.x-10, self.circle1.y - self.circle1.r),
                                     (self.circle2.x - 10, self.circle2.y + self.circle2.r))
                    pygame.draw.line(gameDisplay, self.color, (self.circle1.x + 10, self.circle1.y - self.circle1.r),
                                     (self.circle2.x + 10, self.circle2.y + self.circle2.r))
                else:
                    pygame.draw.line(gameDisplay, self.color, (self.circle2.x - 10, self.circle2.y - self.circle2.r),
                                     (self.circle1.x - 10, self.circle1.y + self.circle1.r))
                    pygame.draw.line(gameDisplay, self.color, (self.circle2.x + 10, self.circle2.y - self.circle2.r),
                                     (self.circle1.x + 10, self.circle1.y + self.circle1.r))
            if self.circle1.y == self.circle2.y:
                if self.circle1.x > self.circle2.x:
                    pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y - 10),
                                     (self.circle2.x + self.circle2.r, self.circle2.y - 10))
                    pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y + 10),
                                     (self.circle2.x + self.circle2.r, self.circle2.y + 10))
                else:
                    pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y - 10),
                                     (self.circle1.x + self.circle1.r, self.circle1.y - 10))
                    pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y +10),
                                     (self.circle1.x + self.circle1.r, self.circle1.y +10))




