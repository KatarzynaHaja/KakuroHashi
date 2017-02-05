from Hashi.display import *
import pygame


class Circle:
    def __init__(self, number, x, y, color):
        """

        :param number: number of bridges
        :param x: position x
        :param y: position y
        :param color: color of circle
        """
        self.number = number
        self.x = x
        self.y = y
        self.r = 30
        self.color = color
        self.conections = 0
        self.value = number
        self.neighbors_x = list()
        self.neighbors_y = list()
        self.neighbors = list()
        self.close_neighbors = list()
        self.visited = False
        self.is_done = False
        self.is_clicked = False
        self.combinations = list()

    def change_color(self, color):
        """
        This method change a color of button
        :param color: name of color
        :return:
        """
        self.color = color

    def show(self):
        """
        This method show circle
        :return:
        """
        pygame.draw.circle(game_display, self.color, (self.x, self.y), 30, 0)
        if self.number ==1:
            text_display(str(self.number), 30, c1, (self.x, self.y))
        if self.number == 2:
            text_display(str(self.number), 30, c2, (self.x, self.y))
        if self.number == 3:
            text_display(str(self.number), 30, c3, (self.x, self.y))
        if self.number == 4:
            text_display(str(self.number), 30, c4, (self.x, self.y))
        if self.number == 5:
            text_display(str(self.number), 30, c5, (self.x, self.y))
        if self.number == 6:
            text_display(str(self.number), 30, c6, (self.x, self.y))
        if self.number == 7:
            text_display(str(self.number), 30, c7, (self.x, self.y))
        if self.number == 8:
            text_display(str(self.number), 30, c8, (self.x, self.y))
        if self.number == 9:
            text_display(str(self.number), 30, c9, (self.x, self.y))


    def add_bridge(self, second_circle, value):
        """
        This function add bridges and updates number of connections in each circle. It also set is_done if circle
        has all bridges
        :param second_circle: destination of bridge
        :param value: how many bridges connect 2 circles
        """
        self.conections += value
        second_circle.conections += value
        if second_circle.conections == second_circle.value:
            second_circle.is_done = True

    def update(self, event):
        """
        This method update color of circle.  If it is clicked (event == MOUSEBUTTONDOWN) it changes color
        :param event: It is an event.
        :return:circle which is clicked
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] - self.x) ** 2 + (pygame.mouse.get_pos()[1] - self.y) ** 2 <= self.r ** 2:
                self.is_clicked = True
                self.change_color(max_circle)
                return self

    def update_color(self):
        """
        It updates color when circle has all bridges
        """
        if self.conections == self.value:
            self.change_color(max_circle)
