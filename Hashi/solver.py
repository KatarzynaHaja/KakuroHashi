import copy
from Hashi.game import *

from operator import attrgetter


class Solver():
    def __init__(self):
        self.list_of_bridge = list()


def diff(x, y):
    return x - y


def sort_circle(l):
    list_circle = sorted(l, key=lambda circle: (len(ready(circle.close_neighbors)), circle.value - circle.conections))
    return list_circle


def sort_value(l):
    list_circle = sorted(l, key=lambda circle: (-len(ready(circle.close_neighbors)), circle.value - circle.conections),
                         reverse=True)
    return list_circle


def ready(l):
    ready = list()
    for i in l:
        if i.is_done is False:
            ready.append(i)
    return ready


def clear_all(l):
    for i in l:
        i.is_done = False
        i.conections = 0


def solver(circles):
    list_of_bridge = list()
    tmp = copy.deepcopy(circles)
    iter = 0
    j = 0
    while len(ready(circles)) > 0:
        circle = sort_circle(ready(circles))
        print("tyle mamy kulek", len(circle))
        print(circle[j].value, "to jest wartosc")
        diff = circle[j].value - circle[j].conections
        if diff < 0:
            break
        if diff == 0:
            circle[j].is_done = True
            print("juz polaczone")
            # j+=1

        print("roznica przed", diff)
        if len(ready(circle[j].close_neighbors)) == 0:
            print("!!!!BRAK SASIADOW!!!!")
            clear_all(circles)
            list_of_bridge.clear()
            print(len(list_of_bridge))
            print(len(ready(circles)))
            iter += 1

        if (diff > 0 and diff % len(ready(circle[j].close_neighbors)) != 0):
            print("WESZLO DO MODULO")
            z = 0
            if iter == 0:
                while (diff > 0):
                    if (diff > 1 and (sort_value(ready(circle[j].close_neighbors))[z].value -
                                          sort_value(ready(circle[j].close_neighbors))[z].conections) >= 2):
                        list_of_bridge.append(
                            Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 2))
                        circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 2)
                        diff -= 2
                    else:
                        list_of_bridge.append(
                            Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 1))
                        circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 1)

                        diff -= 1
                    z += 1
            if iter == 1:
                if diff == 1:
                    list_of_bridge.append(
                        Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z + 1], violet, 1))
                    circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z + 1], 1)
            if diff <= 0:
                print("juz nie mozna")
                circle[j].is_done = True

        if diff > 0 and diff == len(ready(circle[j].close_neighbors)):
            z = 0
            if iter == 0:
                while (diff > 0):
                    if diff > 1 and sort_value(ready(circle[j].close_neighbors))[z].value - \
                            sort_value(ready(circle[j].close_neighbors))[z].conections >= 2:
                        list_of_bridge.append(
                            Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 2))
                        circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 2)
                        diff -= 2
                    else:
                        list_of_bridge.append(
                            Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 1))
                        circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 1)

                        diff -= 1
                    z += 1
            if iter == 1:
                for i in range(len(ready(circle[j].close_neighbors))):
                    list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[i], violet, 1))
                    circle[j].add_bridge((ready(circle[j].close_neighbors))[i], 1)

            print("tyle samo sasiadow co wartosc")
            if diff <= 0:
                print("juz nie mozna")
                circle[j].is_done = True
        if diff > 0 and diff % 2 == 0 and diff == len(ready(circle[j].close_neighbors)) * 2:
            for z in range(len(ready(circle[j].close_neighbors))):
                list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[z], violet, 2))
                circle[j].add_bridge(ready(circle[j].close_neighbors)[z], 2)

            print("podwojne mosty")
            diff = circle[j].value - circle[j].conections
            if diff <= 0:
                print("juz nie mozna")
                circle[j].is_done = True
        if diff > 0 and len(ready(circle[j].close_neighbors)) == 1:
            list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[0], violet, diff))
            circle[j].add_bridge(ready(circle[j].close_neighbors)[0], diff)

            print("tylko jedne sasiad")
            diff = circle[j].value - circle[j].conections
            if diff <= 0:
                print("juz nie mozna")
                circle[j].is_done = True

    return list_of_bridge
