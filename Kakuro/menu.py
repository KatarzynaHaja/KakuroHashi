import random
from pygame import font
from Kakuro.node import *
from Kakuro.display import *
pygame.init()




def gameloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Quit to zamkniecie okna przez uzytkownika
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        textDisplay("Let's game begin...", 40, red, (width/2, height/2))
        kwadracik = Node(1, 20, 30)
        kwadracik.show(gameDisplay)
        pygame.display.update()
        clock.tick(60)


class Button:
    def __init__(self,xleft, yleft, width, height, color, text, sizeOfLetters):
        self.x = xleft
        self.y = yleft
        self.w = width
        self.h = height
        self.color = color
        self.text = text
        self.size = sizeOfLetters

    def show(self):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        self.positionOfText = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        textDisplay(self.text, self.size, black, self.positionOfText)

    def changeColor(self,color):
        self.color = color

    def backlight(self, mouse):
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.changeColor(bright_green)
            self.show()

    def isClicked(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            return True
        else:
            return False


def menu():
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
        buttonPlay.backlight(mouse)
        if(buttonPlay.isClicked()):
            gameloop()


        pygame.display.update()
        clock.tick(15)

menu()
