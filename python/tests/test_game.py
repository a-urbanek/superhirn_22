import unittest
from ..logic.game import Game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        """
        Wird vor jedem einzelnen Testfall aufgerufen.
        """

    def test_generate_code(self):
        """
        Testet die Generierung eines Farbcodes im Spiel.
        """

    def test_check_guess(self):
        """
        Testet die Überprüfung des geratenen Farbcodes.
        """

if __name__ == '__main__':
    unittest.main()
