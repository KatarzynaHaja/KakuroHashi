import random
class Game():
    def __init__(self):
        self.numberOfCircle = self.selectCircle()

    def selectCircle(self):
        value = random.randint(2,5)
        return value

g = Game()
print(g.numberOfCircle)