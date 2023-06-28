from config import game_config
from constants import ONLINE
from .command import Command


# The EditOnlineSettings class 
class EditOnlineSettings(Command):
    def execute(self, main_app):
        print("Online Settings")
        main_app._state = ONLINE

    def __str__(self):
        return "Online Settings"