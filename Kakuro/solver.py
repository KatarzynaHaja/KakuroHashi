import random
from pygame import font
from Kakuro.node import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.SumOfColumn import *
from Kakuro.Board import *
import copy


class Solver:
    def __init__(self):
        pygame.init()
        self.board = Board()

    def factorise(self, number, count):
        available_numbers = list(range(1, 10))
        factorisation = list()
        while available_numbers:
            temp = list()
            temp_counter = count
            temp_number = number
            for i in reversed(available_numbers):
                if (i < temp_number and temp_counter > 1) or (i == temp_number and temp_counter == 1):
                    temp.append(i)
                    temp_number -= i
                    temp_counter -= 1
            if temp_number == 0:
                factorisation.append(temp)
            del available_numbers[-1]
            if temp[0] in available_numbers:
                available_numbers.remove(temp[0])
        for e in factorisation:
            print(e)

    def f(self, number, count):
        available_numbers = list(range(1, 10))
        self.factor(number, count, available_numbers)

    def factor(self, number, count, available_numbers):
        if count == 1:
            l = list()
            if number in available_numbers:
                available_numbers.remove(number)
                print(number)
                l.append(number)
            return l
        else:
            available_numbers_copy = copy.copy(available_numbers)
            list_of_all = list()
            for i in reversed(available_numbers_copy):
                if i < number and i in available_numbers:
                    temp_number = number - i
                    available_numbers.remove(i)
                    l = self.factor(temp_number, count - 1, available_numbers)
                    if l:
                        print(i)
                        l.append(i)
                        list_of_all.append(l)





    def game(self):
        gameDisplay.fill(white)
        self.board.generate2()
        for c in self.board.columns.values():
            print(c.sum.number)
            self.factorise(c.sum.number, len(c.column))
        while True:
            gameDisplay.fill(white)
            self.board.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            clock.tick(60)

    def solve(self):
        self.game()


s = Solver()
s.f(10, 3)

