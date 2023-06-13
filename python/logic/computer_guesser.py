import random
import matplotlib.pyplot as plt

class ComputerGuesser:
    COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    # COLORS = ['a', 'b', 'c', 'd', 'e', 'f']

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
        code = random.choices(self.COLORS, k=self.code_length)
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

        generate_codes(self.COLORS, self.code_length, [])

        return possibilities

game = ComputerGuesser(code_length=6)
attempts_list = []

for i in range(100):
    if i % 10 == 0:
        print(i)
    guess = None
    attempts = 0

    solution = game.generate_code()
    game.possibilities = game.get_all_possible_codes()

    while guess != solution:
        attempts += 1
        guess = game.guess_code()
        black_pins, white_pins = game.evaluate_guess(solution)
        game.evaluate_feedback(black_pins, white_pins)

    attempts_list.append(attempts)

# Berechnung der schnellsten, langsamsten und durchschnittlichen Anzahl der Versuche
fastest_attempt = min(attempts_list)
slowest_attempt = max(attempts_list)
average_attempt = sum(attempts_list) / len(attempts_list)

# Plotten des Versuchsverlaufs
plt.figure(figsize=(8, 6))
plt.hist(attempts_list, bins=range(min(attempts_list), max(attempts_list) + 2), edgecolor='black')
plt.xlabel('Anzahl der Versuche')
plt.ylabel('Häufigkeit')
plt.title('Verteilung der Versuche')
plt.grid(True)
plt.show()

print("Schnellster Versuch:", fastest_attempt, "Versuche")
print("Langsamster Versuch:", slowest_attempt, "Versuche")
print("Durchschnittliche Anzahl der Versuche:", average_attempt, "Versuche")

'''
Länge = 4
Versuche = 10000

Schnellster Versuch: 1 Versuche
Langsamster Versuch: 8 Versuche
Durchschnittliche Anzahl der Versuche: 4.6445 Versuche

Länge = 5
Versuche = 10000

Schnellster Versuch: 1 Versuche
Langsamster Versuch: 8 Versuche
Durchschnittliche Anzahl der Versuche: 5.069 Versuche

Länge = 6
Versuche = 1000

Schnellster Versuch: 2 Versuche
Langsamster Versuch: 8 Versuche
Durchschnittliche Anzahl der Versuche: 5.519 Versuche
'''
