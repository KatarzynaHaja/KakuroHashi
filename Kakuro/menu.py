import random
from pygame import font
from Kakuro.node import *
from Kakuro.display import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.sumofcolumn import *
from Kakuro.board import *
import os
from datetime import datetime
import datetime


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
            r = pygame.Rect(0, 0, 450, 500)
            sub = gameDisplay.subsurface(r)
            self.board.show()
            button_check = Button(500, 300, 100, 50, red, "Sprawdz", 30)
            button_check.show()
            button_hint = Button(500, 400, 100, 50, red, "Hint", 30)
            button_hint.show()
            button_save = Button(500, 200, 100, 50, green, "Zapisz plansze", 30)
            button_save.show()
            mouse = pygame.mouse.get_pos()
            if button_check.backlight(mouse):
                if button_check.is_clicked(mouse):
                    self.result = self.board.check()
            text_display(self.result, 40, black, (420, 30))
            if button_hint.backlight(mouse):
                if button_hint.is_clicked(mouse):
                    self.hints = self.board.hint()
            text_display(self.hints, 25, black, (520, 470))
            if button_save.backlight(mouse):
                if button_save.is_clicked(mouse):
                    a = datetime.datetime(2013, 12, 30, 23, 59, 59)
                    b = datetime.datetime.now()
                    d = b - a
                    fname = str(d.seconds)
                    position = (700, 450)
                    text_display("Zapisano do pliku", 30, black, position)
                    pygame.display.update()
                    pygame.image.save(sub, "generated_boards/" + fname + ".png")
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
            button_create_from_text = Button(500, 400, 100, 50, green, "Stworz plansze", 30)
            button_create_from_text.show()
            if button_play.backlight(mouse):
                if button_play.is_clicked(mouse):
                    gameDisplay.fill(white)
                    self.choose_level()
            if button_instruction.backlight(mouse):
                if button_instruction.is_clicked(mouse):
                    os.startfile("Instruction.txt")
            if button_create_from_text.backlight(mouse):
                if button_create_from_text.is_clicked(mouse):
                    self.board.create_board_from_file()
                    self.create_board()
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
            if button_easy.is_clicked(mouse):
                self.board.generate(4)
                self.result = ""
                self.gameloop()
            if button_medium.is_clicked(mouse):
                self.board.generate(6)
                self.result = ""
                self.gameloop()
            if button_hard.is_clicked(mouse):
                self.board.generate(8)
                self.result = ""
                self.gameloop()

            pygame.display.update()
            clock.tick(15)

    def create_board(self):
        while True:
            gameDisplay.fill(white)
            self.board.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.board.update(event)
            pygame.display.update()
            clock.tick(60)


game = Game()
game.start()
