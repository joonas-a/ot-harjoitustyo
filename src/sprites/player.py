import pygame
from pygame.locals import *

vector = pygame.math.Vector2
acceleration = 1
friction = -0.12

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((25, 40))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.position = vector((20, 580))
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)
        self.dbjump = True

    def movement(self):
        self.acceleration = vector(0, 0.5) #allow gravity
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_LEFT]:
            self.acceleration.x = -acceleration
        if pressed_key[K_RIGHT]:
            self.acceleration.x = +acceleration

        self.acceleration.x += self.velocity.x * friction
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.midbottom = self.position

    def jump(self, player, platforms):
        collision = pygame.sprite.spritecollide(player, platforms, False)
        if collision:
            self.velocity.y = -15
        if not collision and self.dbjump == True:
                self.dbjump = False
                self.velocity.y = -10

    def update(self, player, platforms):
        check_collision = pygame.sprite.spritecollide(player, platforms, False)
        if player.velocity.y > 0:
            if check_collision:
                self.position.y = check_collision[0].rect.top + 1
                self.velocity.y = 0
                self.dbjump = True