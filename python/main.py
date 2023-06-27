import time

import numpy as np
import pygame
from config import config
from config import game_config
from constants import MENU, GAME, ONLINE_SETTINGS
from gui.board_view import BoardView
from gui.menu_controller import MenuController
from gui.menu_view import MenuView
from gui.menu_model import MenuModel
from gui.mvc_online_settings.view import View as OnlineSettingsView
from gui.mvc_online_settings.controller import Controller as OnlineSettingsController
from logic.color_mapping import convert_input_to_color
from logic.computer_guesser import ComputerGuesser
from logic.computer_local_coder import ComputerLocalCoder
from logic.computer_network_coder import ComputerNetworkCoder
from logic.general_logic import calculate_pins
from logic.player_coder import PlayerCoder
from logic.player_guesser import PlayerGuesser

class MainApp:
    def __init__(self):
        # Initialisierung von Pygame
        pygame.init()   # pylint: disable=E1101

        # Erstellen des Bildschirms mit den angegebenen Dimensionen
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

        # Festlegen des Fenstertitels
        pygame.display.set_caption("Mastermind")

        # Erstellen eines Clock-Objekts zur Framerate-Steuerung
        self.clock = pygame.time.Clock()

        self.time = time.time() - 1000

        # Property und Setter für den Zustand der Anwendung (Menü oder Spiel)
        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            if value in [MENU, GAME, ONLINE_SETTINGS]:
                print("setting..." + value)

                self._state = value
            else:
                raise ValueError("Invalid view state")

        self._state = MENU

        self.online_settings_view = OnlineSettingsView(self.screen)
        self.online_settings_controller = OnlineSettingsController(
            self.screen, self)

        # These lines of code are creating instances of the `MenuModel`, `MenuView`, and `MenuController`
        # classes, which are part of the Model-View-Controller (MVC) design pattern.
        # By creating these objects, the code is setting up the MVC architecture for the menu screen.
        self.menu_model = MenuModel(self)
        self.menu_view = MenuView(self.screen, self.menu_model)
        self.menu_controller = MenuController(self.menu_model, self.menu_view)

        # Erstellen eines BoardView-Objekts mit dem Bildschirm und der Farbzellen-Methode
        self.board_view = BoardView(
            self.screen, self.color_cell, self.handle_button_click)

        # Initialisierung der Boardansicht
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click)

        # Initialisierung von Coder und Guesser
        self.coder = None
        self.guesser = None

    def update_roles(self):
        # Aktualisierung der Rollen (Coder und Guesser) basierend auf den Spielkonfigurationen
        if game_config.player_is_guesser:
            self.coder = ComputerLocalCoder() if not game_config.computer_is_network else ComputerNetworkCoder()
            self.guesser = PlayerGuesser()
        else:
            self.coder = PlayerCoder()
            self.guesser = ComputerGuesser(code_length=config.COLUMNS)

    def handle_button_exit_click(self, board_view):
        self._state = MENU
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)
        self.menu_view.clearSetting()
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click)
        self.coder = None
        self.guesser = None

    def set_state(self, value):
        """
        This function sets the value of the "_state" attribute to the input "value".

        :param value: The value parameter is the new value that we want to set for the state attribute of an
        object. The method set_state() takes this value as an argument and assigns it to the private
        attribute _state of the object
        """
        self._state = value

    def handle_button_click(self, board_view):
        """
        Diese Methode wird aufgerufen, wenn der Button geklickt wird.
        Sie überprüft, ob alle Farben in der aktuellen Reihe ausgewählt wurden.
        Wenn ja, wird die entsprechende Aktion ausgeführt.
        """

        if not game_config.computer_is_playing:
            if not game_config.code_is_coded and not game_config.player_is_guesser:
                # Der Spieler legt den Geheimcode fest
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
                # Der Spieler macht einen Rateversuch
                row_is_correct = True
                for column in range(config.COLUMNS):
                    if game_config.board_guess[game_config.current_row][column] is None:
                        row_is_correct = False

                if row_is_correct:
                    game_config.board_final[game_config.current_row] = game_config.board_guess[game_config.current_row]
                    game_config.computer_is_playing = True

            elif not game_config.player_is_guesser:
                # Der Spieler bewertet einen Rateversuch des Computers
                print("Solution:", game_config.solution)
                print("Guess:", game_config.board_final[game_config.current_row])
                black_temp, white_temp = calculate_pins(game_config.solution, game_config.board_final[game_config.current_row])

                white_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 7)
                black_pins = np.count_nonzero(game_config.feedback_board_final[game_config.current_row - 1] == 8)

                if black_temp != black_pins or white_temp != white_pins:
                    print("Falsche Bewertung")
                    self.board_view.textfield_text = "Falsche Bewertung!"
                    return

                # Der Geheimcode wurde erraten
                if black_pins is config.COLUMNS:
                    game_config.player_won = True
                    game_config.game_is_over = True
                    return

                self.guesser.evaluate_feedback(black_pins, white_pins)
                game_config.current_row -= 1
                game_config.computer_is_playing = True

                # Es gibt keine Rateversuche mehr
                if game_config.current_row == 0:
                    game_config.game_is_over = True

    def color_cell(self, board_view, row, column, color, isLeftBoard):
        """
        Diese Methode färbt eine Zelle in Abhängigkeit von ihrer Zeilennummer ein.
        Wenn die Zeilennummer mit der aktuellen Reihe übereinstimmt und der Spieler der Rater ist,
        wird die Zelle eingefärbt und die entsprechende Farbe im Rate-Board gespeichert.
        :param board_view: Das BoardView-Objekt, auf dem die Zelle eingefärbt werden soll
        :param row: Die Zeilennummer der Zelle
        :param column: Die Spaltennummer der Zelle
        :param color: Die Farbe, mit der die Zelle eingefärbt werden soll
        """

        if color == None or game_config.game_is_over:
            return

        if not game_config.computer_is_playing:
            if not game_config.code_is_coded and not game_config.player_is_guesser and isLeftBoard and row == 0:
                # Der Spieler legt den Geheimcode fest
                game_config.board_guess[row, column] = convert_input_to_color(color)
                board_view.board[row][column] = color

            elif row == game_config.current_row and game_config.player_is_guesser and isLeftBoard:
                # Der Spieler macht einen Rateversuch
                game_config.board_guess[row, column] = convert_input_to_color(color)
                board_view.board[row][column] = color

            elif row == (game_config.current_row - 1) and not game_config.player_is_guesser and not isLeftBoard:
                # Der Spieler bewertet einen Rateversuch des Computers
                game_config.feedback_board_final[row, column] = convert_input_to_color(color, True)
                board_view.board_feedback[row + 1][column] = color

    def run(self):
        # Den Bildschirm mit einer Hintergrundfarbe füllen
        self.screen.fill((244, 244, 244))

        """
        Startet die Hauptschleife der Anwendung.
        """
        while True:
            if self._state == MENU:
                # Menüzustand
                for event in pygame.event.get():
                    self.menu_controller.handle_event(event)
                    self.menu_view.draw()

            elif self._state == ONLINE_SETTINGS:
                for event in pygame.event.get():
                    self.online_settings_controller.handle_event(event)
                    self.online_settings_view.draw()

            elif self._state == GAME:
                # Spielzustand

                while self.coder is None:
                    self.update_roles()

                if not game_config.code_is_coded:
                    # Der Geheimcode wurde noch nicht festgelegt
                    self.board_view.textfield_text = "Lege den Code fest in \nder ersten Reihe."

                    if game_config.player_is_guesser:
                        # Der Computer muss den Geheimcode festlegen
                        if not game_config.computer_is_network:
                            self.coder.generate_code()

                else:
                    # Der Geheimcode wurde festgelegt
                    for index, color in enumerate(game_config.solution):
                        self.board_view.board[0][index] = convert_input_to_color(color)

                    if game_config.player_is_guesser:
                        # Der Spieler macht einen Rateversuch
                        self.board_view.textfield_text = "Mach einen Rateversuch."

                        if game_config.computer_is_playing:
                            white_pins, red_pins = self.coder.rate_moe()

                            if game_config.computer_is_network and game_config.game_is_over:
                                # Das Spiel ist vorbei und der Computer hat gewonnen
                                self.board_view.textfield_text = "Spiel ist vorbei."
                                for i in range(config.COLUMNS):
                                    self.board_view.board[0][i] = convert_input_to_color(game_config.board_final[game_config.current_row][i])

                            # Färbe die Pins entsprechend der Bewertung ein
                            for column in range(red_pins):
                                self.board_view.board_feedback[game_config.current_row][column] = config.FEEDBACK_COLORS[1]

                            for column in range(white_pins):
                                self.board_view.board_feedback[game_config.current_row][red_pins + column] = config.FEEDBACK_COLORS[0]

                            game_config.current_row -= 1

                            if game_config.current_row == 0:
                                game_config.game_is_over = True

                            game_config.computer_is_playing = False


                    else:
                        # Der Computer macht einen Rateversuch
                        if game_config.computer_is_playing and not game_config.game_is_over:
                            self.board_view.textfield_text = "Bitte bewerte den Rateversuch."
                            guess = self.guesser.guess_code()

                            for index, item in enumerate(guess):
                                self.board_view.board[game_config.current_row][index] = convert_input_to_color(item)
                                game_config.board_guess[game_config.current_row][index] = item
                                game_config.board_final[game_config.current_row][index] = item
                                game_config.computer_is_playing = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:# pylint: disable=E1101
                        pygame.quit()# pylint: disable=E1101
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        # Linksklick
                        if event.button == 1:
                            # Wenn eine Maustaste gedrückt wird, starte das Drag-Event mit der aktuellen Mausposition
                            self.board_view.start_drag(mouse_pos)
                        elif event.button == 3:
                            # Wenn der Spieler bewertet, kann er Eingaben durch Rechtsklick wieder entfernen
                            if not game_config.player_is_guesser and not game_config.game_is_over and not game_config.computer_is_playing:
                                row, column, is_left = self.board_view.get_clicked_cell(mouse_pos)
                                if not is_left:
                                    game_config.feedback_board_final[row][column] = None
                                    self.board_view.board_feedback[row + 1] = game_config.feedback_board_final[row]
                            # elif game_config.player_is_guesser and not game_config.game_is_over and not game_config.computer_is_playing:
                            #     row, column, is_left = self.board_view.get_clicked_cell(mouse_pos)
                            #     if is_left:
                            #         game_config.board_guess[row][column] = None
                            #         self.board_view.board[row] = game_config.board_guess[row]

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
