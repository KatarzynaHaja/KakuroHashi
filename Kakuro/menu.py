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
        self.hints = ""

    def gameloop(self):
        while True:
            gameDisplay.fill(white)
            self.board.show()
            button_check = Button(500, 300, 100, 50, red, "Sprawdz", 30)
            button_check.show()
            button_hint = Button(500, 400, 100, 50, red, "Hint", 30)
            button_hint.show()
            mouse = pygame.mouse.get_pos()
            if button_check.backlight(mouse):
                if button_check.is_clicked(mouse):
                    self.result = self.board.check()
            text_display(self.result, 40, black, (420, 30))
            if button_hint.backlight(mouse):
                if button_hint.is_clicked(mouse):
                    self.hints = self.board.hint()
            text_display(self.hints, 25, black, (520, 470))
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.event.post(event)

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
                if button_play.is_clicked(mouse):
                    gameDisplay.fill(white)
                    self.choose_level()
            if button_instruction.backlight(mouse):
                if button_instruction.is_clicked(mouse):
                    os.startfile("Instruction.txt")
            pygame.display.update()
            clock.tick(15)

    def start(self):
        self.menu()

    def choose_level(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.event.post(event)

            gameDisplay.fill(white)
            position = ((width / 2), (height / 3))
            text_display("Wybierz poziom", 100, black, position)
            mouse = pygame.mouse.get_pos()
            button_easy = Button(350, 300, 100, 50, green, "Latwy", 30)
            button_easy.show()
            button_easy.backlight(mouse)
            button_medium = Button(350, 380, 100, 50, green, "Średni", 30)
            button_medium.show()
            button_medium.backlight(mouse)
            button_hard = Button(350, 460, 100, 50, green, "Trudny", 30)
            button_hard.show()
            button_hard.backlight(mouse)
            if button_easy.is_clicked(mouse) or button_medium.is_clicked(mouse) or button_hard.is_clicked(mouse):
                self.board.generate2()
                self.result = ""
                self.gameloop()
            pygame.display.update()
            clock.tick(15)


game = Game()
game.start()
