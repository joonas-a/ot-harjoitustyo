import unittest
from level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        self._level = Level()
        self._player = self._level.player