import unittest
import pygame
import game_loop

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game = game_loop.application()

    def test_application_opens_successfully(self):
        self.assertEqual(self.game.running, True)