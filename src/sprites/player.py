import pygame
from pygame.locals import K_LEFT, K_RIGHT

VECTOR = pygame.math.Vector2
ACCELERATION = 0.5
FRICTION = -0.12


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((25, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.position = VECTOR((20, 580))
        self.velocity = VECTOR(0, 0)
        self.acceleration = VECTOR(0, 0)
        self.dbjump = True

    def movement(self):
        self.acceleration = VECTOR(0, 0.5)  # allow gravity
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_LEFT]:
            self.acceleration.x = -ACCELERATION
        if pressed_key[K_RIGHT]:
            self.acceleration.x = +ACCELERATION

        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.midbottom = self.position

    def jump(self, player, platforms):
        collision = pygame.sprite.spritecollide(player, platforms, False)
        if collision:
            self.velocity.y = -15
        if not collision and self.dbjump is True:
            self.dbjump = False
            self.velocity.y = -10

    def update(self, player, platforms):
        check_collision = pygame.sprite.spritecollide(player, platforms, False)
        if player.velocity.y > 0:
            if check_collision:
                self.position.y = check_collision[0].rect.top + 1
                self.velocity.y = 0
                self.dbjump = True
