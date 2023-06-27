import numpy as np

import config
from config import config
from config import game_config
from logic.general_logic import calculate_pins


class PlayerCoder:

    def generate_code(self):
        row_is_correct = True
        for column in range(config.COLUMNS):
            if game_config.board_guess[0][column] is None:
                row_is_correct = False

        if row_is_correct:
            game_config.board_final[0] = game_config.board_guess[0]
            game_config.solution = game_config.board_guess[0]
            game_config.computer_is_playing = True
            game_config.code_is_coded = True

    def rate_move(self, board_view, guesser):
        print("Solution:", game_config.solution)
        print("Guess:", game_config.board_final[game_config.current_row])
        black_temp, white_temp = calculate_pins(game_config.solution, game_config.board_final[game_config.current_row])

        white_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 7)
        black_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 8)

        print("Soll rauskommen")
        print("Black Pins:", black_temp)
        print("White Pins:", white_temp)
        print("Kommt raus")
        print("Black Pins:", black_pins)
        print("White Pins:", white_pins)

        if black_temp != black_pins or white_temp != white_pins:
            print("Falsche Bewertung")
            print(black_temp, white_temp)
            print(black_pins, white_pins)
            board_view.textfield_text = "Falsche Bewertung!"
            return

        # Der Geheimcode wurde erraten
        if black_pins is config.COLUMNS:
            game_config = True
            game_config.game_is_over = True
            return

        guesser.evaluate_feedback(black_pins, white_pins)
        game_config.current_row -= 1
        game_config.computer_is_playing = True

        # Es gibt keine Rateversuche mehr
        if game_config.current_row == 0:
            game_config.game_is_over = True
