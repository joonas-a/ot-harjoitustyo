import pygame

class Switch(pygame.sprite.Sprite):
    """Luokka painikelaatalle

        Attributes:
        cell_size: laatan koko, minä se renderöidään tasolle
        x,y_coord: laatan sijoitus x,y-koordinaatistolla
        color: laatan väri, default harmaa
    """
    def __init__(self, cell_size, x_coord, y_coord):
        super().__init__()

        self.is_activated = False
        self.image = pygame.Surface((0.8 * cell_size, cell_size / 8))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect(bottomleft=(x_coord + 0.1 * cell_size \
            , y_coord + cell_size))
