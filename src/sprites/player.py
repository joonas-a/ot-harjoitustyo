import pygame

VECTOR = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """Luokka pelattavalle hahmolle. Valtaosa pelihahmoon liittyvästä logiikasta tapahtuu täällä.
        Metodeita kutsutaan pääasiassa Level-luokasta, joka vastaa pelin päälogiikasta.

        Attributes:
            position: määrittelee mihin pelihahmo sijoitetaan x,y koordinaatistolla pelitasoa alustaessa
    """
    def __init__(self, position):
        super().__init__()

        self.image = pygame.Surface((25, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft = (position))
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
        right_limit = pygame.display.get_window_size()[0]

        # prevent walking off-screen horizontally
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= right_limit:
            self.rect.right = right_limit

        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.velocity.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.velocity.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collision(self, tiles):
        self._apply_gravity()

        # prevent jumping off-screen
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y = 0
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

    def check_switch_activation(self, switches):
        for sprite in switches.sprites():
            if sprite.rect.colliderect(self.rect):
                return True
        return False

    def check_level_completion(self, door):
        for sprite in door.sprites():
            if sprite.rect.colliderect(self.rect):
                return True
        return False

    def check_falling_out_of_map(self):
        bottom = pygame.display.get_window_size()[1]
        if self.rect.top > bottom:
            return True
        return False
