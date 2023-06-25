import numpy as np

from config import config

player_is_guesser = None
current_row = 9 # unterste Reihe bei 10 Reihen
computer_is_playing = False

code_is_coded = False

solution = np.empty(config.COLUMNS, dtype=object)
solution[0] = (255, 0, 0)
solution[1] = (0, 255, 0)
solution[2] = (0, 0, 255)
solution[3] = (255, 255, 0)
solution[4] = (255, 0, 255)

# Erstellen des Rate-Boards
board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards mit allen logisch sinnvollen Eingaben
board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)
feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)