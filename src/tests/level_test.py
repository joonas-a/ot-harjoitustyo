import unittest
from level import Level

TEST_LEVEL= [
    [0, 0, 4],
    [0, 2, 4]
]


class TestLevel(unittest.TestCase):
    def setUp(self):
        self._level = Level(TEST_LEVEL, None)
        self._player = self._level.player
        self._platforms = self._level.platforms

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_reset_works(self):
        pass
