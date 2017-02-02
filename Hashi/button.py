from Hashi.display import *


class Button:
    def __init__(self, x_left, y_left, w, h, color, text, size_of_letters):
        """
        :param x_left: x position
        :param y_left: y position
        :param w: weight of button
        :param h: height of button
        :param color: color of button
        :param text: text which is on the button
        :param size_of_letters: size of letter
        """
        self.x = x_left
        self.y = y_left
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.size = size_of_letters
        self.position_of_text = (0, 0)

    def show(self):
        """
        This function is responsible to show button on the screen
        :return:
        """
        pygame.draw.rect(game_display, self.color, (self.x, self.y, self.w, self.h))
        self.position_of_text = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        text_display(self.text, self.size, dark_violet, self.position_of_text)

    def change_color(self, color):
        """
        This method change a color of button
        :param color: name of color
        """
        self.color = color

    def backlight(self, mouse):
        """
        This method highlight button when position of mouse is in button, square
        :param mouse:Position of mouse
        """
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.change_color(bright_violet)
            self.show()

    def is_clicked(self, mouse):
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
