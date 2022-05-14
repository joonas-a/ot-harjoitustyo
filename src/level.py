import pygame
from menu import Menu
from sprites.player import Player
from sprites.floor import Floor

CELL_SIZE = 40

LEVEL_1_STAGE_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Level:
    def __init__(self):
        self.floor = pygame.sprite.Group()
        self.player = None
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.menu = Menu()
        self.cell_size = CELL_SIZE

        self._initialize_sprites(LEVEL_1_STAGE_1)

    def in_menu(self, option):
        if option == 1:
            self.menu.display_menu()
        if option == 2:
            self.menu.display_controls()


    def in_controls(self):
        self.menu.display_controls()

    def update(self):
        #self.player.update(self.player, self.platforms)
        self.player.movement()
        self.player.horizontal_collision(self.platforms)
        self.player.vertical_collision(self.platforms)

    def reset(self):
        self.__init__()

    def _initialize_sprites(self, level):
        self.player = Player()

        for row_index, row in enumerate(level):
            for column_index, cell in enumerate(row):
                x_coordinate = column_index * self.cell_size
                y_coordinate = row_index * self.cell_size

                if cell == 1:
                    self.floor.add(Floor(self.cell_size, x_coordinate, y_coordinate))

        self.all_sprites.add(
            self.floor,
            self.player
        )
        self.platforms.add(
            self.floor
        )
