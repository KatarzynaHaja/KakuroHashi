from datetime import datetime

from docutils.nodes import classifier

from Hashi.button import *
from Hashi.display import *
from Hashi.game import *
import os
import random
import datetime

pygame.init()
from Hashi.bridge import *


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

        game_display.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Wybierz tryb gry", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_computer = Button(350, 250, 100, 50, violet, "solver", 30)
        button_computer.show()
        button_computer.backlight(mouse)
        button_myself = Button(350, 350, 100, 50, violet, "zwykły", 30)
        button_myself.show()
        button_myself.backlight(mouse)

        if button_computer.is_clicked(mouse):
            is_file('c')

        if button_myself.is_clicked(mouse):
            is_file('m')

        pygame.display.update()
        clock.tick(15)


def choose_level(type):
    pygame.display.update()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        game_display.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Wybierz poziom", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_easy = Button(350, 250, 100, 50, violet, "łatwy", 30)
        button_easy.show()
        button_easy.backlight(mouse)
        button_medium = Button(350, 320, 100, 50, violet, "średni", 30)
        button_medium.show()
        button_medium.backlight(mouse)
        button_hard = Button(350, 390, 100, 50, violet, "trudny", 30)
        button_hard.show()
        button_hard.backlight(mouse)
        if type == 'm':
            if button_easy.is_clicked(mouse):
                g = Game('easy')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop(g)

            if button_medium.is_clicked(mouse):
                g = Game('midi')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop(g)

            if button_hard.is_clicked(mouse):
                g = Game('hard')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop(g)
        if type == 'c':
            if button_easy.is_clicked(mouse):
                g = Game('easy')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                g.board.solve()
                gameloop(g)

            if button_medium.is_clicked(mouse):
                g = Game('midi')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                g.board.solve()
                gameloop(g)

            if button_hard.is_clicked(mouse):
                g = Game('hard')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                g.board.solve()
                gameloop(g)

        pygame.display.update()
        clock.tick(15)


def is_file(type):
    pygame.display.update()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        game_display.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Czy chcesz wczytać z pliku", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_yes = Button(350, 250, 100, 50, violet, "TAK", 30)
        button_yes.show()
        button_yes.backlight(mouse)
        button_no = Button(350, 350, 100, 50, violet, "NIE", 30)
        button_no.show()
        button_no.backlight(mouse)

        if type == 'c':
            if button_yes.is_clicked(mouse):
                g = Game()
                g.board.generate_by_reconition()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.solve()
                gameloop(g)

            if button_no.is_clicked(mouse):
                choose_level('c')
        else:
            if button_yes.is_clicked(mouse):
                g = Game()
                g.board.generate_by_reconition()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                gameloop(g)

            if button_no.is_clicked(mouse):
                choose_level('m')

        pygame.display.update()
        clock.tick(15)


def gameloop(g):
    pygame.display.update()
    clock.tick(15)
    is_show = False
    is_hint = False
    bridge = list()
    clicked_list = list()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            z = g.board.update(event)
            if z is not None:
                clicked_list.append(z)

        mouse = pygame.mouse.get_pos()
        game_display.fill(blur_violet)
        r = pygame.Rect(0, 0, 600, 500)
        sub = game_display.subsurface(r)
        button_save = Button(650, 380, 120, 50, violet, "Zapisz", 25)
        button_save.show()
        button_save.backlight(mouse)
        button_solve = Button(650, 280, 120, 50, violet, "Rozwiązanie", 25)
        button_solve.show()
        button_solve.backlight(mouse)
        button_hint = Button(650, 180, 120, 50, violet, "Wskazówka", 25)
        button_hint.show()
        button_hint.backlight(mouse)

        g.board.generate_board()

        check(clicked_list, g)
        g.board.print_bridge(g.board.user_list_bridge)
        if is_show == True:
            g.board.print_bridge(g.board.list_bridge)

        if button_save.is_clicked(mouse):
            a = datetime.datetime(2013, 12, 30, 23, 59, 59)
            b = datetime.datetime.now()
            d = b - a
            fname = str(d.seconds)
            position = (700, 450)
            text_display("Zapisano do pliku", 30, dark_violet, position)
            pygame.display.update()
            pygame.image.save(sub, "generated_boards/" + fname + ".png")
        if button_solve.is_clicked(mouse):
            is_show = True
        if button_hint.is_clicked(mouse) and g.number_of_hints < 3:
            is_hint = True
            g.number_of_hints += 1
            bridge.append(g.random_bridge())
        if is_hint == True:
            for i in bridge:
                if i.number == 1:
                    i.show()
                if i.number == 2:
                    i.show_more()

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

        game_display.blit(image, (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Hashi", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_play = Button(350, 250, 100, 50, violet, "Graj", 30)
        button_play.show()
        button_play.backlight(mouse)
        button_instruction = Button(350, 350, 100, 50, violet, "Instrukcja", 30)
        button_instruction.show()
        button_instruction.backlight(mouse)

        if (button_instruction.is_clicked(mouse)):
            os.startfile("Instruction.txt")

        if (button_play.is_clicked(mouse)):
            kind_of_game()

        pygame.display.update()
        clock.tick(15)


def is_in(l, source, dest):
    for b in l:
        if ((b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source)):
            return True, int(l.index(b))

    return False, 0


def if_remove(l, source, dest):
    for b in l:
        if ((b.circle1 == source and b.circle2 == dest) or (
                        b.circle1 == dest and b.circle2 == source)) and b.number == 2:
            return True, int(l.index(b))

    return False, 0


def check(z, g):
    if len(z) == 2:
        if z[0] in z[1].close_neighbors:
            w = is_in(g.board.user_list_bridge, z[0], z[1])
            s = if_remove(g.board.user_list_bridge, z[0], z[1])
            if w[0]:
                g.board.user_list_bridge.remove(g.board.user_list_bridge[w[1]])
                z[0].conections -= 1
                z[1].conections -= 1
                g.board.user_list_bridge.append(Bridge(z[0], z[1], violet, 2))
                z[0].add_bridge(z[1], 2)
            if w[0] is False:
                g.board.user_list_bridge.append(Bridge(z[0], z[1], violet, 1))
                z[0].add_bridge(z[1], 1)
            if s[0]:
                g.board.user_list_bridge.remove(g.board.user_list_bridge[s[1]])
                z[0].conections -= 2
                z[1].conections -= 2
            print(len(g.board.user_list_bridge))

        z.clear()


menu()
