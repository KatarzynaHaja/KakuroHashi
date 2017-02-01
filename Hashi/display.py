from Hashi.settings import *


def text_display(text, size, color, position):
    t = text_object(text, size, color)
    rect = t.get_rect()
    rect.center = position
    game_display.blit(t, rect)

def text_object(text, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    return text_surface