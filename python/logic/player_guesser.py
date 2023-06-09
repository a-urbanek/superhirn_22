from config import game_config

class PlayerGuesser:
    def __init__(self):
        self.example = []

    def method_one(self):
        print("ComputerGuesser: Methode 1")
        return None

    def make_move(self):
        # Wurden in der richtigen Reihe überall Farben gesetzt?
        allColorsAreSelected = True

        for element in game_config.board_guess[game_config.current_row]:
            if element is None:
                allColorsAreSelected = False

        # Abgegebene Row an das finale Board übertragen
        if allColorsAreSelected:
            game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
            game_config.computer_is_playing = True
        return