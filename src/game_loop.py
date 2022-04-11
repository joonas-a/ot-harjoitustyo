import pygame
import entities

width = 720
height = 480
fps = 60

def application():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Platformer')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entities.player.jump()
                    
        screen.fill((0,0,0))

        entities.player.update()
        entities.player.movement()

        for entity in entities.all_entities():
            screen.blit(entity.surf, entity.rect)

        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    application()