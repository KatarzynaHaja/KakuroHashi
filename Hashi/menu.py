import random
import sys, pygame
from Hashi.bridge import *
from Hashi.button import *
from Hashi.circle import *
from Hashi.settings import *
from Hashi.display import *
pygame.init()


def gameloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Quit to zamkniecie okna przez uzytkownika
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        textDisplay("Let's game begin...", 40, red, (width/2, height/2))

        c = Circle(10, 100, 100)
        c.show()
        c2 = Circle(2, 200, 100)
        c2.show()
        c.addBridge(c2)
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
        click = pygame.mouse.get_pressed()
        buttonPlay =Button(350, 300, 100, 50, green, "Graj", 30)
        buttonPlay.show()
        buttonPlay.backlight(mouse)
        if(buttonPlay.isClicked()):
            gameloop()
        pygame.display.update()
        clock.tick(15)


menu()







