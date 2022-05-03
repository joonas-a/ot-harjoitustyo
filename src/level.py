import pygame
from menu import Menu
from sprites.player import Player
from sprites.floor import Floor


class Level:
    def __init__(self):
        self.floor = pygame.sprite.Group()
        self.player = None
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.menu = Menu()

        self._initialize_sprites()

    def in_menu(self, option):
        if option == 1:
            self.menu.display_menu()
        if option == 2:
            self.menu.display_controls()


    def in_controls(self):
        self.menu.display_controls()

    def update(self):
        self.player.movement()
        self.player.update(self.player, self.platforms)

    def reset(self):
        self.__init__()

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
