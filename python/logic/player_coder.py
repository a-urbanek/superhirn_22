import numpy as np

import config
from config import config
from config import game_config
from logic.general_logic import calculate_pins


class PlayerCoder:
    """
    Klasse, die den Codegenerator repräsentiert.
    """

    def generate_code(self, board_view):
        """
        Generiert den Code des Spielers.

        Args:
            board_view (BoardView): Die Ansicht des Spielbretts.

        Returns:
            bool: Gibt zurück, ob der Code korrekt generiert wurde.
        """
        board_view.textfield_text = "Lege den Code in \nder ersten Reihe fest."
        row_is_correct = True
        for column in range(config.COLUMNS):
            if game_config.board_guess[0][column] is None:
                row_is_correct = False

        if row_is_correct:
            game_config.board_final[0] = game_config.board_guess[0]
            game_config.solution = game_config.board_guess[0]
            game_config.computer_is_playing = True
            game_config.code_is_coded = True

        return row_is_correct


    def rate_move(self, board_view, guesser):
        """
        Bewertet den aktuellen Zug des Spielers.

        Args:
            board_view (BoardView): Die Ansicht des Spielbretts.
            guesser (PlayerGuesser): Der Spielerrater.

        Returns:
            tuple: Ein Tupel bestehend aus der Anzahl der schwarzen Pins, der Anzahl der weißen Pins und ob die Bewertung korrekt war.
        """
        global game_config
        rate_was_correct = True
        black_temp, white_temp = calculate_pins(game_config.solution, game_config.board_final[game_config.current_row])

        white_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 7)
        black_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 8)

        if black_temp != black_pins or white_temp != white_pins:
            rate_was_correct = False
            black_pins = 0
            white_pins = 0
            return black_pins, white_pins, rate_was_correct

        # Der Geheimcode wurde erraten
        if black_pins == config.COLUMNS:
            game_config.game_is_over = True
            game_config.guesser_won = True
            black_pins = 5
            white_pins = 0
            rate_was_correct = True
            return black_pins, white_pins, rate_was_correct

        guesser.evaluate_feedback(black_pins, white_pins)
        game_config.current_row -= 1
        game_config.computer_is_playing = True

        # Es gibt keine Rateversuche mehr
        if game_config.current_row == 0:
            game_config.game_is_over = True

        return black_pins, white_pins, rate_was_correct
