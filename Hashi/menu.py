import random
import sys, pygame
from Hashi.bridge import *
from Hashi.button import *
from Hashi.circle import *
from Hashi.settings import *
from Hashi.display import *
from Hashi.game import *
import os
pygame.init()


def gameloop(g):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Quit to zamkniecie okna przez uzytkownika
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        #textDisplay("Let's game begin...", 40, red, (width/2, height/2))
        g.generate_board()
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

        gameDisplay.fill(white)
        position = ((width / 2), (height / 3))
        textDisplay("Hashi", 100, black, position)
        mouse = pygame.mouse.get_pos()
        buttonPlay =Button(350, 300, 100, 50, green, "Graj", 30,0)
        buttonPlay.show()
        buttonPlay.backlight(mouse)
        buttonInstruction = Button(350,400,100,50, green , "Instrukcja", 30,1)
        buttonInstruction.show()
        buttonInstruction.backlight(mouse)

        print(buttonInstruction.isClicked(mouse))
        print(buttonPlay.isClicked(mouse))


        if (buttonInstruction.isClicked(mouse)):
            os.startfile("Instruction.txt")

        if(buttonPlay.isClicked(mouse)):
            g = Game()
            g.generate_default_board()
            g.random_circle()
            g.random_board()
            gameloop(g)

        pygame.display.update()
        clock.tick(15)
    def isFinished():
        #jesli liczba połączeń jest równa wartości we wszystkich kółkach zakończ
        pass


menu()







