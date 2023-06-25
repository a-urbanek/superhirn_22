from collections import Counter
import numpy as np
from config import config
from config import game_config

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
        self.solution_temp = game_config.solution
        self.current_guess = np.array(game_config.board_final[game_config.current_row])
        self.red_pins = self.count_red_pins()
        self.white_pins = self.count_white_pins()

        print("Number of white pins:", self.white_pins)
        print("Number of red pins:", self.red_pins)

        # game_config.computer_is_playing = False
        # game_config.current_row -= 1

        return self.red_pins, self.white_pins

    def count_red_pins(self):
        """
        Zählt die Anzahl der roten Pins (richtige Farbe an richtiger Position).
        """
        red_pins = 0
        for i in range(len(self.current_guess)):
            if self.current_guess[i] == self.solution_temp[i]:
                red_pins += 1
                self.current_guess[i] = None

        return red_pins

    def count_white_pins(self):
        """
        Zählt die Anzahl der weißen Pins (richtige Farbe an falscher Position).
        """
        white_pins = 0
        for i in range(len(self.current_guess)):
            if self.current_guess[i] is not None and np.any(self.current_guess[i] == self.solution_temp):
                index = np.where(self.current_guess[i] == self.solution_temp)[0][0]
                white_pins += 1
                self.solution_temp[index] = -1  # Platzhalterwert, der nicht mit den tatsächlichen Elementen kollidiert

        return white_pins

    def generate_code(self):
        """
        Generiert einen zufälligen Code als Lösung für das Spiel.
        """
        solution = np.random.choice(config.COLORS_NUMBERS, size=config.COLUMNS)
        game_config.solution = solution
        game_config.code_is_coded = True
        print("Code created:", solution)
        return solution
