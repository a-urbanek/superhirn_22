# The PlayAsCodeBreakerCommand class defines a command to set the state of the main app to "GAME" when
# playing as a code breaker.

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
        self.main_app.set_state(GAME)

    def __str__(self):
        return "Play as CodeBreaker"
    