import random
from config import config

class ComputerGuesser:
    def __init__(self, code_length):
        self.code_length = code_length
        self.code = self.generate_code()  # Generiere den zu erratenden Code
        self.solutions = []  # Liste der geratenen Lösungen
        self.possibilities = self.get_all_possible_codes()  # Liste aller möglichen Codes
        self.last_guess = None  # Der zuletzt geratene Code

    def generate_code(self):
        """
        Generiert einen zufälligen Code mit der angegebenen Länge
        """
        code = random.choices(config.COLORS_NUMBERS, k=self.code_length)
        return code

    def evaluate_guess(self, code):
        """
        Bewertet den geratenen Code und gibt die Anzahl der schwarzen und weißen Pins zurück
        """
        black_pins = 0
        white_pins = 0
        code_copy = list(code)
        guess_copy = list(self.last_guess)

        # Überprüfe auf schwarze Pins (richtige Farbe an richtiger Position)
        for i in range(len(guess_copy)):
            if guess_copy[i] == code_copy[i]:
                black_pins += 1
                code_copy[i] = None
                guess_copy[i] = None

        # Überprüfe auf weiße Pins (richtige Farbe an falscher Position)
        for i in range(len(guess_copy)):
            if guess_copy[i] is not None and guess_copy[i] in code_copy:
                white_pins += 1
                index = code_copy.index(guess_copy[i])
                code_copy[index] = None
                guess_copy[i] = None

        return black_pins, white_pins

    def guess_code(self):
        """
        Rät einen zufälligen Code aus der Liste der möglichen Codes und speichert ihn als letzten geratenen Code
        """
        guess = random.choice(self.possibilities)
        self.solutions.append(guess)
        self.last_guess = guess
        return guess

    def evaluate_feedback(self, black_pins, white_pins):
        """
        Aktualisiert die Liste der möglichen Codes basierend auf dem erhaltenen Feedback
        """
        self.possibilities = [code for code in self.possibilities if self.evaluate_guess(code) == (black_pins, white_pins)]

    def get_all_possible_codes(self):
        """
        Generiert alle möglichen Codes mit der angegebenen Länge
        """
        possibilities = []

        def generate_codes(colors, code_length, current_code):
            if len(current_code) == code_length:
                possibilities.append(current_code)
            else:
                for color in colors:
                    generate_codes(colors, code_length, current_code + [color])

        generate_codes(config.COLORS_NUMBERS, self.code_length, [])

        return possibilities
