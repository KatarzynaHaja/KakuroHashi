import random
from operator import attrgetter

from pygments.lexer import include

from Hashi.circle import *


class Game():
    def __init__(self):
        self.list_circle = list()
        self.list_bridge = list()
        self.board = list()
        self.possible = list()


    def set_number_of_circle(self):
        self.number_of_circle = self.random_circle()

    def random_circle(self):
        print("to jest level",self.level)
        if self.level ==0:
            value = random.randint(10,16)
        if self.level == 1:
            value = random.randint(11, 20)
        if self.level == 2:
            value = random.randint(21, 30)
        return value

    def set_level(self,s):
        if s == 'easy':
            self.level =0
        if s == 'midi':
            self.level =1
        if s == 'hard':
            self.level =2

    def random_brigde(self):
        value = random.randint(1, 5)
        return value

    def generate_board(self):
        for i in self.list_circle:
            i = Circle(i.value,i.x , i.y)
            i.show()

    def generate_default_board(self):
        for i in range(5):
            for j in range(8):
                self.board.append(Circle(0,j*100+50,i*100+50))
        for i in range (len(self.board)):
            self.board[i].show()

    def random_board(self):
        print("znowu kółka" , self.number_of_circle)
        n = random.choice(self.board)
        self.list_circle.append(n)
        for i in range(1,self.number_of_circle):
            for j in range(len(self.board)):
                if (self.board[j].x == n.x or self.board[j].y == n.y) and self.board[j] not in self.possible and self.board[j] not in self.list_circle:
                    self.possible.append(self.board[j])
            n = random.choice(self.possible)

            self.list_circle.append(n)
            self.possible.remove(n)



    def is_finished(self):
        finished=False
        for i in self.list_circle:
            if i.connections == i.value:
                finished = True
            else:
                return False
        if finished == True:
            return True

    def set_neighbors(self):
        print("bleee", len(self.list_circle))
        for i in range(len(self.list_circle)):
            for j in range(len(self.list_circle)):
                #if(self.list_circle[j]!=self.list_circle[i]):
                    if self.list_circle[i].x == self.list_circle[j].x:
                        self.list_circle[i].neighbors_x.append(self.list_circle[j])
                    if  self.list_circle[i].y == self.list_circle[j].y:
                        self.list_circle[i].neighbors_y.append(self.list_circle[j])


    def sort_circle_x(self,l):
        list_circle = sorted(l, key=attrgetter('x'))
        return list_circle

    def sort_circle_y(self,l):
        list_circle = sorted(l, key = attrgetter('y'))
        return list_circle

    def print_list(self,l):
        for i in range(len(l)):
            print(l[i].x, l[i].y)



    def set_close_neighbors(self):

        for i in range(len(self.list_circle)):
            value = 0
            sorted_y = self.sort_circle_y(self.list_circle[i].neighbors_x)
            sorted_x = self.sort_circle_x(self.list_circle[i].neighbors_y)
            # pętla po wszystkich sasiadach . Gdy x równe to sprawdzamy na liscie y pozycje i jesli mamy indeks+1 lub indeks-1 zaznaczamy jako sasiad
            # analogicznie gdy y są równe
            for j in range(0,len(self.list_circle[i].neighbors_x)):
                    index_y = sorted_y.index(self.list_circle[i])
                    if sorted_y.index(self.list_circle[i].neighbors_x[j]) == index_y - 1 or sorted_y.index(self.list_circle[i].neighbors_x[j]) == index_y +1:
                            self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_x[j])
                            value += 1
                            print("blee x")
            for j in range(0,len(self.list_circle[i].neighbors_y)):
                    index_x = sorted_x.index(self.list_circle[i])
                    if sorted_x.index(self.list_circle[i].neighbors_y[j]) == index_x - 1 or sorted_x.index(self.list_circle[i].neighbors_y[j]) == index_x +1:
                            self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_y[j])
                            value += 1
                            print("blee x")


            self.list_circle[i].set_value(value)


    def print_circle(self):
        self.list_circle = self.sort_circle_x(self.list_circle)
        for i in range(len(self.list_circle)):
            print(self.list_circle[i].x , self.list_circle[i].y)
            print(self.list_circle.index(self.list_circle[i]))

    def print_neighbors(self):
        for i in range(len(self.list_circle)):
            print("wierzcholek",self.list_circle[i].x, self.list_circle[i].y)
            print("ilosc sasiadow",len(self.list_circle[i].close_neighbors))
            for j in range(len(self.list_circle[i].close_neighbors)):
                print( "to jest sasiad",self.list_circle[i].close_neighbors[j].x,self.list_circle[i].close_neighbors[j].y)



    def set_bridge(self):
        for i in range(len(self.list_circle)):
            for j in range(len(self.list_circle[i].close_neighbors)):
                    self.list_circle[i].addBridge(self.list_circle[i].close_neighbors[j], green)

