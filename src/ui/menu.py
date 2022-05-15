import os
import pygame

pygame.font.init()
DIRNAME = os.path.dirname(__file__)
FONT = pygame.font.Font(os.path.join(DIRNAME, "fonts", "PixeloidSansBold.ttf"), 64)


class Menu:
    def __init__(self):
        self._screen = pygame.display.get_surface()
        self._font = FONT
        self._color = (255, 150, 0)
        self._unavailable_color = (82, 40, 0)
        self._state = 0
        self._selector = Selector(self._screen, self._font)
        self._center = self._screen.get_width() / 2

    def draw_text(self, text, color, text_x, text_y):
        textobj = self._font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = (text_x, text_y)
        self._screen.blit(textobj, textrect)

    def display_menu(self):
        self._screen.fill((0, 0, 0))
        self.draw_text('Play', self._color, self._center, 180)
        self.draw_text('Controls', self._color, self._center, 250)
        self.draw_text('Reset save', self._color, self._center, 320)
        self.draw_text('Quit', self._color, self._center, 390)
        self._selector.draw_selector(self._state)

    def display_controls(self):
        self._screen.fill((0, 0, 0))
        self.draw_text('Move using the', self._color, self._center, 160)
        self.draw_text('arrow keys', self._color, self._center, 230)
        self.draw_text('Jump by clicking', self._color, self._center, 320)
        self.draw_text('the space bar', self._color, self._center, 390)
        self.draw_text('Go Back', self._color, self._center, 530)
        self._selector.draw_selector(5)

    def start_screen(self, saves):

        self._screen.fill((0, 0, 0))
        self.draw_text('Select a save', self._color, self._center, 80)
        self.draw_text(saves[0][1], self._color, self._center, 180)
        self.draw_text(saves[1][1], self._color, self._center, 250)
        self.draw_text(saves[2][1], self._color, self._center, 320)
        self.draw_text(saves[3][1], self._color, self._center, 390)
        self._selector.draw_selector(self._state)

    def reset_save(self, name):
        self._screen.fill((0, 0, 0))
        self.draw_text('Press DEL', (200, 0, 0), self._center, 160)
        self.draw_text('to reset', (200, 0, 0), self._center, 230)
        self.draw_text(name, (200, 0, 0), self._center, 320)
        self.draw_text('Go Back', self._color, self._center, 530)
        self._selector.draw_selector(5)

    def level_selector(self, highest):
        self._screen.fill((0, 0, 0))
        if highest == 0:
            self.draw_text('Stage 1', self._color, self._center, 180)
            self.draw_text('Stage 2', self._unavailable_color, self._center, 250)
            self.draw_text('Stage 3', self._unavailable_color, self._center, 320)
            self.draw_text('Stage 4', self._unavailable_color, self._center, 390)
        if highest == 1:
            self.draw_text('Stage 1', self._color, self._center, 180)
            self.draw_text('Stage 2', self._color, self._center, 250)
            self.draw_text('Stage 3', self._unavailable_color, self._center, 320)
            self.draw_text('Stage 4', self._unavailable_color, self._center, 390)
        if highest == 2:
            self.draw_text('Stage 1', self._color, self._center, 180)
            self.draw_text('Stage 2', self._color, self._center, 250)
            self.draw_text('Stage 3', self._color, self._center, 320)
            self.draw_text('Stage 4', self._unavailable_color, self._center, 390)
        if highest == 3:
            self.draw_text('Stage 1', self._color, self._center, 180)
            self.draw_text('Stage 2', self._color, self._center, 250)
            self.draw_text('Stage 3', self._color, self._center, 320)
            self.draw_text('Stage 4', self._color, self._center, 390)

        self._selector.draw_selector(self._state)

    def completed(self):
        self._screen.fill((0, 0, 0))
        self.draw_text('Congratulations!', (100, 250, 70), self._center, 230)
        self.draw_text('Go Back', self._color, self._center, 530)
        self._selector.draw_selector(5)

    def click_down(self):
        if self._state < 3:
            self._state += 1

    def click_up(self):
        if self._state > 0:
            self._state -= 1

    def reset_state(self):
        self._state = 0

    def get_state(self):
        return self._state

class Selector:
    def __init__(self, screen, font):
        self._screen = screen
        self._color = (255, 255, 255)
        self._font = font
        self._text_x = 70

    def _get_coordinates(self, state):
        return (self._text_x, 185 + state * 70)

    def draw_selector(self, state):
        textobj = self._font.render("->", 1, self._color)
        textrect = textobj.get_rect()
        textrect.center = self._get_coordinates(state)
        self._screen.blit(textobj, textrect)
