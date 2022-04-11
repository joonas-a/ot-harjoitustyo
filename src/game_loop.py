import pygame
import entities

class Application:
    def __init__(self, player, floor, renderer, event_queue, clock):
        self._player = player
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def run(self):
        while True:
            """for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        entities.player.jump()
                        
            screen.fill((0,0,0)) """
            if self._event_handler() == False:
                break

            self._player.update()
            self._player.movement()

            #for entity in entities.all_entities():
            #    screen.blit(entity.surf, entity.rect)

            self._render()
            self._clock.tick(60)

    def _event_handler(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                    return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entities.player.jump()
                    print("space")

    def _render(self):
        self._renderer.render()
