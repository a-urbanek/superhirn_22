import time

import numpy as np
import pygame
from config import config
from config import game_config
from constants import MENU, GAME
from gui.board_view import BoardView
from gui.menu_controller import MenuController
from gui.menu_view import MenuView
from logic.color_mapping import convert_input_to_color
from logic.computer_guesser import ComputerGuesser
from logic.computer_local_coder import ComputerLocalCoder
from logic.computer_network_coder import ComputerNetworkCoder
from logic.player_coder import PlayerCoder
from logic.player_guesser import PlayerGuesser

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

        self.time = time.time() - 1000

        # Property und Setter für den Zustand der Anwendung (Menü oder Spiel)
        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            if value in [MENU, GAME]:
                self._state = value
            else:
                raise ValueError("Invalid view state")

        self._state = MENU

        # Initialisierung der Menüansicht und des Menücontrollers
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)

        # Initialisierung der Boardansicht
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click)

        # Initialisierung von Coder und Guesser
        self.coder = None
        self.guesser = None

    def update_roles(self):

        if game_config.coder_is_computer_local: self.coder = ComputerLocalCoder()
        elif game_config.coder_is_computer_server: self.coder = ComputerNetworkCoder()
        else: self.coder = PlayerCoder()

        if game_config.guesser_is_computer: self.guesser = ComputerGuesser(code_length=config.COLUMNS)
        else: self.guesser = PlayerGuesser()

        print("update_roles", self.coder, self.guesser)



        # Aktualisierung der Rollen (Coder und Guesser) basierend auf den Spielkonfigurationen
        # if game_config.player_is_guesser:
        #     self.coder = ComputerLocalCoder() if not game_config.computer_is_network else ComputerNetworkCoder()
        #     self.guesser = PlayerGuesser()
        # else:
        #     self.coder = PlayerCoder()
        #     self.guesser = ComputerGuesser(code_length=config.COLUMNS)

    def handle_button_exit_click(self, board_view):
        print("handle_button_exit_click")
        self._state = MENU
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)
        self.menu_view.clearSetting()
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click)
        self.coder = None
        self.guesser = None

    def handle_button_click(self, board_view):
        """
        Diese Methode wird aufgerufen, wenn der Button geklickt wird.
        Sie überprüft, ob alle Farben in der aktuellen Reihe ausgewählt wurden.
        Wenn ja, wird die entsprechende Aktion ausgeführt.
        """
        if game_config.guesser_is_player or game_config.coder_is_player:
            if game_config.coder_is_playing:
                if not game_config.code_is_coded:
                    if self.coder.generate_code(self.board_view):
                        game_config.coder_is_playing = False
                else:
                    black_pins, white_pins, rate_was_correct = self.coder.rate_move(self.board_view, self.guesser)
                    if rate_was_correct:
                        game_config.coder_is_playing = False
            else:
                if self.guesser.guess(self.board_view):
                    game_config.coder_is_playing = True

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

        print("color_cell", row, column, color, isLeftBoard)

        if game_config.coder_is_player or game_config.guesser_is_player:
            # print(game_config.coder_is_player or game_config.guesser_is_player)

            if game_config.coder_is_playing:

                if not game_config.code_is_coded and isLeftBoard and row == 0:
                    game_config.board_guess[row, column] = convert_input_to_color(color)
                    board_view.board[row][column] = color
                elif not isLeftBoard and row == (game_config.current_row - 1):
                    game_config.feedback_board_final[row, column] = convert_input_to_color(color, True)
                    board_view.board_feedback[row + 1][column] = color

            else:
                print(game_config.current_row, row, isLeftBoard)
                if row == game_config.current_row and isLeftBoard:
                    game_config.board_guess[row, column] = convert_input_to_color(color)
                    board_view.board[row][column] = color

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

            elif self._state == GAME:
                # Spielzustand

                while self.coder is None:
                    self.update_roles()

                if game_config.coder_is_playing: print("Coder ist dran")
                else: print("Guesser ist dran")

                if game_config.current_row == 0 or game_config.game_is_over:
                    # print(game_config.current_row, game_config.game_is_over)
                    # print("Vorbei...")
                    pass
                else:
                    if not game_config.code_is_coded:
                        print(1)
                        # falls der code vom spieler generiert wird, wird self.coder.generate_code in handle_button_click aufgerufen
                        if not game_config.coder_is_player:
                            print(2)
                            self.coder.generate_code(self.board_view)

                            if game_config.coder_is_computer_local:
                                for index, color in range(game_config.solution):
                                    game_config.board_final[0][index] = convert_input_to_color(color)
                                    game_config.board_guess[0][index] = convert_input_to_color(color)

                            game_config.coder_is_playing = False

                    # Jetzt muss geraten werden
                    elif not game_config.coder_is_playing:
                        print(3)
                        if not game_config.guesser_is_player:
                            print(4)
                            self.guesser.guess(self.board_view)
                            print(game_config.board_final)
                            game_config.coder_is_playing = True
                    else:
                        # Coder ist dran. muss also den Zug bewerten
                        print(5)
                        if not game_config.coder_is_player:
                            print(6)
                            black_pins, white_pins = self.coder.rate_move(self.board_view, self.guesser)
                            print(7)
                            self.guesser.evaluate_feedback(black_pins, white_pins)
                            print(8)

                            if black_pins == 5:
                                game_config.game_is_over = True

                            game_config.coder_is_playing = False
                            game_config.current_row -= 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
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
