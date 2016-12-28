import random
from Hashi.circle import *
from operator import itemgetter, attrgetter, methodcaller


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
            value = random.randint(5, 10)
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
                if(self.board[j]!=self.board[i]):
                    if((self.list_circle[i].x == self.list_circle[j].x or self.list_circle[i].y == self.list_circle[j].y)):
                        self.list_circle[i].neighbors.append(self.list_circle[j])
            print("lista",len(self.list_circle[i].neighbors))
            for z in range(len(self.list_circle[i].neighbors)):
                print(self.list_circle[i].neighbors[z].x , self.list_circle[i].neighbors[z].y)
            print()



    def sort_circle(self):
        list_circle = sorted(self.list_circle,key=attrgetter('x', 'y') )
        return list_circle

    def print_circle(self):
        self.list_circle = self.sort_circle()
        for i in range(len(self.list_circle)):
            print(self.list_circle[i].x , self.list_circle[i].y)