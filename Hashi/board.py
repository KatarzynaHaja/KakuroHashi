import random
from operator import attrgetter
from Hashi.bridge import Bridge
from Hashi.recognize import *
from Hashi.solver import solver
import copy


def sort_circle(l, key):
    """
    :param l: list which should be sorted
    :param key: which value is key of sorting
    :return:list of sorted circle
    """
    list_circle = sorted(l, key=attrgetter(key))
    return list_circle


class Board:
    def __init__(self, number_of_circle):
        """
        :param: how many bridges
        :param number_of_circle: how many circles are on the board
        """
        self.board = list()
        self.list_circle = list()
        self.list_bridge = list()
        self.possible = list()
        self.number_of_circle = number_of_circle
        self.recognition = list()
        self.user_list_bridge = list()

    def generate_by_recognition(self):
        """
        This function generate board from file by recognition circles and numbers from file
        :return: list of circles with numbers
        """
        self.recognition = which_file()
        self.list_circle = copy.deepcopy(self.recognition)

    def generate_default_board(self):
        """
        This is generation of default board which has size : 600x500 and it arranges circle
        every 100 pixels
        :return:list of default circle
        """
        for i in range(5):
            for j in range(6):
                self.board.append(Circle(0, j * 100 + 50, i * 100 + 50, circle_violet))
        return self.board

    def generate_board(self):
        """
        This function shows board on the screen
        :return: Board on the screen
        """
        for i in self.list_circle:
            i = Circle(i.value, i.x, i.y, i.color)
            i.show()

    def solve(self):
        """
        This function sets user's bridges. Those bridges are from solver.
        It is enable only when user clicked solver
        :return: list of user's bridges
        """
        self.user_list_bridge = solver(self.list_circle)

    def random_board(self):
        """
        This function chooses circle from list of default circles.
        Algorithm:
           number_of_circle : how many circle we should random
        1) We choose one circle from default list (n)
        2) For every circle in this list we check if it has equal x or y
           If  yes we add this to possible list.
           If not we continue
        3) From possible list we choose another point and it is lasting until
           i != number_of_circle
        :return:list of drawn circles
        """
        n = random.choice(self.board)
        self.list_circle.append(n)
        for i in range(1, self.number_of_circle):
            for j in range(len(self.board)):
                if (self.board[j].x == n.x or self.board[j].y == n.y) and self.board[j] not in self.possible and \
                                self.board[j] not in self.list_circle:
                    self.possible.append(self.board[j])
            n = random.choice(self.possible)
            self.list_circle.append(n)
            self.possible.remove(n)

        return self.list_circle

    def set_neighbors(self):
        """
        This function set neighbours of circle.
        Neighbour is when it has the same x or the same y.
        It recognize neighbours_x and neighbours_y.
        :return: it sets 2 list : neighbors_x, neighbors_y
        """
        for i in range(len(self.list_circle)):
            for j in range(len(self.list_circle)):
                if self.list_circle[i].x == self.list_circle[j].x:
                    self.list_circle[i].neighbors_x.append(self.list_circle[j])
                if self.list_circle[i].y == self.list_circle[j].y:
                    self.list_circle[i].neighbors_y.append(self.list_circle[j])

    def set_close_neighbors(self):
        """
        This function set close neighbours of circle. Close neighbors is when circle has neighbour on the left or on the
        right but this neighbour cannot be behind another one which is also a neighbour of our circle
        :return: List of close neighbour of circle for each circle in our list
        """

        for i in range(len(self.list_circle)):
            sorted_y = sort_circle(self.list_circle[i].neighbors_x, 'y')
            sorted_x = sort_circle(self.list_circle[i].neighbors_y, 'x')

            for j in range(0, len(self.list_circle[i].neighbors_x)):
                index_y = sorted_y.index(self.list_circle[i])
                if sorted_y.index(self.list_circle[i].neighbors_x[j]) == index_y - 1 or sorted_y.index(
                        self.list_circle[i].neighbors_x[j]) == index_y + 1:
                    self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_x[j])

            for j in range(0, len(self.list_circle[i].neighbors_y)):
                index_x = sorted_x.index(self.list_circle[i])
                if sorted_x.index(self.list_circle[i].neighbors_y[j]) == index_x - 1 or sorted_x.index(
                        self.list_circle[i].neighbors_y[j]) == index_x + 1:
                    self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_y[j])

    def set_bridges(self):
        """
        This function random number of bridges between each pair of circle in our list
        We can have 0,1 or 2 bridges but there isn't case when a circle hasn't go any bridge
        :return: set bridges
        """
        for i in range(len(self.list_circle)):
            self.list_circle[i].visited = True
            for j in range(len(self.list_circle[i].close_neighbors)):
                if self.list_circle[i].close_neighbors[j].visited is False:
                    if len(self.list_circle[i].close_neighbors) == 1:
                        value = random.randint(1, 2)
                    else:
                        value = random.randint(0, 2)
                    self.list_circle[i].value += value
                    self.list_circle[i].close_neighbors[j].value += value
                    self.list_bridge.append(
                        Bridge(self.list_circle[i], self.list_circle[i].close_neighbors[j], violet, value))
            if self.list_circle[i].value == 0:
                for z in range(len(self.list_circle[i].close_neighbors)):
                    value = random.randint(1, 2)
                    self.list_circle[i].value += value
                    self.list_circle[i].close_neighbors[z].value += value
                    self.list_bridge.append(
                        Bridge(self.list_circle[i], self.list_circle[i].close_neighbors[z], violet, value))

    def update(self, event):
        """
        It waits and update if circle is clicked
        :param event: event from user
        :return: it returns circle if event is MOUSEBUTTONDOWN
        """
        for circle in self.list_circle:
            z = circle.update(event)
            circle.update_color()
            if z is not None:
                return z
