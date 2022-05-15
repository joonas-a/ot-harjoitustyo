import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, cell_size, x_coord, y_coord):
        super().__init__()

        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((80, 200, 0))
        self.rect = self.image.get_rect(topleft=(x_coord, y_coord))