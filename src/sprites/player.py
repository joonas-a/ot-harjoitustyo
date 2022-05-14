import pygame

VECTOR = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.default_pos = (20, 520)
        self.image = pygame.Surface((25, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft = (self.default_pos))
        self.velocity = VECTOR(0, 0)

        self.speed = 5
        self.gravity = 0.5
        self.jump_height = -11
        self.double_jump_height = -8
        self.dbjump = True
        self.on_ground = False

    def movement(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif pressed_key[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.on_ground = False
            self.velocity.y = self.jump_height
        elif not self.on_ground and self.dbjump is True:
            self.dbjump = False
            self.velocity.y = self.double_jump_height

    def _apply_gravity(self):
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y

    def horizontal_collision(self, tiles):
        self.rect.x += self.velocity.x

        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.velocity.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.velocity.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collision(self, tiles):
        self._apply_gravity()

        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                    self.dbjump = True
                elif self.velocity.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.velocity.y = 0
        
        if self.velocity.y > 1:
            self.on_ground = False
