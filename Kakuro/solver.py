import random
from pygame import font
from Kakuro.node import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.sumofcolumn import *
from Kakuro.board import *
import copy
import operator
import itertools


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
        list1 = copy.copy(self.list_of_all)
        self.list_of_all = list()
        print(list1)
        for elem in list1:
            for permutation in itertools.permutations(elem):
                self.list_of_all.append(list(permutation))
        print("lista wszystkiego")
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

    def all(self):
        gameDisplay.fill(white)
        self.board.generate(4)
        self.big_list = list()
        for c in self.board.columns.keys():
            value = self.board.columns[c]
            print(value.sum.number)
            value.factors = self.factorise(value.sum.number, len(value.column))
            self.big_list.append(value.factors)
            #self.number_of_possibilities_columns[c] = len(value.factors)
        for c in self.board.rows.keys():
            value = self.board.rows[c]
            print(value.sum.number)
            value.factors = self.factorise(value.sum.number, len(value.column))
            #self.number_of_possibilities_rows[c] = len(value.factors)
        print("alo")
        lista = [self.board.columns[x].factors for x in self.board.columns.keys()]
        #self.all = list(itertools.product(*[self.board.columns[x].factors for x in self.board.columns.keys()]))
        #print("sciapana")
        #print(self.all)
        #print("tyle jest kombinacji", len(self.all))
        while True:
            gameDisplay.fill(white)
            self.board.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            index = 0
            for e in self.gen(lista):
                print(e)
                if self.board.check() != "Wygrana":
                    column_counter = 0
                    for key in self.board.columns.keys():
                        column = self.board.columns[key]
                        for i in range(0, len(column.column)):
                            #column.column[i].number = self.all[index][column_counter][i]
                            column.column[i].number = e[column_counter][i]
                        column_counter += 1
                    index += 1
                    print(index)
                else:
                    print("znaleziono")
                    break
            print("wyszlam")

            pygame.display.update()
            clock.tick(60)

    def a(self):
        print(list(itertools.product([[1,2],[3,4]],[[5],[6,7]])))

    def gen(self, lista):
        for e in list(itertools.product(*lista)):
            yield e

    def p(self, *args):
        pools = [tuple(pool) for pool in args]
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
            print(result)
        #for prod in result:
            #print(tuple(prod))

    def test(self):
        self.p('ABC','xyz')
        print("halo")




s = Solver()
#s.solve()
s.test()
