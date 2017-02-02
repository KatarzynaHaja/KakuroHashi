from Hashi.settings import *


def text_display(text, s, color, position):
    """
    This method displays text
    :param text: What should be display
    :param s: size
    :param color: color
    :param position: where
    """
    t = text_object(text, s, color)
    rect = t.get_rect()
    rect.center = position
    game_display.blit(t, rect)


def text_object(text, s, color):
    """
    It renders text
    :param text: text which should be render
    :param s: size
    :param color: color
    :return: text surface
    """
    font = pygame.font.Font(None, s)
    text_surface = font.render(text, True, color)
    return text_surface
