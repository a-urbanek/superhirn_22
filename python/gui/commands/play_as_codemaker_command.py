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
        print("Playing as CodeMaker")

        game_config.player_is_guesser = False
        self.main_app.set_state(GAME)
        # main_app._player_guesser_state = True

    def __str__(self):
        return "Play as CodeMaker"