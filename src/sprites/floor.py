import pygame


class Floor(pygame.sprite.Sprite):
    """Luokka tavalliselle lattiapalikalle

        Attributes:
        cell_size: palikan koko, minä se renderöidään tasolle
        x,y_coord: palikan sijoitus x,y-koordinaatistolla
        color: palikan väri, default oranssi
    """
    def __init__(self, cell_size, x_coord, y_coord, color=(150, 75, 0)):
        super().__init__()

        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((color))
        self.rect = self.image.get_rect(topleft=(x_coord, y_coord))
