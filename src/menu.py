import pygame
import os

pygame.font.init()
dirname = os.path.dirname(__file__)
font = pygame.font.Font(os.path.join(dirname, "fonts", "PixeloidSansBold.ttf"), 64)


class Menu:
    def __init__(self):
        self._screen = pygame.display.get_surface()
        self._font = font
        self._color = (255, 150, 0)
        self._selected_color = (255, 230, 0)
        self._state = 0
        self._selector = Selector(self._screen, self._font)

    def draw_text(self, text, color, text_x, text_y):
        textobj = self._font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = (text_x, text_y)
        self._screen.blit(textobj, textrect)

    def display_menu(self):
        self._screen.fill((0, 0, 0))
        self.draw_text('Play', self._color, self._screen.get_width() / 2, 180)
        self.draw_text('Controls', self._color, self._screen.get_width() / 2, 250)
        self.draw_text('Reset level', self._color, self._screen.get_width() / 2, 320)
        self.draw_text('Quit', self._color, self._screen.get_width() / 2, 390)
        self._selector.draw_selector(self._state)

    def display_controls(self):
        self._screen.fill((0, 0, 0))
        self.draw_text('Move using the', self._color, self._screen.get_width() / 2, 160)
        self.draw_text('arrow keys', self._color, self._screen.get_width() / 2, 230)
        self.draw_text('Jump by clicking', self._color, self._screen.get_width() / 2, 320)
        self.draw_text('the space bar', self._color, self._screen.get_width() / 2, 390)
        self.draw_text('Back', self._color, self._screen.get_width() / 2, 530)
        self._selector.draw_selector(5)


    def click_down(self):
        if self._state < 3:
            self._state += 1

    def click_up(self):
        if self._state > 0:
            self._state -= 1

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
