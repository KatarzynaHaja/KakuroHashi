import random
from Hashi.circle import *


class Game():
    def __init__(self):
        self.number_of_circle = self.random_circle()
        self.list_circle = list()
        self.list_bridge = list()

    def random_circle(self):
        value = random.randint(2, 5)
        return value

    def random_brigde(self):
        value = random.randint(1, 5)
        return value

    def generate_board(self):
        z=2
        for i in range(self.number_of_circle):
            if i%2 == 0:
                self.list_circle.append(Circle(0, 100+100*i, 100))
            else:
                self.list_circle.append(Circle(0, 100, 100+i*100))
            self.list_circle[i].show()

    def is_finished(self):
        finished=False
        for i in self.list_circle:
            if i.connections == i.value:
                finished = True
            else:
                return False
        if finished == True:
            return True




