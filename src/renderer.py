import pygame

class Renderer:
    def __init__(self, screen, level):
        self._screen = screen
        self._level = level

    def render(self):
        self._screen.fill((0, 0, 0))
        self._level.all_sprites.draw(self._screen)

        pygame.display.update()

    def render_menu(self):
        pygame.display.update()
