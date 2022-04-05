import pygame

def application():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([720, 480])
    pygame.display.set_caption('Platformer')

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



    pygame.quit()

if __name__ == "__main__":
    application()