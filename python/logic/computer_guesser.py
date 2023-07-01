import random

from matplotlib import pyplot as plt

from config import config
from config import game_config
from logic.color_mapping import convert_input_to_color
from logic.general_logic import calculate_pins


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
        code_copy = list(code)
        guess_copy = list(self.last_guess)

        black_pins, white_pins = calculate_pins(code_copy, guess_copy)

        return black_pins, white_pins

    def guess(self, board_view):
        """
        Rät einen zufälligen Code aus der Liste der möglichen Codes und speichert ihn als letzten geratenen Code
        """
        print("Anzahl der verbelibenden Möglichkeiten:", len(self.possibilities))
        guess = random.choice(self.possibilities)
        self.solutions.append(guess)
        self.last_guess = guess

        if board_view != None:
            for index, color in enumerate(guess):
                # Board View hinzufügen
                board_view.board[game_config.current_row][index] = convert_input_to_color(color)
                game_config.board_guess[game_config.current_row][index] = color
                game_config.board_final[game_config.current_row][index] = color

        return True

    def evaluate_feedback(self, black_pins, white_pins):
        """
        Aktualisiert die Liste der möglichen Codes basierend auf dem erhaltenen Feedback
        """
        self.possibilities = [code for code in self.possibilities if
                              self.evaluate_guess(code) == (black_pins, white_pins)]

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

# import matplotlib.pyplot as plt
# import random
#
# game = ComputerGuesser(code_length=config.COLUMNS)
# attempts_list = []
#
# for i in range(10000):
#     if i % 1000 == 0:
#         print(i)
#     guess = None
#     attempts = 0
#
#     solution = game.generate_code()
#     game.possibilities = game.get_all_possible_codes()
#
#     while guess != solution:
#         attempts += 1
#         guess = random.choice(game.possibilities)
#         game.last_guess = guess
#         black_pins, white_pins = game.evaluate_guess(solution)
#         game.evaluate_feedback(black_pins, white_pins)
#
#     attempts_list.append(attempts)
#
# # Berechnung der schnellsten, langsamsten und durchschnittlichen Anzahl der Versuche
# fastest_attempt = min(attempts_list)
# slowest_attempt = max(attempts_list)
# average_attempt = sum(attempts_list) / len(attempts_list)
#
# # Erstellung des Subplots
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))
#
# # Plotten des Barplots
# unique_values = list(set(attempts_list))
# unique_values.sort()
# frequency = [attempts_list.count(value) for value in unique_values]
# ax1.bar(unique_values, frequency, edgecolor='black', color='lightblue')
# ax1.set_xlabel('Anzahl der Versuche')
# ax1.set_ylabel('Häufigkeit')
# ax1.set_title('Verteilung der Versuche')
# ax1.grid(True)
#
# # Markierung des Mittelwerts
# mean_value = average_attempt
# ax1.axvline(mean_value, color='red', linestyle='dashed', linewidth=2)
# ax1.text(mean_value + 0.1, ax1.get_ylim()[1] * 0.97, f'Mittelwert: {mean_value:.2f}', color='black', font={'size': 12})
#
# # Plotten des Boxplots
# boxprops = dict(linewidth=2, edgecolor='blue', facecolor='lightblue')
# medianprops = dict(linewidth=2, color='red')
# bp = ax2.boxplot(attempts_list, vert=False, patch_artist=True)
# for box in bp['boxes']:
#     box.set(facecolor='lightblue')
#     box.set(**boxprops)
# for median in bp['medians']:
#     median.set(**medianprops)
# ax2.set_xlabel('Versuche')
# ax2.set_title('Verteilung der Versuche')
# ax2.grid(True)
#
# plt.tight_layout()
# plt.show()
#
# print("Schnellster Versuch:", fastest_attempt, "Versuche")
# print("Langsamster Versuch:", slowest_attempt, "Versuche")
# print("Durchschnittliche Anzahl der Versuche:", average_attempt, "Versuche")
