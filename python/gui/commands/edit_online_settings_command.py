# The EditOnlineSettings class is a subclass of the Command class that sets the main app state to
# ONLINE_SETTINGS

import sys
from .command import Command
sys.path.insert(0, '..')
from constants import ONLINE_SETTINGS


class EditOnlineSettings(Command):
    
    def execute(self):
        print("Settings")
        self.main_app.set_state(ONLINE_SETTINGS)

    def __str__(self):
        return "Settings"