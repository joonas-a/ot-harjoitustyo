import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self._player = Player((0, 0))

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_jump(self):
        self._player.on_ground = True
        self._player.jump()
        self.assertEqual(self._player.velocity.y, self._player.jump_height)

    def test_can_double_jump(self):
        self._player.jump()
        self.assertEqual(self._player.velocity.y, self._player.double_jump_height)

    def test_gravity_works(self):
        self.assertEqual(self._player.velocity.y, 0)
        self._player._apply_gravity()
        self.assertNotEqual(self._player.velocity.y, 0)
