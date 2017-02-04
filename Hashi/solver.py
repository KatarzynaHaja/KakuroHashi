import copy
from Hashi.bridge import *
import itertools
from Hashi.circle import *


def ready(l):
    ready = list()
    for i in l:
        if i.conections!=i.value:
            ready.append(i)
    return ready


def sort_circle(l):
    list_circle = sorted(l, key=lambda circle: (len(ready(circle.close_neighbors)), circle.value - circle.conections))
    return list_circle


class Solver:
    def __init__(self):
        self.list_bridge = list()
        self.list_circles = list()


    def diff(x, y):
        return x - y




    def sort_value(l):
        list_circle = sorted(l, key=lambda circle: (-len(ready(circle.close_neighbors)), circle.value - circle.conections),
                             reverse=True)
        return list_circle




    def clear_all(l):
        for i in l:
            i.is_done = False
            i.conections = 0



    def find_possible_bridges(self,circle):
        list_one_neighbor = list()
        list_more_neighbor = list()
        for i in circle.close_neighbors:
            if i.value == 1:
                list_one_neighbor.append(i)
            else:
                list_more_neighbor.append(i)
        combinations = list(itertools.combinations_with_replacement(circle.close_neighbors,circle.value - circle.conections))
        bad = list()
        for i in combinations:
            for j in i:
                if j.value == 1:
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
        :param l: list of bridges
        :param source: source circle
        :param dest: end circle
        :return: tuple (is it in list , index of this element)
        """
        for b in self.list_bridge:
            if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
                return True, int(self.list_bridge.index(b))

        return False, 0

    def remove_bridge(self,index):
        print("usuwam most bo już jest jeden")
        number = self.list_bridge[index].number
        self.list_bridge[index].circle1.conections -= number
        print(self.list_bridge[index].circle1.conections, "ilosc połaczen")
        self.list_bridge[index].circle2.conections -= number
        print(self.list_bridge[index].circle2.conections, "ilosc połaczen2")
        self.list_bridge.remove(self.list_bridge[index])

    def remove_all(self, source, dest):
        """
        This function says if we should remove bridge.
        We can remove bridges if we have 2 bridges between circles.
        :param l: list of bridges
        :param source: source circle
        :param dest: end circle
        :return: tuple ( can we remove bridge, index of bridge)
        """
        for b in self.list_bridge:
            if ((b.circle1 == source and b.circle2 == dest) or (
                            b.circle1 == dest and b.circle2 == source)):
                self.remove_bridge(self.list_bridge.index(b))




    def solve(self,circles):
        print("wchodze do solvera")
        self.list_circles = circles
        print("tyle jest kulek",len(self.list_circles))
        sort_circle(self.list_circles)
        #for i in self.list_circles:
         #   self.find_possible_bridges(i)
        self.recursion(0)
        print("zwracam mosty")
        for i in self.list_bridge:
            print("wartosci mostów",i.number)
        return self.list_bridge

    def recursion(self,index):
        print("jestem w rekursji")

        is_ok = False
        if index < len(self.list_circles):
            circle = self.list_circles[index]
            self.find_possible_bridges(circle)
            for e in circle.combinations:
                print(e)
            print("kulka wartość", circle.value)
            active = ready(circle.close_neighbors)
            print("aktywni", len(active))
            for i in active:
                print(i.value)

            if circle.is_done:
                print("kulka już jest done")
                return self.recursion(index+1)

            elif len(active) >0:
                print("sprawdzam aktywnych", len(active))
                j=0
                while not is_ok and j<len(circle.combinations):
                    print("j",j)
                    if all(i in active for i in circle.combinations[j]):
                        print("dodaje mosty")

                        for z in circle.combinations[j]:
                            is_in_list = self.is_in(circle, z)
                            print("robie most miedzy ", circle, z)
                            if is_in_list[0]:
                                print("już mamy jeden most")
                                self.remove_bridge(is_in_list[1])
                                self.list_bridge.append(Bridge(circle,z,violet,2))
                                circle.add_bridge(z,2)
                            else:
                                print("to jest pierwszy most miedzy ", circle, z)
                                self.list_bridge.append(Bridge(circle, z, violet, 1))
                                circle.add_bridge(z,1)

                        is_ok = self.recursion(index+1)
                        if not is_ok:
                            print("usuwam mosty")
                            for z in circle.combinations[j]:
                                self.remove_all(circle,z)
                    j+=1
                return is_ok
            else:
                return False

        return True


    # def solver(circles):
    #     list_of_bridge = list()
    #     tmp = copy.deepcopy(circles)
    #     iter = 0
    #     j = 0
    #     while len(ready(circles)) > 0:
    #         circle = sort_circle(ready(circles))
    #         print("tyle mamy kulek", len(circle))
    #         print(circle[j].value, "to jest wartosc")
    #         diff = circle[j].value - circle[j].conections
    #         if diff < 0:
    #             break
    #         if diff == 0:
    #             circle[j].is_done = True
    #             print("juz polaczone")
    #             # j+=1
    #
    #         print("roznica przed", diff)
    #         if len(ready(circle[j].close_neighbors)) == 0:
    #             print("!!!!BRAK SASIADOW!!!!")
    #             clear_all(circles)
    #             list_of_bridge.clear()
    #             print(len(list_of_bridge))
    #             print(len(ready(circles)))
    #             iter += 1
    #
    #         if (diff > 0 and diff % len(ready(circle[j].close_neighbors)) != 0):
    #             print("WESZLO DO MODULO")
    #             z = 0
    #             if iter == 0:
    #                 while (diff > 0):
    #                     if (diff > 1 and (sort_value(ready(circle[j].close_neighbors))[z].value -
    #                                           sort_value(ready(circle[j].close_neighbors))[z].conections) >= 2):
    #                         list_of_bridge.append(
    #                             Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 2))
    #                         circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 2)
    #                         diff -= 2
    #                     else:
    #                         list_of_bridge.append(
    #                             Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 1))
    #                         circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 1)
    #
    #                         diff -= 1
    #                     z += 1
    #             if iter == 1:
    #                 if diff == 1:
    #                     list_of_bridge.append(
    #                         Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z + 1], violet, 1))
    #                     circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z + 1], 1)
    #             if diff <= 0:
    #                 print("juz nie mozna")
    #                 circle[j].is_done = True
    #
    #         if diff > 0 and diff == len(ready(circle[j].close_neighbors)):
    #             z = 0
    #             if iter == 0:
    #                 while (diff > 0):
    #                     if diff > 1 and sort_value(ready(circle[j].close_neighbors))[z].value - \
    #                             sort_value(ready(circle[j].close_neighbors))[z].conections >= 2:
    #                         list_of_bridge.append(
    #                             Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 2))
    #                         circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 2)
    #                         diff -= 2
    #                     else:
    #                         list_of_bridge.append(
    #                             Bridge(circle[j], sort_value(ready(circle[j].close_neighbors))[z], violet, 1))
    #                         circle[j].add_bridge(sort_value(ready(circle[j].close_neighbors))[z], 1)
    #
    #                         diff -= 1
    #                     z += 1
    #             if iter == 1:
    #                 for i in range(len(ready(circle[j].close_neighbors))):
    #                     list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[i], violet, 1))
    #                     circle[j].add_bridge((ready(circle[j].close_neighbors))[i], 1)
    #
    #             print("tyle samo sasiadow co wartosc")
    #             if diff <= 0:
    #                 print("juz nie mozna")
    #                 circle[j].is_done = True
    #         if diff > 0 and diff % 2 == 0 and diff == len(ready(circle[j].close_neighbors)) * 2:
    #             for z in range(len(ready(circle[j].close_neighbors))):
    #                 list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[z], violet, 2))
    #                 circle[j].add_bridge(ready(circle[j].close_neighbors)[z], 2)
    #
    #             print("podwojne mosty")
    #             diff = circle[j].value - circle[j].conections
    #             if diff <= 0:
    #                 print("juz nie mozna")
    #                 circle[j].is_done = True
    #         if diff > 0 and len(ready(circle[j].close_neighbors)) == 1:
    #             list_of_bridge.append(Bridge(circle[j], ready(circle[j].close_neighbors)[0], violet, diff))
    #             circle[j].add_bridge(ready(circle[j].close_neighbors)[0], diff)
    #
    #             print("tylko jedne sasiad")
    #             diff = circle[j].value - circle[j].conections
    #             if diff <= 0:
    #                 print("juz nie mozna")
    #                 circle[j].is_done = True
    #
    #     return list_of_bridge

