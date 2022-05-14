import pygame

class Application:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._menu_state = 1

    def run(self):

        while True:

            if self._event_handler() is False:
                break
            if self._menu_state == 1 or self._menu_state == 2:
                self._level.in_menu(self._menu_state)
            else:
                self._level.update()
            self._render()
            self._clock.tick(60)

    def _event_handler(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and self._menu_state == -1:
                    self._level.player.jump()

                if event.key == pygame.K_DOWN and self._menu_state == 1:
                    self._level.menu.click_down()

                if event.key == pygame.K_UP and self._menu_state == 1:
                    self._level.menu.click_up()

                if event.key == pygame.K_ESCAPE and self._menu_state != 1:
                    self._menu_state = 1

                if event.key == pygame.K_RETURN and self._level.menu.get_state() == 3:
                    return False

                if event.key == pygame.K_RETURN and self._menu_state == 2:
                    self._menu_state = 1

                elif event.key == pygame.K_RETURN and self._menu_state == 1:
                    self._edit_menu_state(self._level.menu.get_state())

            return True


    def _edit_menu_state(self, state):
        if state == 0:
            self._menu_state = -1
        if state == 1:
            self._menu_state = 2
        if state == 2:
            self._level.reset()
            self._menu_state = 1
        if state == 3:
            self._menu_state = 1

    def _render(self):
        if self._menu_state != -1:
            self._renderer.render_menu()
        else:
            self._renderer.render()
