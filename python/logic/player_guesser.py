import config
from config import game_config
from config import config


class PlayerGuesser:
    """
    Klasse, die den Spielerrater repräsentiert.
    """

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

    def evaluate_feedback(self, black_pins, white_pins):
        """
        Bewertet das Feedback des Spielers.

        Args:
            black_pins (int): Die Anzahl der schwarzen Pins.
            white_pins (int): Die Anzahl der weißen Pins.
        """
        pass

    def guess(self, board_view):
        """
        Führt einen Rateversuch des Spielers aus.

        Args:
            board_view (BoardView): Die Ansicht des Spielbretts.

        Returns:
            bool: Gibt zurück, ob der Rateversuch korrekt ausgeführt wurde.
        """
        row_is_correct = True

        for column in range(config.COLUMNS):
            if game_config.board_guess[game_config.current_row][column] is None:
                row_is_correct = False

        if row_is_correct:
            game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
            game_config.computer_is_playing = True

        return row_is_correct
