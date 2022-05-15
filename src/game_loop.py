import pygame

class Application:
    def __init__(self, level, renderer, event_queue, clock, save_id=1):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._menu_state = 10
        self._save_id = save_id

    def run(self):

        while True:

            if self._event_handler() is False:
                break

            if self._menu_state in (1, 2, 10, 20):
                self._level.in_menu(self._menu_state, self._save_id)

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

                if event.key == pygame.K_DOWN and self._menu_state in (1, 10, 20):
                    self._level.menu.click_down()

                if event.key == pygame.K_UP and self._menu_state in (1, 10, 20):
                    self._level.menu.click_up()

                if event.key == pygame.K_ESCAPE and self._menu_state not in (1, 10):
                    self._menu_state = 1

                elif event.key == pygame.K_ESCAPE and self._menu_state == 1:
                    self._menu_state = 10

                if event.key == pygame.K_RETURN and self._menu_state == 1 \
                and self._level.get_menu_state() == 3:
                    return False

                if event.key == pygame.K_RETURN and self._menu_state == 2:
                    self._menu_state = 1

                elif event.key == pygame.K_RETURN and self._menu_state in (1, 10, 20):
                    self._edit_menu_state(self._menu_state, self._level.get_menu_state())

            #return True #clears pylint error, however causes X button to not function

    def _edit_menu_state(self, state, selector):
        if state == 1: #main menu
            if selector == 0:
                self._menu_state = 20
            if selector == 1:
                self._menu_state = 2
            if selector == 2:
                self._level.reset()
                self._menu_state = 1
            if selector == 3:
                self._menu_state = 1

        if state == 10: #save selection
            self._level.load_save(selector + 1)
            self._save_id = selector + 1
            self._menu_state = 1

        if state == 20: #stage selection
            if self._level.load_stage(selector):
                self._menu_state = -1

    def _render(self):
        if self._menu_state != -1:
            self._renderer.render_menu()
        else:
            self._renderer.render()
