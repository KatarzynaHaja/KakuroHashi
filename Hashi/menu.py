from datetime import datetime

from Hashi.button import *
from Hashi.display import *
from Hashi.game import *
import os
import random
import datetime
pygame.init()


def kind_of_game():
    pygame.display.update()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        gameDisplay.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        textDisplay("Wybierz tryb gry", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_computer = Button(350, 250, 100, 50, violet, "solver", 30, 0)
        button_computer.show()
        button_computer.backlight(mouse)
        button_myself = Button(350, 350, 100, 50, violet, "zwykły", 30, 1)
        button_myself.show()
        button_myself.backlight(mouse)

        if button_computer.isClicked(mouse):
            choose_level()

        if button_myself.isClicked(mouse):
            choose_level()

        pygame.display.update()
        clock.tick(15)


def choose_level():
    pygame.display.update()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        gameDisplay.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        textDisplay("Wybierz poziom", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_easy = Button(350, 250, 100, 50, violet, "łatwy", 30, 0)
        button_easy.show()
        button_easy.backlight(mouse)
        button_medium = Button(350, 320, 100, 50, violet, "średni", 30, 1)
        button_medium.show()
        button_medium.backlight(mouse)
        button_hard = Button(350, 390, 100, 50, violet, "trudny", 30, 1)
        button_hard.show()
        button_hard.backlight(mouse)

        if button_easy.isClicked(mouse):
            g = Game('easy')
            g.board.generate_default_board()
            g.board.random_board()
            g.board.set_neighbors()
            g.board.set_close_neighbors()
            g.board.set_bridges()
            gameloop(g)

        if button_medium.isClicked(mouse):
            g = Game('midi')
            g.board.generate_default_board()
            g.board.random_board()
            g.board.set_neighbors()
            g.board.set_close_neighbors()
            g.board.set_bridges()
            gameloop(g)

        if button_hard.isClicked(mouse):
            g = Game('hard')
            g.board.generate_default_board()
            g.board.random_board()
            g.board.set_neighbors()
            g.board.set_close_neighbors()
            g.board.set_bridges()
            gameloop(g)

        pygame.display.update()
        clock.tick(15)


def gameloop(g):
    pygame.display.update()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        mouse = pygame.mouse.get_pos()
        gameDisplay.fill(blur_violet)
        r = pygame.Rect(0, 0, 600, 500)
        sub = gameDisplay.subsurface(r)
        button_save = Button(650, 380, 100, 50, violet, "Zapisz", 30, 1)
        button_save.show()
        button_save.backlight(mouse)
        g.board.generate_board()
        g.board.print_bridge()
        if button_save.isClicked(mouse):
            a = datetime.datetime(2013, 12, 30, 23, 59, 59)
            b = datetime.datetime.now()
            d = b-a
            fname = str(d.seconds)
            position = (700, 450)
            textDisplay("Zapisano do pliku", 30, dark_violet, position)
            pygame.display.update()
            pygame.image.save(sub, "generated_boards/"+fname+".png")

        pygame.display.update()
        clock.tick(15)
        pygame.display.update()
        clock.tick(60)

def menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        gameDisplay.blit(image,(0,0))
        position = ((width / 2), (height / 3))
        textDisplay("Hashi", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_play = Button(350, 250, 100, 50, violet, "Graj", 30, 0)
        button_play.show()
        button_play.backlight(mouse)
        button_instruction = Button(350, 350, 100, 50, violet, "Instrukcja", 30, 1)
        button_instruction.show()
        button_instruction.backlight(mouse)

        if (button_instruction.isClicked(mouse)):
            os.startfile("Instruction.txt")


        if(button_play.isClicked(mouse)):
            kind_of_game()

        pygame.display.update()
        clock.tick(15)


menu()
