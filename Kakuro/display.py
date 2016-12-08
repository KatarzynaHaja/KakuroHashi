from Kakuro.settings import *


def textDisplay(text, size, color, position):
    t = textObject(text, size, color)
    rect = t.get_rect()
    rect.center = position
    gameDisplay.blit(t, rect)


def textObject(text, size, color):
    font = pygame.font.Font(None, size)
    textSurface = font.render(text, True, color)
    return textSurface