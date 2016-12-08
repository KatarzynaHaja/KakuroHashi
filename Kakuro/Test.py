import pygame


class TextBox:
    def __init__(self, rect, width=1):
        self.selected = False
        self.font_size = 15
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.str_list = []
        self.width = width
        self.color = (255, 255, 255)
        self.rect = rect

    def char_add(self, event):
        '''modify string list based on event.key'''
        if event.key == pygame.K_BACKSPACE:
            if self.str_list:
                self.str_list.pop()
        elif event.key == pygame.K_RETURN:
            return ''.join(self.str_list)
        elif event.key in [pygame.K_TAB, pygame.K_KP_ENTER]:  # unwanted keys
            return False
        elif event.key == pygame.K_DELETE:
            self.str_list = []
            return False
        else:
            char = event.unicode
            if char:  # stop emtpy space for shift key adding to list
                self.str_list.append(char)

    def update(self, scr):
        if self.selected:
            w = 2
        else:
            w = self.width

        s = ''.join(self.str_list)
        if len(s) > 0:
            for n, l in enumerate(s):
                if self.font.size(s[n:])[0] < self.rect.width:
                    label = self.font.render(s[n:], 1, self.color)
                    break
        else:
            label = self.font.render(s, 1, self.color)

        pygame.draw.rect(scr, self.color, self.rect, w)
        scr.blit(label, self.rect)


class Control:
    def __init__(self):
        pygame.init()
        self.screensize = (800, 600)
        self.screen = pygame.display.set_mode(self.screensize)
        self.clock = pygame.time.Clock()
        self.gamestate = True
        self.input_entered = None

        self.textboxes = [
            TextBox(pygame.Rect(100, 300, 300, 25), 1),
            TextBox(pygame.Rect(100, 500, 300, 25), 1)
        ]

    def update(self):
        self.screen.fill((0, 0, 0))
        for box in self.textboxes:
            box.update(self.screen)
        pygame.display.flip()
        self.input_enetered = None

    def mainloop(self):
        while self.gamestate:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = False
                elif event.type == pygame.KEYDOWN:
                    for box in self.textboxes:
                        if box.selected:
                            self.input_entered = box.char_add(event)
                            if self.input_entered:
                                print(self.input_entered)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for box in self.textboxes:
                            if box.rect.collidepoint(pygame.mouse.get_pos()):
                                box.selected = True
                            else:
                                box.selected = False
            self.update()


app = Control()
app.mainloop()