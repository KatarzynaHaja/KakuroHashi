import random
from pygame import font
from Kakuro.node import *
from Kakuro.display import *
from Kakuro.button import *
from Kakuro.settings import *
from Kakuro.Sum_of_column import *

class Game:
    def __init__(self):
        pygame.init()
        self.nodes = list()

    def gameloop(self):
        while True:
            gameDisplay.fill(white)
            for node in self.nodes:
                node.show()
            suma = Sum_of_column([100, 60], [100, 100], [140, 100], 10)
            suma.show()
            pygame.draw.polygon(gameDisplay, black, [[100, 60], [100, 100], [140, 100]], 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Quit to zamkniecie okna przez uzytkownika
                    pygame.quit()
                    quit()
                for node in self.nodes:
                    node.update(event, gameDisplay)
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
            if buttonPlay.backlight(mouse):
                if(buttonPlay.isClicked()):
                    gameDisplay.fill(white)
                    kwadracik = Node(1, 100, 100)
                    self.nodes.append(kwadracik)
                    self.gameloop()

            pygame.display.update()
            clock.tick(15)

    def start(self):
        self.menu()

game = Game()
game.start()