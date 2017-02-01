from Hashi.display import *


class Button:
    def __init__(self, xleft, yleft, width, height, color, text, size_of_letters, i):
        self.x = xleft
        self.y = yleft
        self.w = width
        self.h = height
        self.color = color
        self.text = text
        self.size = size_of_letters
        self.is_clicked = False
        self.position = i

    def show(self):
        """
        This function is responsible to show button on the screen
        :return:
        """
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        self.position_of_text = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        textDisplay(self.text, self.size, dark_violet, self.position_of_text)

    def change_color(self, color):
        """
        This method change a color of button
        :param color: name of color
        :return:
        """
        self.color = color

    def backlight(self, mouse):
        """
        This method highlight button when position of mouse is in button, square
        :param mouse:Position of mouse
        :return:
        """
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.change_color(bright_violet)
            self.show()

    def isClicked(self, mouse):
        """
        This function says if button is clicked. Peek of the queue is checked
        :param mouse: position of mouse
        :return: logical value : yes if button is clicked and no if not
        """
        if pygame.event.peek(pygame.MOUSEBUTTONDOWN) and self.x + self.w > mouse[0] > self.x and self.y + self.h > \
                mouse[1] > self.y:
            pygame.event.clear()
            return True
        else:
            return False
