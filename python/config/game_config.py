import numpy as np

from config import config

# Variable, die angibt, ob der Spieler der Rater ist
player_is_guesser = None

# Aktuelle Reihe, auf der der Rater seinen Rateversuch macht (unterste Reihe bei 10 Reihen)
current_row = config.ROWS - 1

# Variable, die angibt, ob der Computer am Zug ist
computer_is_playing = False

# Variable, die angibt, ob der Computer über ein Netzwerk kommuniziert
computer_is_network = False

guesser_is_player = True
guesser_is_computer = False
coder_is_player = False
coder_is_computer_local = True
coder_is_computer_server = False
coder_is_playing = True
rate_was_correct = True
no_network_connection = False
error_message = ""

# IP-Adresse und Port für den Server
IP_ADDRESS = "127.0.0.1"
PORT = 8003
# IP_ADDRESS = "141.45.39.112"
# PORT = 5001

# Variable, die angibt, ob der Geheimcode bereits festgelegt wurde
code_is_coded = False

# Array, das den Geheimcode enthält
solution = np.empty(config.COLUMNS, dtype=object)

# Variable, die angibt, ob das Spiel vorbei ist
game_is_over = False

# Variable, die angibt, ob der Spieler gewonnen hat
player_won = False # muss raus

guesser_won = False

# Erstellen des Rate-Boards, auf dem der Spieler seinen Rateversuch macht
board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards, das alle logisch sinnvollen Eingaben enthält
board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)

# Erstellen des Boards, das die Bewertungen des Raters enthält
feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)
