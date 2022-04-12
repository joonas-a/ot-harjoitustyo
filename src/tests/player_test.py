import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self._player = Player()

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move(self):
        player = self._player

        x = player.position.x
        player