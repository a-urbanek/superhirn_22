from config import game_config
from config import config
import numpy as np

class ComputerLocalCoder:
    def __init__(self):
        self.current_guess = np.empty(config.COLUMNS, dtype=object)
        self.solution_temp = game_config.solution
        self.red_pins = 0
        self.white_pins = 0

    def method_one(self):
        print("ComputerCoder: Methode 1")

    def rate_moe(self):
        self.current_guess = np.array(game_config.board_final[game_config.current_row])
        # Ermittle die Anzahl der identischen Symbole
        self.red_pins = np.sum(self.current_guess == self.solution_temp)
        # Ermittle die Anzahl der Symbole mit unterschiedlichen Indizes und Werten
        self.white_pins = np.intersect1d(self.current_guess, self.solution_temp, assume_unique=True).size - self.red_pins
        print("White Pins: ", self.white_pins)
        print("Red Pins: ", self.red_pins)
        game_config.computer_is_playing = False
        game_config.current_row = game_config.current_row - 1
        return self.red_pins, self.white_pins