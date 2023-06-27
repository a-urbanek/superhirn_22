import config
from config import game_config


class PlayerGuesser:

    def make_move(self):
        """
        Führt einen Rateversuch des Spielers aus.
        """
        # Überprüfen, ob in der aktuellen Reihe alle Farben ausgewählt wurden
        allColorsAreSelected = True

        for element in game_config.board_guess[game_config.current_row]:
            if element is None:
                allColorsAreSelected = False

        # Übertragen der abgegebenen Reihe auf das finale Board
        if allColorsAreSelected:
            game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
            game_config.computer_is_playing = True

        return

    def guess(self):
        row_is_correct = True
        for column in range(config.COLUMNS):
            if game_config.board_guess[game_config.current_row][column] is None:
                row_is_correct = False

        if row_is_correct:
            game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
            game_config.computer_is_playing = True
