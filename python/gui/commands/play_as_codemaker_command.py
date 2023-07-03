from .command import Command
from config import game_config

import sys
sys.path.insert(0, '..')
from constants import GAME


# The PlayAsCodeMakerCommand class defines a command to play as a CodeMaker.
class PlayAsCodeMakerCommand(Command):
    def execute(self):
        """
        This function sets the state of the main app to "GAME"
        
        :param main_app: main_app is an instance of the main application class that this method belongs to.
        It is passed as a parameter to the method so that the method can access and modify the state of the
        main application
        """
        if self.main_app.online_settings_model.online_mode:
            return print("Nicht erlaubt für Online Mode")

        print("Playing as CodeMaker")

        game_config.player_is_guesser = False
        game_config.guesser_is_computer = True
        game_config.guesser_is_player = False

        game_config.coder_is_player = True
        game_config.coder_is_computer_local = False
        game_config.coder_is_computer_server = False
        self.main_app.start_new_game()
        # main_app._player_guesser_state = True

    def __str__(self):
        return "CodeMaker Spielen"