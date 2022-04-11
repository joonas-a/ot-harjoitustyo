import pygame
import entities

class Renderer:
    def __init__(self, screen, entities):
        self._screen = screen
        self._entities = entities

    def render(self):
        for entity in self._entities.all_entities():
            self._screen.blit(entity.surf, entity.rect)

        pygame.display.update()