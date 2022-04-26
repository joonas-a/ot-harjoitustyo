import pygame

class Application:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._in_menu = True

    def run(self):

        while True:

            if self._event_handler() is False:
                break
            if self._in_menu:
                self._level.in_menu()
            else:
                self._level.update()

            self._render()
            self._clock.tick(60)

    def _event_handler(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self._in_menu:
                        self._in_menu = False
                    else:
                        self._level.player.jump(
                            self._level.player, self._level.platforms)
                if event.key == pygame.K_ESCAPE:
                    if self._in_menu:
                        return False
                    self._in_menu = True


    def _render(self):
        if self._in_menu:
            self._renderer.render_menu()
        else:
            self._renderer.render()
