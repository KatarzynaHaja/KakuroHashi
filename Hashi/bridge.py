from Hashi.display import *


class Bridge:
    def __init__(self, from_circle, to_circle, color, value):
        """
        Constructor
        :param from_circle: source circle
        :param to_circle: destination circle
        :param color: bridge's color
        :param value: it says how many bridges connect 2 circles
        """
        self.circle1 = from_circle
        self.circle2 = to_circle
        self.color = color
        self.number = value

    def show(self):
        """
        This function draws bridge between two circles.
        """
        if self.circle1.x == self.circle2.x:
            if self.circle1.y > self.circle2.y:
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x, self.circle1.y - self.circle1.r),
                                 (self.circle2.x, self.circle2.y + self.circle2.r))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x, self.circle2.y - self.circle2.r),
                                 (self.circle1.x, self.circle1.y + self.circle1.r))
        if self.circle1.y == self.circle2.y:
            if self.circle1.x > self.circle2.x:
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y),
                                 (self.circle2.x + self.circle2.r, self.circle2.y))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y),
                                 (self.circle1.x + self.circle1.r, self.circle1.y))

    def show_more(self):
        """
        Function which draws 2 bridges between two circle
        """
        if self.circle1.x == self.circle2.x:
            if self.circle1.y > self.circle2.y:
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x - 10, self.circle1.y - self.circle1.r),
                                 (self.circle2.x - 10, self.circle2.y + self.circle2.r))
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x + 10, self.circle1.y - self.circle1.r),
                                 (self.circle2.x + 10, self.circle2.y + self.circle2.r))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x - 10, self.circle2.y - self.circle2.r),
                                 (self.circle1.x - 10, self.circle1.y + self.circle1.r))
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x + 10, self.circle2.y - self.circle2.r),
                                 (self.circle1.x + 10, self.circle1.y + self.circle1.r))
        if self.circle1.y == self.circle2.y:
            if self.circle1.x > self.circle2.x:
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y - 10),
                                 (self.circle2.x + self.circle2.r, self.circle2.y - 10))
                pygame.draw.line(gameDisplay, self.color, (self.circle1.x - self.circle1.r, self.circle1.y + 10),
                                 (self.circle2.x + self.circle2.r, self.circle2.y + 10))
            else:
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y - 10),
                                 (self.circle1.x + self.circle1.r, self.circle1.y - 10))
                pygame.draw.line(gameDisplay, self.color, (self.circle2.x - self.circle2.r, self.circle2.y + 10),
                                 (self.circle1.x + self.circle1.r, self.circle1.y + 10))
