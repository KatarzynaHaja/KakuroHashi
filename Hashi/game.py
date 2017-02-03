from Hashi.randomize import Randomize
from Hashi.board import Board
from Hashi.bridge import *
from Hashi.settings import *


def set_level(s):
    """
    It sets level of game
    :param s: level as string
    :return: level
    """
    if s == 'easy':
        return 0
    if s == 'midi':
        return 1
    if s == 'hard':
        return 2


def is_finished(l):
    """
    It checks if game is finished
    :param l: list of circles
    :return: True when all circles have all bridges, False if not
    """
    finished = False
    for i in l:
        if i.conections == i.value:
            finished = True
        else:
            return False
    if finished is True:
        return True


class Game:
    def __init__(self, s='easy'):
        """
        :param s:level , defalut is easy
        """
        self.level = set_level(s)
        self.randomize = Randomize(self.level)
        self.number_of_circle = self.randomize.random_circle()
        self.board = Board(self.number_of_circle)
        self.number_of_hints = 0


def is_in(l, source, dest):
    """
    This function says if bridge is in list. It check 2 circles
    :param l: list of bridges
    :param source: source circle
    :param dest: end circle
    :return: tuple (is it in list , index of this element)
    """
    for b in l:
        if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
            return True, int(l.index(b))

    return False, 0


def if_remove(l, source, dest):
    """
    This function says if we should remove bridge.
    We can remove bridges if we have 2 bridges between circles.
    :param l: list of bridges
    :param source: source circle
    :param dest: end circle
    :return: tuple ( can we remove bridge, index of bridge)
    """
    for b in l:
        if ((b.circle1 == source and b.circle2 == dest) or (
                        b.circle1 == dest and b.circle2 == source)) and b.number == 2:
            return True, int(l.index(b))

    return False, 0


def check(z, g):
    """
    This function allows to add bridge and remove bridge by user.
    Algorihtm:
        1)If we haven't got any bridge we can add one
        2) if we have one bridge we can add sencond.
           This function change value of bridge and method of showing
        3) If we have 2 bridges we can remove all if we clicked third time
    :param z: list of events
    :param g: game
    """
    if len(z) == 2:
        if z[0] in z[1].close_neighbors:
            w = is_in(g.board.user_list_bridge, z[0], z[1])
            s = if_remove(g.board.user_list_bridge, z[0], z[1])
            if s[0]:
                g.board.user_list_bridge.remove(g.board.user_list_bridge[s[1]])
                z[0].conections -= 2
                z[1].conections -= 2
            elif w[0]:
                g.board.user_list_bridge.remove(g.board.user_list_bridge[w[1]])
                z[0].conections -= 1
                z[1].conections -= 1
                g.board.user_list_bridge.append(Bridge(z[0], z[1], violet, 2))
                z[0].add_bridge(z[1], 2)
            elif w[0] is False:
                g.board.user_list_bridge.append(Bridge(z[0], z[1], violet, 1))
                z[0].add_bridge(z[1], 1)

            print(len(g.board.user_list_bridge))

        z[0].change_color(circle_violet)
        z[1].change_color(circle_violet)
        z.clear()


def clear_bridges(l):
    """
    This method clear all bridges and additionally updates number of connections
    :param l: list of bridge
    """
    for i in l:
        if i.number == 2:
            i.circle1.conections -= 2
            i.circle2.conections -= 2
        if i.number == 1:
            i.circle1.conections -= 1
            i.circle2.conections -= 1


def show_solution(l):
    """
    This update number of connections when user clicks show solution
    :param l: list of circle
    :return:
    """
    for i in l:
        i.conections = i.value


def print_bridge(l):
    """
    This function shows bridges.
    :param l: list of bridge
    """
    for i in range(len(l)):
        if l[i].number == 1:
            l[i].show()
        if l[i].number == 2:
            l[i].show_more()
