import pygame

class Switch(pygame.sprite.Sprite):
    def __init__(self, cell_size, x_coord, y_coord):
        super().__init__()

        self.is_activated = False
        self.image = pygame.Surface((0.8 * cell_size, cell_size / 8))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect(bottomleft=(x_coord, y_coord + cell_size))

    def toggle_switch_on(self):
        self.is_activated = True

    def toggle_switch_off(self):
        self.is_activated = False

    def get_status(self):
        return self.is_activated
