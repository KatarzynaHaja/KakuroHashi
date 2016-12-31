from Kakuro.settings import *


def text_display(text, sizze, color, position):
    t = text_object(text, sizze, color)
    rect = t.get_rect()
    rect.center = position
    gameDisplay.blit(t, rect)


def text_object(text, sizze, color):
    font = pygame.font.Font(None, sizze)
    text_surface = font.render(text, True, color)
    return text_surface
