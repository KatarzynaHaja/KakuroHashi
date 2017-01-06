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


        gameDisplay.fill(white)
        position = ((width / 2), (height / 3))
        textDisplay("Wybierz tryb gry", 100, black, position)
        mouse = pygame.mouse.get_pos()
        button_computer = Button(400, 250, 100, 50, green, "Z komputerem", 30, 0)
        button_computer.show()
        button_computer.backlight(mouse)
        button_myself = Button(400, 350, 100, 50, green, "Zwykły", 30, 1)
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

        gameDisplay.fill(white)
        position = ((width / 2), (height / 3))
        textDisplay("Wybierz poziom", 100, black, position)
        mouse = pygame.mouse.get_pos()
        button_easy = Button(400, 250, 100, 50, green, "łatwy", 30, 0)
        button_easy.show()
        button_easy.backlight(mouse)
        button_medium = Button(400, 320, 100, 50, green, "Średni", 30, 1)
        button_medium.show()
        button_medium.backlight(mouse)
        button_hard = Button(400, 390, 100, 50, green, "Trudny", 30, 1)
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
            g = Game('medium')
            g.board.generate_default_board()
            g.board.random_board()
            g.board.set_neighbors()
            g.board.set_close_neighbors()
            gameloop(g)

        if button_hard.isClicked(mouse):
            g = Game('hard')
            g.board.generate_default_board()
            g.board.random_board()
            g.board.set_neighbors()
            g.board.set_close_neighbors()
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
        gameDisplay.fill(white)
        button_save = Button(850, 380, 100, 50, green, "Zapisz", 30, 1)
        button_save.show()
        button_save.backlight(mouse)
        g.board.generate_board()
        #g.board.print_bridge()
        if button_save.isClicked(mouse):
            a = datetime.datetime(2013, 12, 30, 23, 59, 59)
            b = datetime.datetime.now()
            d = b-a
            fname = str(d.seconds)
            r = pygame.Rect(0,0,800,500)
            sub = gameDisplay.subsurface(r)
            position = (900, 450)
            textDisplay("Zapisano do pliku", 30, black, position)
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
        position = ((width / 2)-50, (height / 3))
        textDisplay("Hashi", 100, black, position)
        mouse = pygame.mouse.get_pos()
        button_play = Button(400, 250, 100, 50, green, "Graj", 30, 0)
        button_play.show()
        button_play.backlight(mouse)
        button_instruction = Button(400, 350, 100, 50, green, "Instrukcja", 30, 1)
        button_instruction.show()
        button_instruction.backlight(mouse)

        if (button_instruction.isClicked(mouse)):
            os.startfile("Instruction.txt")


        if(button_play.isClicked(mouse)):
            kind_of_game()

        pygame.display.update()
        clock.tick(15)


menu()
