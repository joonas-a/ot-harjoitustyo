import pygame
from pygame.locals import *
from sprites.player import Player
from sprites.floor import Floor

x = 720 #game window measurements
y = 480
vector = pygame.math.Vector2
acceleration = 0.5
friction = -0.12

class Level:
    def __init__(self):
        self.floor = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
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