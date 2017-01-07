from Kakuro.node import *
from Kakuro.SumOfColumn import *


class Column:
    def __init__(self, x, y, z, o):
        self.column = list()
        self.sum = SumOfColumn(x, y, z, 0, o)
        self.x = x
        self.y = y
        self.z = z
        self.count = 0
        self.available_numbers = list(range(1, 10))
        self.factors = list()
        self.current_factorisation = 0
        self.index_of_factorisation = 0

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

    def update(self, event):
        for c in self.column:
            c.update(event)

    def check(self):
        s = 0
        new_list = list()
        for c in self.column:
            s += int(c.number)
            new_list.append(int(c.number))
        set_list = set(new_list)
        set_list = list(set_list)
        if s == self.sum.number and sorted(set_list) == sorted(new_list):
            return True
        else:
            return False

    def is_filled(self):
        filled = True
        for c in self.column:
            if c.number == "":
                filled = False
        return filled
