from config import game_config


class PlayerGuesser:
    def __init__(self):
        # Initialisierung des PlayerGuesser-Objekts
        # Hier können ggf. weitere Initialisierungen vorgenommen werden
        pass

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
