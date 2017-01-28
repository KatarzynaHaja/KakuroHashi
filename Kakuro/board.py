from Kakuro.column import *
from random import randint
import random


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

    def check_partial(self):
        print("jestem w bordzie")
        for key in self.rows.keys():
            for c in self.rows[key].column:
                print( c.number )
                #print("dlugosc", len(c))
            print("rzad", key)
            if not self.rows[key].check_partial():
                print("zle")
                return False
        return True

    def find_nearest_column(self, w, k):
        while (w, k) not in self.columns.keys() and w != 0:
            w -= 1
        if w == 0 and (w, k) not in self.columns.keys():
            return False
        return w, k

    def find_nearest_row(self, w, k):
        while (w, k) not in self.rows.keys() and k != 0:
            k -= 1
        if k == 0 and (w, k) not in self.rows.keys():
            return False
        return w, k

    def create_board_from_file(self):
        with open('text_files/2.txt') as file:
            lines = file.readlines()
            #print(lines)
            for i, line in enumerate(lines):
                print(i)
                line = line.strip('\n')
                l = line.split(";")
                print(l)
                counter_of_columns = 0
                for elem in l:
                    print("elem", elem)
                    if "P" in elem:
                        print("node")
                        print("najblizsza kolumna",self.find_nearest_column(i, counter_of_columns))
                        print("najblizszy wiersz", self.find_nearest_row(i, counter_of_columns))
                        (x, y) = self.find_nearest_column(i, counter_of_columns)
                        column = self.columns[(x, y)]
                        node = column.add(0, 'v')
                        row = self.rows[(self.find_nearest_row(i, counter_of_columns))]
                        row.add(node)

                    elif elem != "":
                        j = 0
                        row_or_column = 0
                        while j < len(elem):
                            if elem[j] != 'x' and elem[j] != " ":
                                number = ""
                                while j < len(elem) and elem[j] != " ":
                                    number += elem[j]
                                    j += 1
                                print(number, "numer")
                                print("row or column", row_or_column)
                                if row_or_column == 0:
                                    print("alo1")
                                    column = Column([100 + 40 * counter_of_columns, 60 + 40 * i],
                                        [100 + 40 * counter_of_columns, 100 + 40 * i],
                                        [140 + 40 * counter_of_columns, 100 + 40 * i], "column", int(number))
                                    self.columns[(i, counter_of_columns)] = column
                                else:
                                    print("alo2")
                                    column = Column([60 + 40 * (counter_of_columns +1), 100 + 40 * (i-1)], [100 + 40 * (counter_of_columns+1), 100 + 40 * (i-1)],
                                        [100 + 40 * (counter_of_columns+1), 140 + 40 * (i-1)], "row", int(number))
                                    print(i, counter_of_columns, "o takim kluczu")
                                    self.rows[(i, counter_of_columns)] = column

                            else:
                                j += 1
                                row_or_column += 1
                                print("row or column", row_or_column)
                    counter_of_columns += 1





