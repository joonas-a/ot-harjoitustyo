import pygame
from ui.menu import Menu
from stages import STAGE_1, STAGE_2, STAGE_3, STAGE_4
import queries
from sprites.player import Player
from sprites.floor import Floor
from sprites.switch import Switch
from sprites.door import Door

CELL_SIZE = 40

ALL_STAGES = [STAGE_1, STAGE_2, STAGE_3, STAGE_4]


class Level:
    def __init__(self, current_stage=ALL_STAGES[0], save_id=1):
        self.current_stage = current_stage #this can be hard-coded for testing
        self.save_id = save_id
        self.player = None
        self.floor = pygame.sprite.Group()
        self.removable_floor = pygame.sprite.Group()
        self.transparent_floor = pygame.sprite.Group()
        self.ghost_floor = pygame.sprite.Group()
        self.switch = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.menu = Menu()
        self.cell_size = CELL_SIZE

        self._initialize_sprites(self.current_stage)


    def in_menu(self, option, save_id=1):
        if option == 1:
            self.menu.display_menu()
        if option == 2:
            self.menu.display_controls()
        if option == 3:
            self.menu.reset_save(queries.get_name(self.save_id))
        if option == 10:
            self.menu.start_screen(queries.get_saves())
        if option == 20:
            highest = queries.get_completed(save_id)
            self.menu.level_selector(highest)
        if option == 100:
            self.menu.completed()

    def get_menu_state(self):
        return self.menu.get_state()

    def update(self):
        self.player.movement()
        self.player.horizontal_collision(self.platforms)
        self.player.vertical_collision(self.platforms)
        if self.player.check_switch_activation(self.switch):
            self.toggle_transparent_blocks()
        if self.player.check_level_completion(self.door):
            self.next_stage()
        if self.player.check_falling_out_of_map():
            self.reset()

    def reset(self):
        self.__init__(self.current_stage, self.save_id)

    def reset_menu_selector(self):
        self.menu.reset_state()

    def has_access_to_stage(self, stage):
        highest = queries.get_completed(self.save_id)
        return highest >= stage

    def load_stage(self, stage: int):
        if self.has_access_to_stage(stage):
            self.__init__(ALL_STAGES[stage], self.save_id)
            return True
        return False

    def load_save(self, save_id):
        self.save_id = save_id

    def reset_save(self):
        queries.set_highest(0, self.save_id)

    def next_stage(self):
        if self.current_stage == STAGE_1:
            queries.set_highest(1, self.save_id)
            self.__init__(STAGE_2, self.save_id)
        elif self.current_stage == STAGE_2:
            queries.set_highest(2, self.save_id)
            self.__init__(STAGE_3, self.save_id)
        elif self.current_stage == STAGE_3:
            queries.set_highest(3, self.save_id)
            self.__init__(STAGE_4, self.save_id)

    def is_completed(self):
        if self.current_stage == STAGE_4:
            if self.player.check_level_completion(self.door):
                return True
        return False

    def toggle_transparent_blocks(self):
        self.platforms.remove(self.removable_floor)
        self.all_sprites.remove(self.removable_floor)
        self.all_sprites.add(self.ghost_floor)
        self.platforms.add(self.ghost_floor)

    def get_player_coordinates(self):
        if self.current_stage == STAGE_1:
            return (0, 520)
        if self.current_stage == STAGE_2:
            return (0, 80)
        if self.current_stage == STAGE_3:
            return (240, 40)
        if self.current_stage == STAGE_4:
            return (0, 40)
        return (0, 0)

    def _initialize_sprites(self, level):
        self.player = Player(self.get_player_coordinates())

        for row_index, row in enumerate(level):
            for column_index, cell in enumerate(row):
                x_coord = column_index * self.cell_size
                y_coord = row_index * self.cell_size

                if cell == 1:
                    self.floor.add(Floor(self.cell_size, x_coord, y_coord))
                if cell == 2:
                    self.switch.add(Switch(self.cell_size, x_coord, y_coord))
                if cell == 3:
                    self.transparent_floor.add(Floor(self.cell_size, x_coord, y_coord, (40, 20, 0)))
                    self.removable_floor.add(Floor(self.cell_size, x_coord, y_coord))
                if cell == 4:
                    self.door.add(Door(self.cell_size, x_coord, y_coord))
                if cell == 5:
                    self.ghost_floor.add(Floor(self.cell_size, x_coord, y_coord, (100, 100, 100)))

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
