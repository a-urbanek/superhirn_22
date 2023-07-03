import unittest

from config import config
from logic.color_mapping import convert_input_to_color


class TestLogic(unittest.TestCase):


    def test_convert_white_color_to_number(self):
        assert convert_input_to_color((255, 0, 0)) == 1
        assert convert_input_to_color((0, 255, 0)) == 2
        assert convert_input_to_color((255, 255, 0)) == 3
        assert convert_input_to_color((0, 0, 255)) == 4
        assert convert_input_to_color((255, 128, 0)) == 5
        assert convert_input_to_color((153, 76, 0)) == 6

    def test_convert_feedback_colors(self):
        assert convert_input_to_color(7, True) == config.FEEDBACK_COLORS[0]
        assert convert_input_to_color(8, True) == config.FEEDBACK_COLORS[1]

    def test_convert_normal_colors(self):
        assert convert_input_to_color(1) == config.COLORS[0]
        assert convert_input_to_color(2) == config.COLORS[1]
        assert convert_input_to_color(3) == config.COLORS[2]
        assert convert_input_to_color(4) == config.COLORS[3]
        assert convert_input_to_color(5) == config.COLORS[4]
        assert convert_input_to_color(6) == config.COLORS[5]

    def test_convert_feedback_colors_false(self):
        # Testet, ob zahlen 7 und 8 auf im normalen Superhirn converten
        self.assertEqual(convert_input_to_color(7, False), None)
        self.assertEqual(convert_input_to_color(8, False), None)

    def test_convert_normal_colors_true(self):
        self.assertEqual(convert_input_to_color(1, True), None)
        self.assertEqual(convert_input_to_color(2, True), None)
        self.assertEqual(convert_input_to_color(3, True), None)
        self.assertEqual(convert_input_to_color(4, True), None)
        self.assertEqual(convert_input_to_color(5, True), None)
        self.assertEqual(convert_input_to_color(6, True), None)

    def test_convert_invalid_string_to_number(self):
        self.assertIsNone(convert_input_to_color("invalid input"))

    def test_convert_large_number_to_number(self):
        self.assertIsNone(convert_input_to_color(999999))


if __name__ == "__main__":
    unittest.main()
