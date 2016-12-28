from Kakuro.node import *
from Kakuro.Sum_of_column import *


class Column:
    def __init__(self, x, y, z):
        self.column = list()
        self.sum = Sum_of_column(x, y, z, 0)
        self.x = x
        self.y = y
        self.z = z
        self.count = 0
        self.available_numbers = list(range(1, 10))

    def add(self, number, direction):      # v - pionowy    h - poziomy
        if isinstance(number, int):
            if direction == 'v':
                node = Node(number, self.x[0], self.y[1] + self.count * 40)
            else:
                node = Node(number, self.x[0] + self.count * 40, self.y[1])
        else:
            node = number
        self.column.append(node)
        self.count += 1
        self.sum.update(node.hidden_number)
        return node

    def show(self):
        self.sum.show()
        for c in self.column:

               c.show()

    def update(self, event, surface):
        for c in self.column:
            c.update(event, surface)

    def check(self):
        s = 0
        newList = list()
        for c in self.column:
            s += int(c.number)
            newList.append(int(c.number))
        nnList = set(newList)
        nnList = list(nnList)
        if s == self.sum.number and sorted(nnList) == sorted(newList):
            return True
        else:
            return False

    def isFilled(self):
        filled = True
        for c in self.column:
            if c.number == "":
                filled = False
        return filled