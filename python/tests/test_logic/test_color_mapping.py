import unittest
from logic.color_mapping import convert_input_to_color


class TestLogic(unittest.TestCase):
    def test_convert_input_to_color(self):
        # Testen Sie die Konvertierung von Integer-Eingaben in Farben
        self.assertEqual(convert_input_to_color(1), (255, 0, 0))  # Ändern Sie die Farbe entsprechend Ihrer config-Datei
        self.assertEqual(convert_input_to_color(2), (0, 255, 0))  # Ändern Sie die Farbe entsprechend Ihrer config-Datei
        self.assertEqual(convert_input_to_color(0), None)  # Es gibt keine Farbe, die der Nummer 0 zugeordnet ist

        # Testen Sie die Konvertierung von Tuple-Eingaben in Farbennummern
        self.assertEqual(convert_input_to_color((255, 0, 0)), 1)  # Ändern Sie die Farbe entsprechend Ihrer config-Datei
        self.assertEqual(convert_input_to_color((0, 255, 0)), 2)  # Ändern Sie die Farbe entsprechend Ihrer config-Datei
        self.assertEqual(convert_input_to_color((0, 0, 0)), 8)  # Ändern Sie die Farbe entsprechend Ihrer config-Datei

        # Testen Sie ungültige Eingaben
        self.assertEqual(convert_input_to_color("invalid_input"), None)
        self.assertEqual(convert_input_to_color(9), None)  # Es gibt keine Farbe, die der Nummer 9 zugeordnet ist
        self.assertEqual(convert_input_to_color((128, 128, 128)), None)  # Es gibt keine Farbennummer, die dieser Farbe zugeordnet ist

if __name__ == "__main__":
    unittest.main()
