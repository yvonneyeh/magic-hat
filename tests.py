import game
from game import Game
import unittest
from unittest import mock, TestCase


class TestGame(TestCase):


    def test_start(self):
        """
        Test for start of game.
        """
        magic_hat = Game()
        result = Game.start(magic_hat)
        self.assertEqual(result, game.STATUS_PLAYING)


if __name__ == '__main__':
    unittest.main()
