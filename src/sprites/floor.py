import pygame

X = 800  # game window size
Y = 600


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((X, 20))
        self.image.fill((150, 75, 0))
        self.rect = self.image.get_rect(center=(X/2, Y-10))
