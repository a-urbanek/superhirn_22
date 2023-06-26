import numpy as np

from config import config

player_is_guesser = None
current_row = config.ROWS - 1 # unterste Reihe bei 10 Reihen
computer_is_playing = False
computer_is_network = True

code_is_coded = False

solution = np.empty(config.COLUMNS, dtype=object)

game_is_over = False
player_won = False

# Erstellen des Rate-Boards
board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards mit allen logisch sinnvollen Eingaben
board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)
feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)