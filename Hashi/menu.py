from datetime import datetime
from Hashi.button import *
from Hashi.game import *
import os
import datetime
from Hashi.solver import *

pygame.init()


def kind_of_game():
    """
    This function start screen where you can choose kind of game.
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

        game_display.blit(pygame.image.load("background.png"), (0, 0))
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


def is_again(s):
    """
    After you win you can start again. This function starts screen where you can choose
    :param s: kind of game
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

        game_display.blit(pygame.image.load("background.png"), (0, 0))
        position = ((width / 2), (height / 3))
        text_display('Wygrana', 50, dark_violet, (position[0],position[1]-20))
        text_display('Czy chcesz zagrać ponownie?',50,dark_violet,(position[0]+10,position[1]+30))
        mouse = pygame.mouse.get_pos()
        button_yes = Button(350, 250, 100, 50, violet, "tak", 30)
        button_yes.show()
        button_yes.backlight(mouse)
        button_no = Button(350, 350, 100, 50, violet, "nie", 30)
        button_no.show()
        button_no.backlight(mouse)

        if button_yes.is_clicked(mouse):
            choose_level(s)

        pygame.display.update()
        clock.tick(15)

        if button_no.is_clicked(mouse):
            pygame.quit()
            quit()


def choose_level(typ):
    """
    This function allows to choose level
    :param typ: type of game
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

        game_display.blit(pygame.image.load("background.png"), (0, 0))
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
        if typ == 'm':
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
        if typ == 'c':
            if button_easy.is_clicked(mouse):
                g = Game('easy')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop_solver(g)

            if button_medium.is_clicked(mouse):
                g = Game('midi')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop_solver(g)

            if button_hard.is_clicked(mouse):
                g = Game('hard')
                g.board.generate_default_board()
                g.board.random_board()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                g.board.set_bridges()
                gameloop_solver(g)

        pygame.display.update()
        clock.tick(15)


def is_file(typ):
    """
    This function allows to choose if you want to read from file
    :param typ: type of game
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

        game_display.blit(pygame.image.load("background.png"), (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Czy chcesz wczytać z pliku", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_yes = Button(350, 250, 100, 50, violet, "TAK", 30)
        button_yes.show()
        button_yes.backlight(mouse)
        button_no = Button(350, 350, 100, 50, violet, "NIE", 30)
        button_no.show()
        button_no.backlight(mouse)

        if typ == 'c':
            if button_yes.is_clicked(mouse):
                g = Game()
                g.board.generate_by_recognition()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                gameloop_solver(g)

            if button_no.is_clicked(mouse):
                choose_level('c')
        else:
            if button_yes.is_clicked(mouse):
                g = Game()
                g.board.generate_by_recognition()
                g.board.set_neighbors()
                g.board.set_close_neighbors()
                gameloop(g)

            if button_no.is_clicked(mouse):
                choose_level('m')

        pygame.display.update()
        clock.tick(15)


def gameloop(g):
    """
    Main game for normal game ( user and generation)
    :param g: game
    :return:
    """
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
        button_clear = Button(650, 80, 120, 50, violet, "Wyczyść", 25)
        button_clear.show()
        button_clear.backlight(mouse)

        g.board.generate_board()
        check(clicked_list, g)
        print_bridge(g.board.user_list_bridge)

        if is_finished(g.board.list_circle):
            pygame.display.update()
            clock.tick(15)
            pygame.time.delay(800)
            is_again('m')

        if is_show is True:
            g.board.user_list_bridge.clear()
            print_bridge(g.board.user_list_bridge)
            print_bridge(g.board.list_bridge)

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
            print_bridge(g.board.list_bridge)
            pygame.display.update()
            clock.tick(15)
            pygame.time.delay(1500)
            is_again('m')

        if button_hint.is_clicked(mouse) and g.number_of_hints < 3:
            is_hint = True
            g.number_of_hints += 1
            bridge.append(g.random_bridge())

        if is_hint is True:
            for i in bridge:
                if i.number == 1:
                    i.show()
                if i.number == 2:
                    i.show_more()
        if button_clear.is_clicked(mouse):
            clear_bridges(g.board.user_list_bridge)
            g.board.user_list_bridge.clear()

        pygame.display.update()
        clock.tick(15)
        pygame.display.update()
        clock.tick(60)


def gameloop_solver(g):
    """
    Main game for solver
    :param g: game
    :return:
    """
    pygame.display.update()
    clock.tick(15)
    is_show = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        game_display.fill(blur_violet)
        r = pygame.Rect(0, 0, 600, 500)
        sub = game_display.subsurface(r)
        button_save = Button(650, 380, 120, 50, violet, "Zapisz", 25)
        button_save.show()
        button_save.backlight(mouse)
        button_solve = Button(650, 280, 120, 50, violet, "Rozwiąż", 25)
        button_solve.show()
        button_solve.backlight(mouse)

        g.board.generate_board()

        if button_solve.is_clicked(mouse):
            g.board.solve()
            is_show = True

        if is_show is True:
            print_bridge(g.board.user_list_bridge)
            pygame.display.update()
            clock.tick(15)
            pygame.time.delay(800)

        if is_finished(g.board.list_circle):
            is_again('c')

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

        pygame.display.update()
        clock.tick(15)
        pygame.display.update()
        clock.tick(60)


def menu():
    """
    Start menu
    :return:
    """
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)

        game_display.blit(pygame.image.load("background.png"), (0, 0))
        position = ((width / 2), (height / 3))
        text_display("Hashi", 70, dark_violet, position)
        mouse = pygame.mouse.get_pos()
        button_play = Button(350, 250, 100, 50, violet, "Graj", 30)
        button_play.show()
        button_play.backlight(mouse)
        button_instruction = Button(350, 350, 100, 50, violet, "Instrukcja", 30)
        button_instruction.show()
        button_instruction.backlight(mouse)

        if button_instruction.is_clicked(mouse):
            os.startfile("hashi_instruction.pdf")

        if button_play.is_clicked(mouse):
            kind_of_game()

        pygame.display.update()
        clock.tick(15)


menu()
