import unittest
from level import Level
from game_loop import Application


class TestLoop(unittest.TestCase):
    def setUp(self):
        self._level = Level()
        self._player = self._level.player
