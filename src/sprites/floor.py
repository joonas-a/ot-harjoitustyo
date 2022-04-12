import pygame

x = 800 #game window size
y = 600

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((x, 20))
        self.image.fill((150,75,0))
        self.rect = self.image.get_rect(center = (x/2, y-10))