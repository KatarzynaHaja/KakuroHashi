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
            column = Column([100 + 40 * i, 60], [100 + 40 * i, 100], [140 + 40 * i, 100])
            self.columns[i] = column
            number_of_nodes = randint(2, 3)
            for j in range(0, number_of_nodes):
                if len(self.rows) <= j:
                    row = Column([60, 100 + 40*j], [100, 100 + 40 * j], [100, 140 + 40 * j])
                    self.rows[j] = row
                row = self.rows[j]
                available = [val for val in column.available_numbers if val in row.available_numbers]
                n = random.choice(available)
                node = column.add(n, 'v')
                row.add(node, 'h')
                if n in column.available_numbers:
                    column.available_numbers.remove(n)
                if n in row.available_numbers:
                    row.available_numbers.remove(n)

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
