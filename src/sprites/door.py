import pygame


class Door(pygame.sprite.Sprite):
    """Luokka ovelle tasolla. Ovi on pääsääntöisesti maali joka tasolla.

        Attributes:
        cell_size: oven koko, minä se renderöidään tasolle
        x,y_coord: oven sijoitus x,y-koordinaatistolla
        color: oven väri, default vihreä
    """
    def __init__(self, cell_size, x_coord, y_coord):
        super().__init__()

        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((80, 200, 0))
        self.rect = self.image.get_rect(topleft=(x_coord, y_coord))
