import random


class Randomize():
    def __init__(self, level):
        self.level = level

    def random_circle(self):
        if self.level == 0:
            value = random.randint(4, 8)
        if self.level == 1:
            value = random.randint(9, 14)
        if self.level == 2:
            value = random.randint(15, 20)
        return value

    def set_number_of_circle(self):
        value = self.random_circle()
        return value

    def random_brigde(self):
        value = random.randint(0, 2)
        return value
