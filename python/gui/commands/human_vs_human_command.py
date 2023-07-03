
from constants import GAME
from .command import Command
from config import game_config

import sys
sys.path.insert(0, '..')


class HumanVsHuman(Command):
    def execute(self):

        print("Executing the Human vs Human command...")


        if self.main_app.online_settings_model.online_mode:
            
           return print("Gamemode does not exist")

        game_config.player_is_guesser = True
        game_config.guesser_is_computer = False
        game_config.guesser_is_player = True
        game_config.coder_is_player = True
        game_config.coder_is_computer_local = False
        game_config.coder_is_computer_server = False
        
        self.main_app.start_new_game()

    def __str__(self):
        return "Human vs Human"
