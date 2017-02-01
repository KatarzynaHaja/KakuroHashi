import pygame

size = width, height = 800, 500
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('Hashi')

image = pygame.image.load("background.png")
white = (255, 255, 255)
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
