import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 60)


class Menu:
    def __init__(self):
        self._screen = pygame.display.get_surface()
        self._font = font
        self._color = (255, 255, 255)

    def draw_text(self, text, color, text_x, text_y):
        textobj = self._font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (text_x, text_y)
        self._screen.blit(textobj, textrect)

    def display_menu(self):
        self._screen.fill((0,0,0))
        self.draw_text('Press SPACE to play', self._color, 20, 20)
        self.draw_text('Press ESCAPE to return', self._color, 20, 80)
        self.draw_text('Press ESCAPE again to quit', self._color, 20, 170)