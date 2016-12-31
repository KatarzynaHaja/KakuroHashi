from Kakuro.Column import *
from random import randint
import random


class Board:
    def __init__(self):
        self.columns = dict()
        self.rows = dict()
        self.number_of_columns = 0

    def generate(self):
        self.number_of_columns = randint(2, 4)
        for i in range(0, self.number_of_columns):
            column = Column([100 + 40 * i, 60], [100 + 40 * i, 100], [140 + 40 * i, 100], "column")
            self.columns[(0, i)] = column
            number_of_nodes = randint(2, 3)
            for j in range(0, number_of_nodes):
                if len(self.rows) <= j:
                    row = Column([60, 100 + 40*j], [100, 100 + 40 * j], [100, 140 + 40 * j], "row")
                    self.rows[(j, 0)] = row
                row = self.rows[(j, 0)]
                available = [val for val in column.available_numbers if val in row.available_numbers]
                n = random.choice(available)
                node = column.add(n, 'v')
                row.add(node, 'h')
                if n in column.available_numbers:
                    column.available_numbers.remove(n)
                if n in row.available_numbers:
                    row.available_numbers.remove(n)

    def generate_column(self, x, y, z, range_from, range_to, id_row, id_column):
        column = Column(x, y, z, "column")
        self.columns[(id_row, id_column)] = column
        for j in range(range_from, range_to):
            temp = id_column
            while (j, temp) not in self.rows.keys() and (j, temp) not in self.columns.keys() and temp != 0:
                temp -= 1
            if (j, temp) not in self.rows.keys():
                row = Column([60 + 40 * temp, 100 + 40 * (j-1)], [100 + 40 * temp, 100 + 40 * (j-1)],
                             [100 + 40 * temp, 140 + 40 * (j-1)], "row")
                self.rows[(j, temp)] = row
            row = self.rows[(j, temp)]
            available = [val for val in column.available_numbers if val in row.available_numbers]
            n = random.choice(available)
            node = column.add(n, 'v')
            row.add(node, 'h')
            if n in column.available_numbers:
                column.available_numbers.remove(n)
            if n in row.available_numbers:
                row.available_numbers.remove(n)

    def generate2(self):
        self.number_of_columns = 8
        for i in range(1, self.number_of_columns + 1):
            if i % 2 == 1:
                number_of_nodes = randint(3, 5)
            self.generate_column([100 + 40 * (i-1), 60], [100 + 40 * (i-1), 100], [140 + 40 * (i-1), 100], 1,
                                 number_of_nodes, 0, i)
            new = 7 - number_of_nodes
            self.generate_column([100 + 40 * (i-1), 60 + 40 * number_of_nodes],
                             [100 + 40 * (i-1), 100 + 40 * number_of_nodes],
                             [140 + 40 * (i-1), 100 + 40 * number_of_nodes], number_of_nodes + 1,
                                 new + number_of_nodes + 1, number_of_nodes, i)

    def hint(self):
        pass

    def show(self):
        for column in self.columns.values():
            column.show()
        for row in self.rows.values():
            row.show()

    def update(self, event):
        for column in self.columns.values():
            column.update(event)

    def check(self):
        end = True
        for c in self.columns.values():
            if c.is_filled() is False:
                end = False
        for c in self.rows.values():
            if c.is_filled() is False:
                end = False
        if end is False:
            return "Nie wszystkie pola sa wypelnione"
        else:
            end = True
            for c in self.columns.values():
                if c.check() is False:
                    end = False
            for c in self.rows.values():
                if c.check() is False:
                    end = False
            if end:
                return "Wygrales"
            else:
                return "Blad"
