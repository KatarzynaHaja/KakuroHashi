from Kakuro.button import *
import os
from datetime import datetime
import datetime
from Kakuro.solver import *


class Game:
    def __init__(self):
        pygame.init()
        self.nodes = list()
        self.result = ""
        self.board = Board()
        self.hints = ""

    def game_loop(self, board_generated=True):
        """
        Function
        :return:
        """
        color_of_solve = button_green
        while True:
            background()
            r = pygame.Rect(0, 0, 450, 500)
            sub = gameDisplay.subsurface(r)
            self.board.show()
            button_check = Buttton(650, 280, 120, 50, button_green, "Sprawdź", 25)
            button_check.show()
            button_save = Buttton(650, 180, 120, 50, button_green, "Zapisz", 25)
            button_save.show()
            button_solve = Buttton(650, 80, 120, 50, color_of_solve, "Rozwiąż", 25)
            button_solve.show()
            if board_generated:
                button_hint = Buttton(650, 380, 120, 50, button_green, "Podpowiedz", 25)
                button_hint.show()
            mouse = pygame.mouse.get_pos()
            if button_check.backlight(mouse):
                if button_check.is_clicked(mouse):
                    self.result = self.board.check()
                    if self.result == 'Wygrana':
                        self.again()
            text_display(self.result, 40, black, (420, 30))
            if board_generated:
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
            if self.board.is_filled():
                color_of_solve = (247, 111, 117)
                button_solve.change_color(color_of_solve)
            else:
                color_of_solve = button_green
                if button_solve.backlight(mouse):
                    if button_solve.is_clicked(mouse):
                        solver = Solver(self.board)
                        solver.solve()
                        self.board.show()
                        pygame.display.update()
                        pygame.time.delay(1500)
                        self.again()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.board.update(event)
            pygame.display.update()
            clock.tick(60)

    def menu(self):
        """
        Function shows menu
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.event.post(event)

            background()
            position = ((width / 2), (height / 3))
            text_display("Kakuro", 70, black, position)
            mouse = pygame.mouse.get_pos()
            button_play = Buttton(320, 250, 150, 50, button_green, "Graj", 30)
            button_play.show()
            button_instruction = Buttton(320, 320, 150, 50, button_green, "Instrukcja", 30)
            button_instruction.show()
            button_create_from_text = Buttton(320, 390, 150, 50, button_green, "Wczytaj planszę", 30)
            button_create_from_text.show()
            if button_play.backlight(mouse):
                if button_play.is_clicked(mouse):
                    background()
                    self.choose_level()
            if button_instruction.backlight(mouse):
                if button_instruction.is_clicked(mouse):
                    os.startfile("kakuro_instruction.pdf")
            if button_create_from_text.backlight(mouse):
                if button_create_from_text.is_clicked(mouse):
                    self.board.create_board_from_file()
                    self.game_loop(False)
            pygame.display.update()
            clock.tick(15)

    def start(self):
        self.menu()

    def choose_level(self):
        """
        Function which lets user choose level
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.event.post(event)

            background()
            position = ((width / 2), (height / 3))
            text_display("Wybierz poziom", 70, black, position)
            mouse = pygame.mouse.get_pos()
            button_easy = Buttton(320, 250, 150, 50, button_green, "Łatwy", 30)
            button_easy.show()
            button_easy.backlight(mouse)
            button_medium = Buttton(320, 320, 150, 50, button_green, "Średni", 30)
            button_medium.show()
            button_medium.backlight(mouse)
            button_hard = Buttton(320, 390, 150, 50, button_green, "Trudny", 30)
            button_hard.show()
            button_hard.backlight(mouse)
            if button_easy.is_clicked(mouse):
                self.board.generate(4)
                self.result = ""
                self.game_loop()
            if button_medium.is_clicked(mouse):
                self.board.generate(6)
                self.result = ""
                self.game_loop()
            if button_hard.is_clicked(mouse):
                self.board.generate(8)
                self.result = ""
                self.game_loop()

            pygame.display.update()
            clock.tick(15)

    def again(self):
        """
        After you won you can start again. This function shows screen where you can choose
        :return:
        """
        pygame.display.update()
        clock.tick(15)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.event.post(event)

            background()
            position = ((width / 2), (height / 3))
            text_display("Wygrana!!!", 100, black, ((width / 2), (height / 5)))
            text_display("Czy chcesz zagrać ponownie?", 70, black, position)
            mouse = pygame.mouse.get_pos()
            button_yes = Buttton(350, 250, 100, 50, green, "tak", 30)
            button_yes.show()
            button_yes.backlight(mouse)
            button_no = Buttton(350, 350, 100, 50, green, "nie", 30)
            button_no.show()
            button_no.backlight(mouse)

            if button_yes.is_clicked(mouse):
                self.board = Board()
                self.choose_level()

            pygame.display.update()
            clock.tick(15)

            if button_no.is_clicked(mouse):
                pygame.quit()
                quit()


game = Game()
game.start()
