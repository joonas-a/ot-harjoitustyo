import unittest
import pygame
from level import Level
from game_loop import Application

class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

class TestLoop(unittest.TestCase):
    def setUp(self):
        self._level = Level()
        self._player = self._level.player

    def test_can_move_player(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_r),
            StubEvent(pygame.KEYUP, pygame.K_r),
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)
        ]
        loop = Application(
            self._level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        loop._in_menu = False
        loop.run()

        self.assertEqual(self._player.acceleration.x, 12)
