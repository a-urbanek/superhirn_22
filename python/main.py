import pygame

from config import config
from config import game_config
from constants import MENU, GAME
from gui.board_view import BoardView
from gui.menu_controller import MenuController
from gui.menu_view import MenuView
from logic.computer_guesser import ComputerGuesser
from logic.computer_local_coder import ComputerLocalCoder
from logic.player_guesser import PlayerGuesser
from logic.player_coder import PlayerCoder
from logic.color_mapping import convert_input_to_color

import numpy as np


class MainApp:
    def __init__(self):
        # Initialisierung von Pygame
        pygame.init()

        # Erstellen des Bildschirms mit den angegebenen Dimensionen
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

        # Festlegen des Fenstertitels
        pygame.display.set_caption("Mastermind")

        # Erstellen eines Clock-Objekts zur Framerate-Steuerung
        self.clock = pygame.time.Clock()

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            print(value)
            if value in [MENU, GAME]:
                print("setting..." + value)
                self._state = value
            else:
                raise ValueError("Invalid view state")

        # @state.setter
        # def player_guesser_state(self, role):
        #     print(role)
        #     self._player_guesser_state = role
            # if value in [MENU, GAME]:
            #     print("setting..." + value)
            #     self._state = value
            # else:
            #     raise ValueError("Invalid view state")

        self._state = MENU

        # self._player_guesser_state = True

        # It creates an instance of the `MenuView` class, passing in the `screen` object as a parameter. This
        # is used to display the menu screen in the game.
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)

        # Erstellen eines BoardView-Objekts mit dem Bildschirm und der Farbzellen-Methode
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click)

        # Coder erstellen
        # self.coder = ComputerLocalCoder()
        # self.coder = PlayerCoder()

        self.coder = None
        self.guesser = None

        # print("Start")
        # if game_config.player_is_guesser:
        #     self.coder = ComputerLocalCoder()
        #     self.guesser = PlayerGuesser()
        # else:
        #     self.coder = PlayerCoder()
        #     self.guesser = ComputerGuesser(code_length=config.COLUMNS)

        # print(self.coder)
        # print(self.guesser)
        # print(game_config.player_is_guesser)

        # Guesser erstellen
        # self.guesser = PlayerGuesser()
        # self.guesser = ComputerGuesser(code_length=config.COLUMNS)
        # self.guesser = ComputerGuesser(code_length=config.COLUMNS) if not game_config.player_is_guesser else PlayerGuesser()

    def update_roles(self):
        if game_config.player_is_guesser:
            self.coder = ComputerLocalCoder()
            self.guesser = PlayerGuesser()
        else:
            self.coder = PlayerCoder()
            self.guesser = ComputerGuesser(code_length=config.COLUMNS)

    def handle_button_click(self, board_view):
        """
        Die Methode, die aufgerufen wird, wenn der Button geklickt wird.
        Überprüft, ob alle Farben in der aktuellen Reihe ausgewählt wurden.
        Wenn ja, wird die Meldung "Row complete" ausgegeben und die aktuelle Reihe verringert.
        """

        print("computer_is_playing", game_config.computer_is_playing)
        print("code_is_coded", game_config.code_is_coded)
        print("player_is_guesser", game_config.player_is_guesser)

        if not game_config.computer_is_playing:
            if not game_config.code_is_coded and not game_config.player_is_guesser:
                row_is_correct = True
                for column in range(config.COLUMNS):
                    if game_config.board_guess[0][column] is None:
                        row_is_correct = False

                if row_is_correct:
                    game_config.board_final[0] = game_config.board_guess[0]
                    game_config.solution = game_config.board_guess[0]
                    game_config.computer_is_playing = True
                    game_config.code_is_coded = True

            elif game_config.player_is_guesser:
                row_is_correct = True
                for column in range(config.COLUMNS):
                    if game_config.board_guess[game_config.current_row][column] is None:
                        row_is_correct = False

                if row_is_correct:
                    game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
                    game_config.computer_is_playing = True

            elif not game_config.player_is_guesser:
                print(game_config.feedback_board_final[game_config.current_row - 1])
                white_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 7)
                black_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 8)
                self.guesser.evaluate_feedback(black_pins, white_pins)
                game_config.current_row -= 1
                game_config.computer_is_playing = True









        # if game_config.computer_is_playing == False:
            # self.player.make_move()

    def color_cell(self, board_view, row, column, color, isLeftBoard):
        """
        Färbt eine Zelle in Abhängigkeit von ihrer Zeilennummer ein.
        Wenn die Zeilennummer mit der aktuellen Reihe übereinstimmt und der Spieler der Rater ist,
        wird die Zelle eingefärbt und die entsprechende Farbe im Rate-Board gespeichert.
        :param board_view: Das BoardView-Objekt, auf dem die Zelle eingefärbt werden soll
        :param row: Die Zeilennummer der Zelle
        :param column: Die Spaltennummer der Zelle
        :param color: Die Farbe, mit der die Zelle eingefärbt werden soll
        """

        print(row, column, color, isLeftBoard, game_config.current_row)

        if color == None:
            return

        if not game_config.computer_is_playing:
            if not game_config.code_is_coded and not game_config.player_is_guesser and isLeftBoard:
                game_config.board_guess[row, column] = convert_input_to_color(color)
                board_view.board[row][column] = color

            elif row == game_config.current_row and game_config.player_is_guesser and isLeftBoard:
                game_config.board_guess[row, column] = convert_input_to_color(color)
                board_view.board[row][column] = color

            elif row == (game_config.current_row - 1) and not game_config.player_is_guesser and not isLeftBoard:
                game_config.feedback_board_final[row, column] = convert_input_to_color(color)
                board_view.board_feedback[row + 1][column] = color


    def run(self):
        # Bildschirm mit einer Hintergrundfarbe füllen
        self.screen.fill((244, 244, 244))

        """
        Startet die Hauptschleife der Anwendung.
        """
        while True:
            if self._state == MENU:
                for event in pygame.event.get():
                    self.menu_controller.handle_event(event)
                    self.menu_view.draw()

            elif self._state == GAME:

                while self.coder is None:
                    self.update_roles()

                if not game_config.code_is_coded:
                    # Es wurde noch kein Geheimcode festgelegt
                    if game_config.player_is_guesser:
                        # der Computer muss den Code festlegen
                        self.coder.generate_code()
                        # game_config.code_is_coded = True
                else:
                    if game_config.player_is_guesser:
                        if game_config.computer_is_playing:
                            red_pins, white_pins = self.coder.rate_moe()
                            for column in range(red_pins):
                                self.board_view.board_feedback[game_config.current_row][column] = config.FEEDBACK_COLORS[0]

                            for column in range(white_pins):
                                self.board_view.board_feedback[game_config.current_row][red_pins + column] = config.FEEDBACK_COLORS[1]

                            game_config.current_row -= 1
                            game_config.computer_is_playing = False
                            # print("Der Computer ist dran")


                    else:
                        if game_config.computer_is_playing:
                            guess = self.guesser.guess_code()

                            for index, item in enumerate(guess):
                                print(index, item)
                                self.board_view.board[game_config.current_row][index] = convert_input_to_color(item)
                                game_config.board_guess[game_config.current_row][index] = item
                                game_config.board_final[game_config.current_row][index] = item
                                game_config.computer_is_playing = False














                # Ereignisschleife zum Abfragen von Ereignissen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Wenn eine Maustaste gedrückt wird, starte das Drag-Event mit der aktuellen Mausposition
                        mouse_pos = pygame.mouse.get_pos()
                        self.board_view.start_drag(mouse_pos)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        # Wenn eine Maustaste losgelassen wird, führe das Drop-Event mit der aktuellen Mausposition aus
                        mouse_pos = pygame.mouse.get_pos()
                        self.board_view.drop(mouse_pos)

                # Bildschirm mit einer Hintergrundfarbe füllen
                self.screen.fill((80, 80, 80))

                # Aktualisieren und Zeichnen des Spielbretts
                self.board_view.update()
                self.board_view.draw()

                # Bildschirm aktualisieren
                pygame.display.flip()

                # Begrenzung der Framerate
                self.clock.tick(config.FPS)


if __name__ == '__main__':
    # Erstellen einer Instanz der MainApp-Klasse und Starten der Anwendung
    app = MainApp()
    app.run()
