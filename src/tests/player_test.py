import unittest
from level import Level


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self._level = Level()
        self._player = self._level.player
        self._platforms = self._level.platforms

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_jump_velocity_check(self):
        self._player.jump(self._player, self._platforms)
        self.assertEqual(self._player.velocity.y, -10)
"""
    def test_no_falling_through_floor(self):
        self.assertEqual(self._player.velocity.y, 0)

    def test_gravity_works(self):
        self.assertEqual(self._player.velocity.y, 0)
        self._player.movement()
        self.assertEqual(self._player.velocity.y, 0)"""