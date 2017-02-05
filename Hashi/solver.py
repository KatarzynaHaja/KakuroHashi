from Hashi.bridge import *
import itertools
from Hashi.circle import *


def ready(l):
    """
    This function returns list of active neighbours.
    Active neigbour is when we can connect circle with it
    :param l: list of circle
    :return: ready circle
    """
    active = list()
    for i in l:
        if i.conections < i.value:
            active.append(i)
    return active


def sort_circle(l):
    """
    Sorting circle. Keys are number of neighbours and value - connection
    :param l: list of circle
    :return: list of circle
    """
    list_circle = sorted(l, key=lambda circle: (len(ready(circle.close_neighbors)), circle.value - circle.conections))
    return list_circle


class Solver:
    def __init__(self):
        self.list_bridge = list()
        self.list_circles = list()

    def find_possible_bridges(self, circle):
        """
        This function looks for possible combination of connections
        :param circle: one circle
        :return:
        """
        combinations = list()
        list_one_neighbor = list()
        list_more_neighbor = list()
        for i in circle.close_neighbors:
            if i.value == 1:
                list_one_neighbor.append(i)
            else:
                list_more_neighbor.append(i)
            print(circle.value - circle.conections)
            combinations = list(
                itertools.combinations_with_replacement(ready(circle.close_neighbors),
                                                        circle.value - circle.conections))

        bad = list()
        for i in combinations:
            for j in i:
                if j.value - j.conections == 1:
                    if i.count(j) > 1:
                        bad.append(i)
                        break

                if i.count(j) > 2:
                    bad.append(i)
                    break
        for i in combinations:
            if i not in bad:
                circle.combinations.append(i)

    def is_in(self, source, dest):
        """
        This function says if bridge is in list. It check 2 circles
        :param source: source circle
        :param dest: end circle
        :return: tuple (is it in list , index of this element)
        """
        for b in self.list_bridge:
            if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
                return True, int(self.list_bridge.index(b))

        return False, 0

    def remove_bridge(self, index):
        """
        This function removes bridge
        :param index: index of removing bridge
        :return:
        """
        number = self.list_bridge[index].number
        print(self.list_bridge[index].circle1.conections, "przed kólko 1")
        print(self.list_bridge[index].circle1.conections, "przed kólko 2")
        self.list_bridge[index].circle1.conections -= number
        self.list_bridge[index].circle2.conections -= number
        print(self.list_bridge[index].circle1.conections, "po kólko 1")
        print(self.list_bridge[index].circle2.conections, "po kólko 2")
        self.list_bridge.remove(self.list_bridge[index])

    def remove_all(self, source, dest):
        """
        This function says if we should remove bridge.
        We can remove bridges if we have 2 bridges between circles.
        :param source: source circle
        :param dest: end circle
        :return: tuple ( can we remove bridge, index of bridge)
        """
        for b in self.list_bridge:
            if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
                self.remove_bridge(self.list_bridge.index(b))

    def solve(self, circles):
        """
        Solver
        :param circles: list of circle
        :return: list of bridge
        """
        print("wchodze do solvera")
        self.list_circles = circles
        print("tyle jest kulek", len(self.list_circles))
        self.list_circles = sort_circle(self.list_circles)
        self.recursion(0)
        for i in self.list_bridge:
            print("mosty", i.number)
        for i in self.list_circles:
            print(i.x, i.y)
        return self.list_bridge

    def recursion(self, index):
        """
        Recursion which solves board
        :param index: index of circle
        :return: logical value
        """
        is_ok = False

        if index < len(self.list_circles):
            circle = self.list_circles[index]
            self.find_possible_bridges(circle)
            print("kulka wartość", circle.value)
            active = ready(circle.close_neighbors)
            print("aktywni", len(active))
            for i in active:
                print(i.value)

            if circle.conections == circle.value:
                return self.recursion(index + 1)

            elif len(active) > 0:
                j = 0
                while not is_ok and j < len(circle.combinations):
                    if all(i in active for i in circle.combinations[j]):
                        print("dodaje mosty")

                        for z in circle.combinations[j]:
                            is_in_list = self.is_in(circle, z)
                            print("robie most miedzy ", circle, z)
                            if is_in_list[0]:
                                print("już mamy jeden most")
                                self.remove_bridge(is_in_list[1])
                                self.list_bridge.append(Bridge(circle, z, violet, 2))
                                circle.add_bridge(z, 2)
                            else:
                                print("to jest pierwszy most miedzy ", circle, z)
                                self.list_bridge.append(Bridge(circle, z, violet, 1))
                                circle.add_bridge(z, 1)
                        is_ok = self.recursion(index + 1)
                        if not is_ok:
                            for z in circle.combinations[j]:
                                self.remove_all(circle, z)

                    j += 1
                return is_ok
            else:
                return False

        return True
