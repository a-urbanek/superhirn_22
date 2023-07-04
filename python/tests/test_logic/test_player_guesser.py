import unittest
import numpy as np

from config import config, game_config
from logic.player_guesser import PlayerGuesser


class TestPlayerGuesser(unittest.TestCase):
    def setUp(self):
        self.player_guesser = PlayerGuesser()
        game_config.board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.current_row = config.ROWS - 1

    def test_make_move_with_incomplete_guess(self):
        """
        Testet die make_move Methode, wenn die aktuelle Reihe nicht vollständig ist.
        """
        game_config.BOARD_GUESS[game_config.CURRENT_ROW][0] = 'Red'
        self.player_guesser.make_move()
        self.assertFalse(game_config.COMPUTER_IS_PLAYING)

    def test_make_move_with_complete_guess(self):
        """
        Testet die make_move Methode, wenn die aktuelle Reihe vollständig ist.
        """
        for i in range(config.COLUMNS):
            game_config.BOARD_GUESS[game_config.CURRENT_ROW][i] = 'Red'
        self.player_guesser.make_move()
        self.assertTrue(game_config.COMPUTER_IS_PLAYING)
        self.assertListEqual(game_config.BOARD_GUESS[game_config.CURRENT_ROW].tolist(),
                             game_config.BOARD_FINAL[game_config.CURRENT_ROW].tolist())

    def test_guess_with_incomplete_guess(self):
        """
        Testet die guess Methode, wenn die aktuelle Reihe unvollständig ist.
        """
        game_config.BOARD_GUESS[game_config.CURRENT_ROW][0] = 'Red'
        result = self.player_guesser.guess(None)
        self.assertFalse(result)

    def test_guess_with_complete_guess(self):
        """
        Testet die guess Methode, wenn die aktuelle Reihe vollständig ist.
        """
        for i in range(config.COLUMNS):
            game_config.BOARD_GUESS[game_config.CURRENT_ROW][i] = 'Red'
        result = self.player_guesser.guess(None)
        self.assertTrue(result)

    def test_make_move_without_guess(self):
        """
        Testet die make_move Methode ohne Rateversuch.
        """
        self.player_guesser.make_move()
        self.assertFalse(game_config.COMPUTER_IS_PLAYING)

    def test_make_move_with_one_color_guessed(self):
        """
        Testet die make_move Methode mit einer Farbe geraten.
        """
        game_config.BOARD_GUESS[game_config.CURRENT_ROW][0] = 'Red'
        self.player_guesser.make_move()
        self.assertFalse(game_config.COMPUTER_IS_PLAYING)

    def test_guess_without_guess(self):
        """
        Testet die guess Methode ohne Rateversuch.
        """
        result = self.player_guesser.guess(None)
        self.assertFalse(result)

    def test_guess_with_one_color_guessed(self):
        """
        Testet die guess Methode mit einer Farbe geraten.
        """
        game_config.BOARD_GUESS[game_config.CURRENT_ROW][0] = 'Red'
        result = self.player_guesser.guess(None)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
