from Hashi.bridge import *
from Hashi.display import *
import pygame
class Circle():
    def __init__(self, number, x, y, color):
        self.number = number
        self.bridges = list()
        self.x = x
        self.y = y
        self.r = 30
        self.color = color
        self.conections=0
        self.value=number
        self.neighbors_x = list()
        self.neighbors_y = list()
        self.neighbors = list()
        self.close_neighbors = list()
        self.visited = False
        self.is_done =False
        self.is_clicked = False

    def change_color(self, color):
        """
        This method change a color of button
        :param color: name of color
        :return:
        """
        self.color = color

    def show(self):
        pygame.draw.circle(gameDisplay,self.color, (self.x, self.y), 30, 0)
        textDisplay(str(self.number), 30, dark_violet, (self.x, self.y))



    def addBridge(self, secondCircle,value):
        self.conections+=value
        secondCircle.conections += value
        if(secondCircle.conections == secondCircle.value):
            secondCircle.is_done = True


    # def backlight(self,mouse):
    #     if (mouse[0] - self.x)**2 + (mouse[1]-self.y)**2 > self.r:
    #         self.change_color(red)
    #         self.show()

    def update(self,event):
        """
        This method update color of circle.  If it is clicked (event == MOUSEBUTTONDOWN) it changes color
        :param event: It is an event.
        :return:
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pos()[0] - self.x)**2 + (pygame.mouse.get_pos()[1]-self.y)**2 <= self.r**2:
                print("blee")
                self.is_clicked = True
                self.change_color(red)
                return self






