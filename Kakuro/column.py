from Kakuro.node import *
from Kakuro.sumofcolumn import *


class Column:
    def __init__(self, x, y, z, o, number=0):
        """
        :param x: first coordinate
        :param y: second coordinate
        :param z: third coordinate
        :param o: orientation can be 'column' or 'row'
        :param number: the sum of the column, default 0
        """
        self.column = list()
        self.sum = SumOfColumn(x, y, z, number, o)
        self.x = x
        self.y = y
        self.z = z
        self.count = 0
        self.available_numbers = list(range(1, 10))
        self.factors = list()
        self.current_factorisation = 0
        self.index_of_factorisation = 0

    def add(self, number, direction='v'):      # v - pionowy    h - poziomy
        """
        Function creates node (if it does not exists) and add to the column
        :param number: number (then node is created) or node
        :param direction:
        :return: added node
        """
        if isinstance(number, int):
            print(number)
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
        """
        Function displays column
        :return:
        """
        self.sum.show()
        for c in self.column:
            c.show()

    def update(self, event):
        """
        Function updates column
        :param event: event sent by user
        :return:
        """
        for c in self.column:
            c.update(event)

    def check(self):
        """
        Function checks if column is filled correctly
        :return: True or False
        """
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

    def check_partial(self):
        """
        Function checks if column if filled correctly when not all nodes are filled
        :return: True or False
        """
        s = 0
        new_list = list()
        for c in self.column:
            if c.number != "":
                s += int(c.number)
                new_list.append(int(c.number))
        set_list = set(new_list)
        set_list = list(set_list)
        print(set_list)
        print(sorted(new_list))
        if s <= self.sum.number and sorted(set_list) == sorted(new_list):
            return True
        else:
            return False

    def is_filled(self):
        """
        Function checks if all nodes are filled
        :return: True or False
        """
        filled = True
        for c in self.column:
            if c.number == "":
                filled = False
        return filled
