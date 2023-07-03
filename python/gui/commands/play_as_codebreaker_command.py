# The PlayAsCodeBreakerCommand class defines a command to set the state of the main app to "GAME" when
# playing as a code breaker.
from config import game_config

from .command import Command
import sys
sys.path.insert(0, '..')
from constants import GAME

# The PlayAsCodeBreakerCommand class defines a command to play as a code breaker.
class PlayAsCodeBreakerCommand(Command):
    def execute(self):
        """
        This function sets the state of the main app to "GAME"
        
        :param main_app: main_app is an instance of the main application class that this method belongs to.
        It is passed as a parameter to the method so that the method can access and modify the state of the
        main application
        """
        print("Playing as CodeBreaker")

        game_config.player_is_guesser = True
        game_config.guesser_is_player = True
        game_config.guesser_is_computer = False
  
        game_config.coder_is_player = False
        game_config.coder_is_computer_local = True
        game_config.coder_is_computer_server = False

        if self.main_app.online_settings_model.online_mode:
            game_config.IP_ADDRESS = self.main_app.online_settings_model.ip_address
            game_config.PORT = self.main_app.online_settings_model.port
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = True


        self.main_app.start_new_game()
        # main_app._player_guesser_state = False

    def __str__(self):
        return "CodeBreaker Spielen"
    