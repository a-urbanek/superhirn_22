import unittest

from logic.general_logic import calculate_pins


class TestLogic(unittest.TestCase):
    def test_calculate_pins(self):
        # Test 1: Prüfen, ob die Funktion korrekt auf eine vollständige Übereinstimmung reagiert
        assert calculate_pins([1, 2, 3, 4], [1, 2, 3, 4]) == (4, 0)

        # Test 2: Prüfen, ob die Funktion korrekt auf eine teilweise Übereinstimmung reagiert, wobei einige Farben richtig, aber an der falschen Position sind
        assert calculate_pins([1, 2, 3, 4], [4, 3, 2, 1]) == (0, 4)

        # Test 3: Prüfen, ob die Funktion korrekt auf einen Fall reagiert, bei dem keine Farben übereinstimmen
        assert calculate_pins([1, 2, 3, 4], [5, 6, 7, 8]) == (0, 0)

        # Test 4: Prüfen, ob die Funktion korrekt auf einen Fall reagiert, bei dem einige Farben richtig sind und einige Farben an der falschen Position stehen
        assert calculate_pins([1, 2, 3, 4], [1, 3, 2, 4]) == (2, 2)

        # Test 5: Prüfen, ob die Funktion korrekt auf einen Fall reagiert, bei dem einige Farben richtig sind und einige Farben fehlen
        assert calculate_pins([1, 2, 3, 4], [1, 3, 5, 6]) == (1, 1)

    # Die gleichen Tests für SupersuperHirn
    def test_calculate_pins_supersuperhirn(self):
        # Test 6:
        assert calculate_pins([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (5, 0)

        # Test 7:
        assert calculate_pins([1, 3, 2, 5, 4], [5, 4, 3, 2, 1]) == (0, 5)

        # Test 8:
        assert calculate_pins([1, 2, 3, 4, 5], [6, 6, 8, 7, 8]) == (0, 0)

        # Test 9:
        assert calculate_pins([1, 6, 7, 4, 2], [1, 4, 7, 2, 6]) == (2, 3)

        # Test 10:
        assert calculate_pins([1, 6, 7, 4, 2], [2, 6, 7, 5, 2]) == (3, 0)


if __name__ == "__main__":
    unittest.main()
