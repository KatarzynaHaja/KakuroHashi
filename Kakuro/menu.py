import random
from pygame import font
from Kakuro.node import *
from Kakuro.display import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.SumOfColumn import *
from Kakuro.Board import *
import os


class Game:
    def __init__(self):
        pygame.init()
        self.nodes = list()
        self.result = ""
        self.board = Board()

    def gameloop(self):
        while True:
            gameDisplay.fill(white)
            self.board.show()
            button_check = Button(500, 300, 100, 50, red, "Sprawdz", 30)
            button_check.show()
            if button_check.backlight(pygame.mouse.get_pos()):
                if button_check.is_clicked():
                    self.result = self.board.check()
            text_display(self.result, 40, black, (250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.board.update(event)
            pygame.display.update()
            clock.tick(60)

    def menu(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            position = ((width / 2), (height / 3))
            text_display("Kakuro", 100, black, position)
            mouse = pygame.mouse.get_pos()
            button_play = Button(350, 300, 100, 50, green, "Graj", 30)
            button_play.show()
            button_instruction = Button(350, 400, 100, 50, green, "Instrukcja", 30)
            button_instruction.show()
            button_instruction.backlight(mouse)
            if button_play.backlight(mouse):
                if button_play.is_clicked():
                    gameDisplay.fill(white)
                    self.board.generate2()
                    self.result = ""
                    self.gameloop()
            if button_instruction.backlight(mouse):
                if button_instruction.is_clicked():
                    os.startfile("Instruction.txt")
            pygame.display.update()
            clock.tick(15)

    def start(self):
        self.menu()

game = Game()
game.start()
