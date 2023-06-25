from config import game_config
from .command import Command

import sys
sys.path.insert(0, '..')
from constants import GAME

# The PlayAsCodeBreakerCommand class defines a command to play as a code breaker.
class PlayAsCodeBreakerCommand(Command):
    def execute(self, main_app):
        """
        This function sets the state of the main app to "GAME"
        
        :param main_app: main_app is an instance of the main application class that this method belongs to.
        It is passed as a parameter to the method so that the method can access and modify the state of the
        main application
        """
        print("Playing as CodeBreaker")
        game_config.player_is_guesser = True
        main_app._state = GAME
        # main_app._player_guesser_state = False

    def __str__(self):
        return "Play as CodeBreaker"