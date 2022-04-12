import pygame
from sprites.player import Player
from sprites.floor import Floor


class Level:
    def __init__(self):
        self.floor = pygame.sprite.Group()
        self.player = None
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self._initialize_sprites()

    def update(self):
        self.player.movement()
        self.player.update(self.player, self.platforms)

    def _initialize_sprites(self):
        self.player = Player()
        self.floor = Floor()

        self.all_sprites.add(
            self.floor,
            self.player
        )

        self.platforms.add(
            self.floor
        )
