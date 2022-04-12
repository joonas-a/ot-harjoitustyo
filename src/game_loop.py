import pygame


class Application:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def run(self):
        while True:

            if self._event_handler() is False:
                break

            self._level.update()

            self._render()
            self._clock.tick(60)

    def _event_handler(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._level.player.jump(
                        self._level.player, self._level.platforms)

    def _render(self):
        self._renderer.render()
