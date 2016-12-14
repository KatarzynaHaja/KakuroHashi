import random
from Hashi.circle import *


class Game():
    def __init__(self):
        self.number_of_circle = self.random_circle()
        self.list_circle = list()
        self.list_bridge = list()
        self.board = list()
        self.possible = list()

    def random_circle(self):
        value = random.randint(5, 10)
        return value

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
        print(self.number_of_circle)
        n = random.choice(self.board)
        self.list_circle.append(n)
       # self.possible.append(n)
        print(n.x , n.y)
        for i in range(1,self.number_of_circle):
            for j in range(len(self.board)):
                if (self.board[j].x == n.x or self.board[j].y == n.y) and self.board[j] not in self.possible and self.board[j] not in self.list_circle:
                    self.possible.append(self.board[j])
            print('listaaaa')
            for z in range(len(self.possible)):
                print(self.possible[z].x, self.possible[z].y)
                print()
            n = random.choice(self.possible)
            print('To wylosowalam')
            print(n.x , n.y)
            self.list_circle.append(n)
            self.possible.remove(n)

        for i in self.list_circle:
            print(i.x , i.y )
            print()






    def is_finished(self):
        finished=False
        for i in self.list_circle:
            if i.connections == i.value:
                finished = True
            else:
                return False
        if finished == True:
            return True



