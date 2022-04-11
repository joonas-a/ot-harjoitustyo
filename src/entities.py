import pygame
from pygame.locals import *

x = 720 #game window measurements
y = 480
vector = pygame.math.Vector2
acceleration = 0.5
friction = -0.12

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 40))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()
        self.position = vector((20, 440))
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

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

    def jump(self):
        collision = pygame.sprite.spritecollide(player, platforms(), False)
        if collision:
            self.velocity.y = -15

    def update(self):
        check_collision = pygame.sprite.spritecollide(player, platforms(), False)
        if player.velocity.y > 0:
            if check_collision:
                self.position.y = check_collision[0].rect.top + 1
                self.velocity.y = 0

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((x, 20))
        self.surf.fill((150,75,0))
        self.rect = self.surf.get_rect(center = (x/2, y-10))

player = Player()
floor = Floor()

def platforms():
    platforms = pygame.sprite.Group()
    platforms.add(floor)
    return platforms    

def all_entities():
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(floor)
    return all_sprites