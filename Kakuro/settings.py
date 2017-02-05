import pygame
size = width, height = 800, 500
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Kakuro')

highlight_green = (178,225,68)
back_green = (135,199,121,255)
button_green = (90,191,68)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


def background():
    gameDisplay.blit(pygame.image.load("background.png"), (0, 0))

clock = pygame.time.Clock()
