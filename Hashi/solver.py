from Hashi.circle import Circle
from Hashi.settings import *
from Hashi.bridge import Bridge
import copy
from Hashi.game import *

from operator import attrgetter


class Solver():
    def __init__(self, g):
        self.list_of_bridge = list()


def is_finished(l):
    finished = False
    for i in l:
        if i.conections == i.value:
            finished = True
        else:
            return False
    if finished is True:
        return True

def diff(x,y):
    return x-y

def sort_circle(l):
    list_circle = sorted(l, key=lambda circle: (circle.value - circle.conections, len(ready(circle.close_neighbors))))
    return list_circle


def ready(l):
    ready = list()
    for i in l:
        if i.is_done is False:
            ready.append(i)
    return ready


def solver(circles):
     list_of_bridge = list()
     tmp = copy.deepcopy(circles)
     while is_finished(circles) == False:
        circles = sort_circle(circles)
        for circle in circles:
                print(circle.value,"to jest wartosc")
                diff = circle.value - circle.conections
                print("roznica przed",diff)
                if diff == len(ready(circle.close_neighbors)):
                    for j in range(diff):
                        circle.addBridge(ready(circle.close_neighbors)[j],1)
                        list_of_bridge.append(Bridge(circle,ready(circle.close_neighbors)[j], violet, 1))
                    print("tyle samo sasiadow co wartosc")
                    diff = circle.value - circle.conections
                    if diff ==0:
                        print("juz nie mozna")
                        circle.is_done =True
                    continue
                if diff%2==0 and diff*2 == len(ready(circle.close_neighbors)):
                    for j in range(diff):
                        circle.addBridge(ready(circle.close_neighbors)[j],2)
                        list_of_bridge.append(Bridge(circle,ready(circle.close_neighbors)[j], violet, 2))
                    print("podwojne mosty")
                    diff = circle.value - circle.conections
                    if diff == 0:
                        print("juz nie mozna")
                        circle.is_done = True
                if len(ready(circle.close_neighbors))== 1:
                    circle.addBridge(ready(circle.close_neighbors)[0],diff)
                    list_of_bridge.append(Bridge(circle,ready(circle.close_neighbors)[0], violet, diff))
                    print("tylko jedne sasiad")
                    diff = circle.value - circle.conections
                    if diff == 0:
                        print("juz nie mozna")
                        circle.is_done = True
                # if (dif % len(circles[i].close_neighbors) != 0):
                #     pass
        return list_of_bridge
