from Kakuro.board import *
import copy
import itertools


class Solver:
    def __init__(self, board):
        self.board = board
        self.count = 0
        self.number_of_possibilities_columns = dict()
        self.number_of_possibilities_rows = dict()
        self.list_of_all = list()

    def factorise(self, number, count):
        """
        Function makes a list of all factorisations with permutations
        :param number: number which we want to factorise
        :param count: number of factors on which we want to factorise
        :return:
        """
        self.list_of_all = list()
        available_numbers = list(range(1, 10))
        self.count = count
        self.factor(number, count, 9, available_numbers)
        print("wyswietlam liste")
        list1 = copy.copy(self.list_of_all)
        print(list1)
        for elem in list1:
            for permutation in itertools.permutations(elem):
                if list(permutation) != elem:
                    self.list_of_all.append(list(permutation))
        print("lista wszystkiego")
        self.list_of_all
        print(self.list_of_all)
        return

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

    def solve(self):
        """
        Function
        :return:
        """
        print("dzialam")
        for c in self.board.columns.keys():
            value = self.board.columns[c]
            self.factorise(value.sum.number, len(value.column))
            value.factors = self.list_of_all
        list_of_columns = [x for x in self.board.columns.keys()]
        print(list_of_columns)
        self.recursion(list_of_columns)
        print("koniec")

    def recursion(self, l):
        """
        Recursive function which fills board with next possible values
        :param l: list of columns which are not filled
        :return: True - if current solution is correct
                 False - if current solution is not correct
        """
        if l:
            index = 0
            while index < len(self.board.columns[l[0]].factors):
                column = self.board.columns[l[0]]
                print("jestem w kolumnie ", l[0], "i wpisuje liczby")
                for i in range(0, len(column.column)):
                    column.column[i].number = self.board.columns[l[0]].factors[index][i]
                print("ududu")
                for i in range(0, len(column.column)):
                    print(self.board.columns[l[0]].column[i].number)
                if self.board.check_partial():
                    if self.recursion(l[1::]):
                        return True
                print("NIEEE")
                index += 1
            if index == len(self.board.columns[l[0]].factors):
                for i in range(0, len(column.column)):
                    column.column[i].number = ""
                return False
        else:
            return True
