import pygame
from menu import Menu
from sprites.player import Player
from sprites.floor import Floor
from sprites.switch import Switch
from sprites.transparent_floor import TransparentFloor
from sprites.door import Door

CELL_SIZE = 40

LEVEL_1_STAGE_1 = [
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
LEVEL_1_STAGE_2 = [
    [0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 2],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
]

class Level:
    def __init__(self, current_stage):
        self.current_stage = current_stage
        self.player = None
        self.floor = pygame.sprite.Group()
        self.removable_floor = pygame.sprite.Group()
        self.transparent_floor = pygame.sprite.Group()
        self.switch = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.menu = Menu()
        self.cell_size = CELL_SIZE

        self._initialize_sprites(self.current_stage)

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
        if self.player.check_switch_activation(self.switch):
            self.toggle_transparent_blocks()
        if self.player.check_level_completion(self.door):
            self.next_stage()

    def reset(self):
        self.__init__(self.current_stage)

    def next_stage(self):
        if self.current_stage == LEVEL_1_STAGE_1:
            self.__init__(LEVEL_1_STAGE_2)

    def toggle_transparent_blocks(self):
        self.platforms.remove(self.removable_floor)
        self.all_sprites.remove(self.removable_floor)

    def get_player_coordinates(self):
        if self.current_stage == LEVEL_1_STAGE_1:
            return (0, 520)
        if self.current_stage == LEVEL_1_STAGE_2:
            return (0, 80)

    def _initialize_sprites(self, level):
        self.player = Player(self.get_player_coordinates())

        for row_index, row in enumerate(level):
            for column_index, cell in enumerate(row):
                x_coordinate = column_index * self.cell_size
                y_coordinate = row_index * self.cell_size

                if cell == 1:
                    self.floor.add(Floor(self.cell_size, x_coordinate, y_coordinate))
                if cell == 2:
                    self.switch.add(Switch(self.cell_size, x_coordinate, y_coordinate))
                if cell == 3:
                    self.transparent_floor.add(TransparentFloor(self.cell_size, x_coordinate, y_coordinate))
                    self.removable_floor.add(Floor(self.cell_size, x_coordinate, y_coordinate))
                if cell == 4:
                    self.door.add(Door(self.cell_size, x_coordinate, y_coordinate))

        # affects the order in which the sprites are drawn
        self.all_sprites.add(
            self.transparent_floor,
            self.removable_floor,
            self.floor,
            self.switch,
            self.door,
            self.player
        )
        self.platforms.add(
            self.floor,
            self.removable_floor
        )
