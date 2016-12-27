from Kakuro.Column import *
from Kakuro.Row import *


class Board:
    def __init__(self):
        self.columns = list()

    def add(self):
        kolumna = Column([100, 60], [100, 100], [140, 100])
        kolumna.add(1)
        kolumna.add(2)
        self.columns.append(kolumna)

    def show(self):
        for kolumna in self.columns:
            kolumna.show()

    def update(self, event, surface):
        for kolumna in self.columns:
            kolumna.update(event, surface)

    def check(self):
        end = True
        for c in self.columns:
            if c.isFilled() == False:
                end = False
        if end==False:
            return("Nie wszystkie pola sa wypelnione")
        else:
            end = True
            for c in self.columns:
                if c.check() == False:
                    end = False
            if end:
                return("Wygrales")
            else:
                return("Blad")

