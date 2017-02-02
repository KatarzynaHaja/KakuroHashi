import random


class Randomize:
    def __init__(self, level):
        """
        :param level: level
        """
        self.level = level

    def random_circle(self):
        """
        This method random number of circle. Number depends on level which was chosen by user
        :return: number of circle
        """
        value = 0
        if self.level == 0:
            value = random.randint(4, 6)
        if self.level == 1:
            value = random.randint(7, 15)
        if self.level == 2:
            value = random.randint(11, 15)
        return value
