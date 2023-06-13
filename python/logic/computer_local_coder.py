import random
import numpy as np

from config import game_config
from config import config

class ComputerLocalCoder:
    def __init__(self):
        self.current_guess = np.empty(config.COLUMNS, dtype=object)
        self.solution_temp = game_config.solution
        self.red_pins = 0
        self.white_pins = 0

    def rate_moe(self):
        """
        Bewertet den aktuellen Zug des Spielers.
        """
        self.current_guess = np.array(game_config.board_final[game_config.current_row])
        self.red_pins = np.sum(self.current_guess == self.solution_temp)
        self.white_pins = np.intersect1d(self.current_guess, self.solution_temp, assume_unique=True).size - self.red_pins
        print("White Pins: ", self.white_pins)
        print("Red Pins: ", self.red_pins)
        game_config.computer_is_playing = False
        game_config.current_row = game_config.current_row - 1
        return self.red_pins, self.white_pins

    def generate_code(self):
        """
        Generiert einen zufälligen Code als Lösung für das Spiel.
        """
        solution = random.choices(config.COLORS, k=5)
        game_config.solution = solution
        return solution
