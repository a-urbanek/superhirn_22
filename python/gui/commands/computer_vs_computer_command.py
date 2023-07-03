# The `ComputerVsComputer` command sets up the game configuration for a computer vs computer mode and
# starts a new game.
from constants import GAME
from .command import Command
from config import game_config

import sys
sys.path.insert(0, '..')


"""
The `ComputerVsComputer` command sets up the game configuration for a computer vs computer mode and
starts a new game.
"""
class ComputerVsComputer(Command):
    def execute(self):
        """
        The method sets up the game configuration for a computer vs computer mode and starts a new game.
        """
        print("Executing the Computer vs Computer command...")
        
        game_config.player_is_guesser = False
        game_config.guesser_is_computer = True
        game_config.guesser_is_player = False
        game_config.coder_is_player = False

        if self.main_app.online_settings_model.online_mode:
            
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = True

            game_config.IP_ADDRESS = self.main_app.online_settings_model.ip_address
            game_config.PORT = self.main_app.online_settings_model.port

        else:        
            game_config.coder_is_computer_local = True
            game_config.coder_is_computer_server = False
        
        self.main_app.start_new_game()

    def __str__(self):
        """
        The method returns a string that says "Computer vs Computer".
        :return: The string "Computer vs Computer" is being returned.
        """
        return "Computer vs Computer"
