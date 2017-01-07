import random
from pygame import font
from Kakuro.node import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.SumOfColumn import *
from Kakuro.Board import *
import copy


class Solver:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.list_of_all = list()
        self.count = 0

    def f(self, number, count):
        self.list_of_all = list()
        available_numbers = list(range(1, 10))
        self.count = count
        self.factor(number, count, 9, available_numbers)
        print("wyswietlam liste")
        for e in self.list_of_all:
            print(e)

    def factor(self, number, count, start, available_numbers):
        if count == 1:
            l = list()
            if number in available_numbers:
                available_numbers.remove(number)
                l.append(number)
            return l
        else:
            available_numbers_copy = copy.copy(available_numbers)
            l = list()
            lista = list()
            for i in reversed(available_numbers_copy):
                if i <= start and i <= number and i in available_numbers:
                    temp_number = number - i
                    a = copy.copy(available_numbers)
                    a.remove(i)
                    available_numbers.remove(i)
                    l = self.factor(temp_number, count - 1, temp_number, a)  #lista list
                    if l:
                        if count == 2:
                            l.append(i)
                            if len(l) == self.count:
                                self.list_of_all.append(l)
                        else:
                            for e in l:
                                e.append(i)
                                if len(e) == self.count:
                                    self.list_of_all.append(e)
                        if count != 2:
                            for e in l:
                                lista.append(e)
                        else:
                            lista.append(l)

        return lista


    def game(self):
        gameDisplay.fill(white)
        self.board.generate(4)
        for c in self.board.columns.values():
            print(c.sum.number)
            self.f(c.sum.number, len(c.column))
        for c in self.board.rows.values():
            print(c.sum.number)
            self.f(c.sum.number, len(c.column))
        while True:
            gameDisplay.fill(white)
            self.board.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
            clock.tick(60)

    def solve(self):
        self.game()


s = Solver()
s.solve()
