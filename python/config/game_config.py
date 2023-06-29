import numpy as np

from config import config

# Variable, die angibt, ob der Spieler der Rater ist
player_is_guesser = None

# Aktuelle Reihe, auf der der Rater seinen Rateversuch macht (unterste Reihe bei 10 Reihen)
current_row = config.ROWS - 1

# Variable, die angibt, ob der Computer am Zug ist
computer_is_playing = False

# Variable, die angibt, ob der Geheimcode bereits festgelegt wurde
code_is_coded = False

# Array, das den Geheimcode enthält
solution = np.empty(config.COLUMNS, dtype=object)

# Variable, die angibt, ob das Spiel vorbei ist
game_is_over = False

# Variable, die angibt, ob der Spieler gewonnen hat
player_won = False

# Erstellen des Rate-Boards, auf dem der Spieler seinen Rateversuch macht
board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards, das alle logisch sinnvollen Eingaben enthält
board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards, das die Bewertungen des Raters enthält
feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)
