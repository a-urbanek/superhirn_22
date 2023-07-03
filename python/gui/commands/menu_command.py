import sys
from .command import Command
sys.path.insert(0, '..')
from constants import MENU


class MenuCommand(Command):
    
    def execute(self):
        self.main_app.set_state(MENU)

    def __str__(self):
        return "Open Menu"