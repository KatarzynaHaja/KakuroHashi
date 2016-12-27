import random
from pygame import font
from Kakuro.node import *
from Kakuro.display import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.Sum_of_column import *
from Kakuro.Board import *
import os

class Game:
    def __init__(self):
        pygame.init()
        self.nodes = list()

    def gameloop(self):
        while True:
            gameDisplay.fill(white)
            #for node in self.nodes:
                #node.show()
            #suma = Sum_of_column([100, 60], [100, 100], [140, 100], 10)
            #suma.show()

            self.board.show()
            buttonCheck = Button(500, 300, 100, 50, red, "Sprawdz", 30)
            buttonCheck.show()
            if buttonCheck.backlight(pygame.mouse.get_pos()):
                if (buttonCheck.isClicked()):
                    self.result = self.board.check()
            textDisplay(self.result, 40, black, (250,250))
            #pygame.draw.polygon(gameDisplay, black, [[100, 60], [100, 100], [140, 100]], 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Quit to zamkniecie okna przez uzytkownika
                    pygame.quit()
                    quit()
                #for node in self.nodes:
                    #node.update(event, gameDisplay)
                self.board.update(event, gameDisplay)
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
            textDisplay("Kakuro", 100, black, position)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            buttonPlay = Button(350, 300, 100, 50, green, "Graj", 30)
            buttonPlay.show()
            buttonInstruction = Button(350, 400, 100, 50, green, "Instrukcja", 30)
            buttonInstruction.show()
            buttonInstruction.backlight(mouse)
            if buttonPlay.backlight(mouse):
                if(buttonPlay.isClicked()):
                    gameDisplay.fill(white)
                    #kwadracik = Node(1, 100, 100)
                    #self.nodes.append(kwadracik)
                    self.board = Board()
                    self.board.add()
                    self.result = ""
                    self.gameloop()
            if buttonInstruction.backlight(mouse):
                if(buttonInstruction.isClicked()):
                    os.startfile("Instruction.txt")


            pygame.display.update()
            clock.tick(15)

    def start(self):
        self.menu()

game = Game()
game.start()