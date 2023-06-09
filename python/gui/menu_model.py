from .commands.play_as_codebreaker_command import PlayAsCodeBreakerCommand
from .commands.play_as_codemaker_command import PlayAsCodeMakerCommand
from .commands.edit_online_settings_command import EditOnlineSettings
from .commands.quit_game_command import QuitGameCommand


# The MenuModel class initializes a list of menu items for the game.
class MenuModel:
    def __init__(self):
        """
        This function initializes a list of menu items for the game, including options to play as a code
        breaker or maker, edit online settings, and quit the game.
        """
        self.menu_items = [
            PlayAsCodeBreakerCommand(),
            PlayAsCodeMakerCommand(),
            EditOnlineSettings(),
            QuitGameCommand()
        ]