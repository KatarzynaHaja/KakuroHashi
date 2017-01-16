from Hashi.randomize import Randomize
from Hashi.board import Board
import random



class Game():
    def __init__(self, s):
        self.level = self.set_level(s)
        self.randomize = Randomize(self.level)
        self.number_of_circle = self.randomize.set_number_of_circle()
        self.number_of_bridge = self.randomize.random_brigde()
        self.board = Board(self.number_of_bridge, self.number_of_circle)
        self.number_of_hints = 0

    def set_level(self, s):
        if s == 'easy':
            return 0
        if s == 'midi':
            return 1
        if s == 'hard':
            return 2

    def random_bridge(self):
        n = random.choice(self.board.list_bridge)
        return n

    def is_finished(l):
        finished = False
        for i in l:
            if i.connections == i.value:
                finished = True
            else:
                return False
        if finished is True:
            return True
