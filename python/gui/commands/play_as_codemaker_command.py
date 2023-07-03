# The PlayAsCodeMakerCommand class defines a command to play as a CodeMaker
from constants import GAME
from .command import Command
from config import game_config

import sys
sys.path.insert(0, '..')


# The PlayAsCodeMakerCommand class defines a command to play as a CodeMaker
class PlayAsCodeMakerCommand(Command):
    def execute(self):

        print("Executing Play As CodeMaker command...")

        game_config.player_is_guesser = False
        game_config.guesser_is_computer = True
        game_config.guesser_is_player = False
        game_config.coder_is_player = True

        if self.main_app.online_settings_model.online_mode:
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = False
            game_config.IP_ADDRESS = self.main_app.online_settings_model.ip_address
            game_config.PORT = self.main_app.online_settings_model.port

        else:
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = False

        self.main_app.start_new_game()

    def __str__(self):
        return "CodeMaker Spielen"
