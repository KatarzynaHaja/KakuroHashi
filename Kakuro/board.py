from Kakuro.column import *
from random import randint
import random
from Kakuro.open_file import *


class Board:
    def __init__(self):
        self.columns = dict()
        self.rows = dict()
        self.number_of_columns = 0
        self.number_of_hints = 0
        self.empty = list()

    def generate_column(self, x, y, z, range_from, range_to, id_row, id_column):
        """
        Function generates one column
        :param x: first coordinate of column
        :param y: second coordinate of column
        :param z: third coordinate of column
        :param range_from: the smallest index of node in column
        :param range_to: the biggest index of node in column
        :param id_row: number of row where column begins
        :param id_column: number of column
        :return:
        """
        column = Column(x, y, z, "column")
        self.columns[(id_row, id_column)] = column
        for j in range(range_from, range_to):
            temp = id_column
            while (j, temp) not in self.rows.keys() and (j, temp) not in self.columns.keys() \
                    and temp != 0 and (j, temp) not in self.empty:
                temp -= 1
            if (j, temp) not in self.rows.keys():
                row = Column([60 + 40 * temp, 100 + 40 * (j - 1)], [100 + 40 * temp, 100 + 40 * (j - 1)],
                             [100 + 40 * temp, 140 + 40 * (j - 1)], "row")
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
        """
        Function generates board
        :param number_of_columns: number of columns that will be in a board
        :return:
        """
        self.number_of_columns = number_of_columns
        for i in range(1, self.number_of_columns + 1):
            if i % 2 == 1:
                number_of_nodes = randint(3, self.number_of_columns / 2 + 1)
                start = randint(0, self.number_of_columns / 2)
            for e in range(0, start):
                self.empty.append((e, i))
            self.generate_column([100 + 40 * (i - 1), 60 + start * 40], [100 + 40 * (i - 1), 100 + start * 40],
                                 [140 + 40 * (i - 1), 100 + start * 40], start + 1, number_of_nodes + start, start, i)
            new = self.number_of_columns - number_of_nodes - start - 1
            if new > 1:
                self.generate_column([100 + 40 * (i - 1), 60 + 40 * (number_of_nodes + start)],
                                     [100 + 40 * (i - 1), 100 + 40 * (number_of_nodes + start)],
                                     [140 + 40 * (i - 1), 100 + 40 * (number_of_nodes + start)],
                                     number_of_nodes + 1 + start, new + number_of_nodes + + start + 2,
                                     number_of_nodes + start, i)
            else:
                for j in range(number_of_nodes + start, self.number_of_columns + 1 + start):
                    self.empty.append((j, i))

    def hint(self):
        """
        Function chooses random node which is not written by user to show as a hint
        :return: text which is shown on the screen: message that user used all hints or empty when they did not
        """
        if self.number_of_hints == 3:
            return "Wykorzystano wszystkie podpowiedzi"
        else:
            self.number_of_hints += 1
            column = random.choice(list(self.columns.keys()))
            row = random.randint(0, len(self.columns[column].column) - 1)
            number_of_nodes = 0
            counter = 0
            for key in self.columns.keys():
                number_of_nodes += len(self.columns[key].column)
            while self.columns[column].column[row].number != "" and counter <= number_of_nodes:
                counter += 1
                column = random.choice(list(self.columns.keys()))
                row = random.randint(0, len(self.columns[column].column) - 1)
            self.columns[column].column[row].number = self.columns[column].column[row].hidden_number
            return ""

    def show(self):
        """
        Function displays board
        :return:
        """
        gameDisplay.fill(back_green)
        for column in self.columns.values():
            column.show()
        for row in self.rows.values():
            row.show()

    def update(self, event):
        """
        Functions update board due to event
        :param event: event sent by user
        :return:
        """
        for column in self.columns.values():
            column.update(event)

    def check(self):
        """
        Function checks if board is correctly filled
        :return: text which says that: not all nodes are filled or user won or user lost
        """
        end = True
        for c in self.columns.values():
            if c.is_filled() is False:
                end = False
        for c in self.rows.values():
            if c.is_filled() is False:
                end = False
        if end is False:
            return "Nie wszystkie pola są wypełnione"
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
                return "Błąd"

    def check_partial(self):
        """
        Function checks if board is filled correctly when not all nodes are filled
        :return: True or False
        """
        for key in self.rows.keys():
            if not self.rows[key].check_partial():
                return False
        return True

    def find_nearest_column(self, w, k):
        """
        Function finds key of nearest column of node
        :param w: number of row in which node is
        :param k: number of column in which node is
        :return: key of column
        """
        while (w, k) not in self.columns.keys() and w != 0:
            w -= 1
        if w == 0 and (w, k) not in self.columns.keys():
            return False
        return w, k

    def find_nearest_row(self, w, k):
        """
        Function finds key of nearest row of node
        :param w: number of row in which node is
        :param k: number of column in which node is
        :return: key of row
        """
        while (w, k) not in self.rows.keys() and k != 0:
            k -= 1
        if k == 0 and (w, k) not in self.rows.keys():
            return False
        return w, k

    def is_filled(self):
        """
        Function checks if any node is filled in board
        :return: True or False
        """
        for c in self.columns.values():
            for node in c.column:
                if node.number != "":
                    return True
        return False

    def create_board_from_file(self, path):
        """
        Functions creates board from text file
        :return:
        """
        with open(path) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip('\n')
                l = line.split(";")
                l = l[:-1]
                l = l[1::]
                counter_of_columns = 0
                digits = re.compile('\d')
                for elem in l:
                    if not bool(digits.search(elem)) and i != 0 and counter_of_columns != 0:
                        if self.find_nearest_column(i, counter_of_columns) and \
                                self.find_nearest_row(i, counter_of_columns):
                            (x, y) = self.find_nearest_column(i, counter_of_columns)
                            column = self.columns[(x, y)]
                            node = column.add(0, 'v')
                            row = self.rows[(self.find_nearest_row(i, counter_of_columns))]
                            row.add(node)
                    else:
                        j = 0
                        row_or_column = 0
                        while j < len(elem):
                            if elem[j] != 'x' and elem[j] != " ":
                                number = ""
                                while j < len(elem) and elem[j] != " ":
                                    number += elem[j]
                                    j += 1
                                if row_or_column == 0:
                                    column = Column([100 + 40 * counter_of_columns, 60 + 40 * i],
                                                    [100 + 40 * counter_of_columns, 100 + 40 * i],
                                                    [140 + 40 * counter_of_columns, 100 + 40 * i], "column",
                                                    int(number))
                                    self.columns[(i, counter_of_columns)] = column
                                else:
                                    column = Column([60 + 40 * (counter_of_columns + 1), 100 + 40 * (i - 1)],
                                                    [100 + 40 * (counter_of_columns + 1), 100 + 40 * (i - 1)],
                                                    [100 + 40 * (counter_of_columns + 1), 140 + 40 * (i - 1)],
                                                    "row", int(number))
                                    self.rows[(i, counter_of_columns)] = column
                            else:
                                j += 1
                                row_or_column += 1
                    counter_of_columns += 1
