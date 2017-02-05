import pygame


def load_file():
    return pygame.image.load("background.png")


size = width, height = 800, 500
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('Hashi')
# colors
c1 = (45, 22, 80)
c2 = (45, 22, 81)
c3 = (45, 21, 80)
c4 = (45, 21, 81)
c5 = (55, 22, 80)
c6 = (44, 21, 80)
c7 = (44, 21, 81)
c8 = (45, 22, 82)
c9 = (45, 23, 80)
white = (255, 255, 255)
max_circle = (230, 227, 200)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
violet = (141, 95, 211)
bright_violet = (198, 175, 233)
dark_violet = (45, 22, 80)
blur_violet = (227, 215, 244)
circle_violet = (198, 175, 233, 95.9)

clock = pygame.time.Clock()
