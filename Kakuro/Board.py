from Kakuro.Column import *
from Kakuro.Row import *
from random import randint
import random


class Board:
    def __init__(self):
        self.columns = dict()
        self.rows = dict()

    def generate(self):
        self.number_of_columns = randint(2,5)
        for i in range(0, self.number_of_columns + 1):
            kolumna = Column([100 + 40 * i, 60], [100 + 40 * i, 100], [140 + 40 * i, 100])
            self.columns[i] = kolumna
            number_of_nodes = randint(2, 3)
            for j in range(0, number_of_nodes):
                if len(self.rows) < number_of_nodes:
                    rzad = Column([60, 100 + 40*j], [100, 100 + 40 * j], [100, 140 + 40 * j])
                    self.rows[j] = rzad
                rzad = self.rows[j]
                available = [val for val in kolumna.available_numbers if val in rzad.available_numbers]
                n = random.choice(available)
                node = kolumna.add(n, 'v')
                rzad.add(node, 'h')
                if n in kolumna.available_numbers:
                    kolumna.available_numbers.remove(n)
                if n in rzad.available_numbers:
                    rzad.available_numbers.remove(n)

    def show(self):
        for kolumna in self.columns.values():
            kolumna.show()
        for row in self.rows.values():
            row.show()

    def update(self, event, surface):
        for kolumna in self.columns.values():
            kolumna.update(event, surface)

    def check(self):
        end = True
        for c in self.columns.values():
            if c.isFilled() == False:
                end = False
        for c in self.rows.values():
            if c.isFilled() == False:
                end = False
        if end == False:
            return("Nie wszystkie pola sa wypelnione")
        else:
            end = True
            for c in self.columns.values():
                if c.check() == False:
                    end = False
            for c in self.rows.values():
                if c.check() == False:
                    end = False
            if end:
                return("Wygrales")
            else:
                return("Blad")

