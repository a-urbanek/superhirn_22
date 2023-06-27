from .command import Command
import sys


# The QuitGameCommand class defines a command to quit the game and exit the program.
class QuitGameCommand(Command):
    def execute(self):
        """
        The function terminates the program.
        """
        sys.exit()
    
    def __str__(self):
        return "Beenden"