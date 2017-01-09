from Kakuro.column import *
from random import randint
import random
import math


class Board:
    def __init__(self):
        self.columns = dict()
        self.rows = dict()
        self.number_of_columns = 0
        self.number_of_hints = 0
        self.empty = list()

    def generate_column(self, x, y, z, range_from, range_to, id_row, id_column):
        column = Column(x, y, z, "column")
        self.columns[(id_row, id_column)] = column
        for j in range(range_from, range_to):
            temp = id_column
            while (j, temp) not in self.rows.keys() and (j, temp) not in self.columns.keys() and temp != 0 and \
                            (j, temp) not in self.empty:
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

    def generate(self, number_of_columns):
        self.number_of_columns = number_of_columns
        for i in range(1, self.number_of_columns + 1):
            if i % 2 == 1:
                number_of_nodes = randint(3, self.number_of_columns + 1)
            self.generate_column([100 + 40 * (i-1), 60], [100 + 40 * (i-1), 100], [140 + 40 * (i-1), 100], 1,
                                 number_of_nodes, 0, i)
            new = self.number_of_columns - number_of_nodes
            if new > 1:
                self.generate_column([100 + 40 * (i-1), 60 + 40 * number_of_nodes],
                            [100 + 40 * (i-1), 100 + 40 * number_of_nodes],
                            [140 + 40 * (i-1), 100 + 40 * number_of_nodes], number_of_nodes + 1,
                            new + number_of_nodes + 1, number_of_nodes, i)
            else:
                for j in range(number_of_nodes, self.number_of_columns + 1):
                    self.empty.append((j, i))

    def hint(self):
        if self.number_of_hints == 3:
            return "Wykorzystano wszystkie podpowiedzi"
        else:
            self.number_of_hints += 1
            column = random.choice(list(self.columns.keys()))
            row = random.randint(0, len(self.columns[column].column)-1)
            while self.columns[column].column[row].number != "":
                column = random.choice(list(self.columns.keys()))
                row = random.randint(0, len(self.columns[column].column) - 1)
            self.columns[column].column[row].number = self.columns[column].column[row].hidden_number
            return ""

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
                return "Wygrana"
            else:
                return "Blad"

    def create_board_from_file(self):
        with open('text_files/1.txt') as file:
            lines = file.readlines()
            print(lines)
            for i, line in enumerate(lines):
                print(i)
                line = line.strip('\n')
                l = line.split("\t")
                print(l)
                counter_of_columns = 0
                for elem in l:
                    k = 0
                    while k < len(elem) - 1:
                        if elem[k] != " ":
                            if elem[k] != 'x' and elem[k] != 'P' and elem[k+1] != 'x' and elem[k+1] != 'P':
                                number = ""
                                while k < len(elem) and elem[k] != " ":
                                    number += elem[k]
                                    k += 1
                                print(number, "numer")
                                print("tworze kolumne")
                                column = Column([100 + 40 * counter_of_columns, 60 + 40 * i],
                                                [100 + 40 * counter_of_columns, 100 + 40 * i],
                                                [140 + 40 * counter_of_columns, 100 + 40 * i], "column")
                                print(i, counter_of_columns, "o takim kluczu")
                                self.columns[(i, counter_of_columns)] = column
                                counter_of_columns += 1
                               
                        k += 1
                print(self.columns)


b = Board()
b.create_board_from_file()


