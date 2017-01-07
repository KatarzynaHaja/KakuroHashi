import random
from pygame import font
from Kakuro.node import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.SumOfColumn import *
from Kakuro.Board import *
import copy
import operator


class Solver:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.list_of_all = list()
        self.count = 0
        self.number_of_possibilities_columns = dict()
        self.number_of_possibilities_rows = dict()

    def factorise(self, number, count):
        self.list_of_all = list()
        available_numbers = list(range(1, 10))
        self.count = count
        self.factor(number, count, 9, available_numbers)
        print("wyswietlam liste")
        for i in range(0, len(self.list_of_all)):
            self.list_of_all[i] = list(reversed(self.list_of_all[i]))
        print(self.list_of_all)
        return self.list_of_all

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

    def funkcja(self, column, nrpodzialu, nrskladnika, ind):

        column.current_factorisation = column.factors[nrpodzialu]
        print("obecny rozklad")
        print(column.current_factorisation)
        index = ind
        print("dlugosc kolumn", len(column.column))
        while index <= len(column.column):
            print("nr podzialu", nrpodzialu, "nrskladnika", nrskladnika)
            print(column.current_factorisation)
            factor = column.current_factorisation[nrskladnika]
            print("factor", factor)
            row = self.board.rows[(index, 0)]
            print(row.sum.number)
            i = 0
            while i < len(row.factors) and factor not in row.factors[i]:
                print("nie znaleziono", factor, "w", row.factors[i])
                i += 1

            if i == len(row.factors):
                if nrskladnika + 1 >= len(column.current_factorisation):
                    if index != 1:
                        row = self.board.rows[(index - 1, 0)]
                        print(row.factors)
                        print("dodaje", column.column[index - 1].number)
                        row.current_factorisation.append(column.column[index - 1].number)
                        print(row.current_factorisation)
                    index = self.funkcja(column, nrpodzialu + 1, 0, index - 1)
                else:
                    index = self.funkcja(column, nrpodzialu, nrskladnika + 1, index)
            else:
                row.current_factorisation = row.factors[i]
                row.index_of_factorisation = i
                print("rozklad wiersza", row.current_factorisation)
                column.column[index - 1].number = factor
                index += 1
                column.current_factorisation.remove(factor)
                row.current_factorisation.remove(factor)
                if nrskladnika + 1 == len(column.column):
                    nrskladnika -= 1

        return index

    def funkcja2(self, column, nrpodzialu, nrskladnika, ind):
        index = ind
        if nrpodzialu >= len(column.factors):
            print("Zle")
            return 1000000
        else:
            while index <= len(column.column):
                row = self.board.rows[(index, 0)]
                print("faktoryzacja wiersza", row.current_factorisation)
                factor = row.current_factorisation[0]
                i = 0
                while i < len(column.factors) and factor not in column.factors[i]:
                    i += 1
                if i == len(column.factors):
                    if nrskladnika + 1 >= len(row.current_factorisation):
                        index = self.funkcja2(column, nrpodzialu + 1, nrskladnika, index)
                    else:
                        index = self.funkcja2(column, nrpodzialu, nrskladnika + 1, index)
                else:
                    column.current_factorisation = column.factors[i]
                    print("rozklad kolumny", column.current_factorisation)
                    column.column[index - 1].number = factor
                    index += 1
                    column.current_factorisation.remove(factor)
                    row.current_factorisation.remove(factor)
        return index

    def game(self):
        gameDisplay.fill(white)
        self.board.generate(2)
        for c in self.board.columns.keys():
            value = self.board.columns[c]
            print(value.sum.number)
            value.factors = self.factorise(value.sum.number, len(value.column))
            self.number_of_possibilities_columns[c] = len(value.factors)
        self.number_of_possibilities_columns = sorted(self.number_of_possibilities_columns.items(),
                                                      key=operator.itemgetter(1))
        #print(self.number_of_possibilities_columns)
        for c in self.board.rows.keys():
            value = self.board.rows[c]
            print(value.sum.number)
            value.factors = self.factorise(value.sum.number, len(value.column))
            self.number_of_possibilities_rows[c] = len(value.factors)
        self.number_of_possibilities_rows = sorted(self.number_of_possibilities_rows.items(),
                                                   key=operator.itemgetter(1))

        column = self.board.columns[(0, 1)]
        self.funkcja(column, 0, 0, 1)
        index = 1
        print("druga kolumna")
        column = self.board.columns[(0, 2)]
        self.funkcja2(column, 0, 0, 1)

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
