import time

import numpy as np
import pygame
from config import config
from config import game_config
from constants import MENU, GAME, MENU_NEW
from gui.board_view import BoardView
from gui.menu_controller import MenuController
from gui.menu_view import MenuView
from gui.menu_view_update import MenuViewUpdate
from logic.color_mapping import convert_input_to_color
from logic.computer_guesser import ComputerGuesser
from logic.computer_local_coder import ComputerLocalCoder
from logic.computer_network_coder import ComputerNetworkCoder
from logic.player_coder import PlayerCoder
from logic.player_guesser import PlayerGuesser

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Fenstergröße
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# Button-Größe
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

# Texteingabe-Größe
TEXT_INPUT_WIDTH = 200
TEXT_INPUT_HEIGHT = 60

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

        self.last_player_is_coder = game_config.coder_is_playing

        # Property und Setter für den Zustand der Anwendung (Menü oder Spiel)
        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            if value in [MENU, GAME, MENU_NEW]:
                self._state = value
            else:
                raise ValueError("Invalid view state")

        self._state = MENU_NEW

        # Initialisierung der Menüansicht und des Menücontrollers
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)

        self.menu_view_new = MenuViewUpdate(self.screen, self.handle_button_start_game_click)

        # Initialisierung der Boardansicht
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click, self.handle_button_restart_click)

        # Initialisierung von Coder und Guesser
        self.coder = None
        self.guesser = None

    def update_roles(self):
        """
        Aktualisiert die Rollen des Coder und Guesser basierend auf den Spielkonfigurationen.
        """
        if game_config.coder_is_computer_local:
            self.coder = ComputerLocalCoder()
        elif game_config.coder_is_computer_server:
            self.coder = ComputerNetworkCoder(self)
        else:
            self.coder = PlayerCoder()

        if game_config.guesser_is_computer:
            self.guesser = ComputerGuesser(code_length=config.COLUMNS)
        else:
            self.guesser = PlayerGuesser()

        print("Die Spieler wurden initialisiert.")

    def handle_button_start_game_click(self):
        """
        Diese Methode wird aufgerufen, wenn der "Start Game" Button im Menü geklickt wird.
        Sie überprüft die ausgewählten Optionen und startet das Spiel mit den entsprechenden Konfigurationen.
        """
        selected_buttons = []
        if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Superhirn")
        if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Supersuperhirn")

        if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Spieler Rater")
        if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Computer Rater")

        if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Spieler Kodierer")
        if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Computer Kodierer")
        if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
            selected_buttons.append("Server")

        if len(selected_buttons) != 3:
            return
        elif 'Server' in selected_buttons and (len(self.menu_view_new.text_input1) < 1 or len(self.menu_view_new.text_input2) < 1):
            return

        if "Superhirn" in selected_buttons:
            config.IS_SUPERSUPERHIRN = False
        else:
            config.IS_SUPERSUPERHIRN = True

        if "Spieler Rater" in selected_buttons:
            game_config.guesser_is_player = True
            game_config.guesser_is_computer = False
        else:
            game_config.guesser_is_computer = True
            game_config.guesser_is_player = False

        if "Spieler Kodierer" in selected_buttons:
            game_config.coder_is_player = True
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = False
        elif "Computer Kodierer" in selected_buttons:
            game_config.coder_is_player = False
            game_config.coder_is_computer_local = True
            game_config.coder_is_computer_server = False
        else:
            game_config.IP_ADDRESS = self.menu_view_new.text_input1
            game_config.PORT = self.menu_view_new.text_input2
            game_config.coder_is_player = False
            game_config.coder_is_computer_local = False
            game_config.coder_is_computer_server = True

        game_config.game_is_over = False
        game_config.board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)
        game_config.solution = np.empty(config.COLUMNS, dtype=object)
        game_config.code_is_coded = False
        game_config.current_row = config.ROWS - 1
        game_config.error_message = ""
        game_config.no_network_connection = False

        # Farben für die Zellen im Spielbrett
        config.COLORS = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 128, 0), (153, 76, 0), (255, 255, 255),
                  (0, 0, 0)] if config.IS_SUPERSUPERHIRN else [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255),
                                                        (255, 128, 0), (153, 76, 0)]

        # Farbennummern für die Zellen im Spielbrett
        config.COLORS_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8] if config.IS_SUPERSUPERHIRN else [1, 2, 3, 4, 5, 6]

        config.FEEDBACK_COLUMNS = 5 if config.IS_SUPERSUPERHIRN else 4
        config.COLUMNS = 5 if config.IS_SUPERSUPERHIRN else 4

        # Erstellen des Rate-Boards, auf dem der Spieler seinen Rateversuch macht
        game_config.board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)

        # Erstellen des Boards, das alle logisch sinnvollen Eingaben enthält
        game_config.board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)

        # Erstellen des Boards, das die Bewertungen des Raters enthält
        game_config.feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)

        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click, self.handle_button_restart_click)
        self.update_roles()

        self._state = GAME

        print()
        print("############################################")
        print("#                                          #")
        print("#    Es wurde ein neues Spiel gestartet.   #")
        print("#                                          #")
        print("############################################")
        print()

    def handle_button_exit_click(self, board_view):
        """
        Diese Methode wird aufgerufen, wenn der "Exit" Button im Spiel geklickt wird.
        Sie setzt den Zustand der Anwendung auf das Menü zurück.
        """
        self._state = MENU_NEW
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)
        self.menu_view.clearSetting()
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click, self.handle_button_exit_click)
        self.coder = None
        self.guesser = None

    def handle_button_restart_click(self, board_view):  
        #Wie muss ich die Config Einstellungen bearbeiten damit es wieder zurückgesetzt ist
        pass

    def handle_button_click(self, board_view):
        """
        Diese Methode wird aufgerufen, wenn der Button im Spiel geklickt wird.
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
                    game_config.rate_was_correct = rate_was_correct
                    if game_config.rate_was_correct:
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
        if game_config.coder_is_player or game_config.guesser_is_player:
            if game_config.coder_is_playing:

                if not game_config.code_is_coded and isLeftBoard and row == 0:
                    game_config.board_guess[row, column] = convert_input_to_color(color)
                    board_view.board[row][column] = color
                elif not isLeftBoard and row == (game_config.current_row - 1):
                    game_config.feedback_board_final[row, column] = convert_input_to_color(color, True)
                    board_view.board_feedback[row + 1][column] = color

            else:
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

            elif self._state == MENU_NEW:

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()

                        if self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                self.menu_view_new.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            else:
                                self.menu_view_new.marked_buttons.append(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                                if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.menu_view_new.marked_buttons:
                                    self.menu_view_new.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                        elif self.menu_view_new.check_button_collision(mouse_pos, pygame.Rect(config.MARGIN, 450, BUTTON_WIDTH, BUTTON_HEIGHT)):
                            self.handle_button_start_game_click()

                    elif event.type == pygame.KEYDOWN:
                        if self.menu_view_new.server_button_selected:
                            if pygame.Rect(config.MARGIN, 350, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT).collidepoint(
                                    pygame.mouse.get_pos()):
                                if event.key == pygame.K_BACKSPACE:
                                    if len(self.menu_view_new.text_input1) > 0:
                                        self.menu_view_new.text_input1 = self.menu_view_new.text_input1[:-1]
                                elif event.key == pygame.K_RETURN:
                                    pass
                                else:
                                    self.menu_view_new.text_input1 += event.unicode
                            elif pygame.Rect(2 * config.MARGIN + TEXT_INPUT_WIDTH, 350, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT).collidepoint(
                                    pygame.mouse.get_pos()):
                                if event.key == pygame.K_BACKSPACE:
                                    if len(self.menu_view_new.text_input2) > 0:
                                        self.menu_view_new.text_input2 = self.menu_view_new.text_input2[:-1]
                                elif event.key == pygame.K_RETURN:
                                    pass
                                else:
                                    self.menu_view_new.text_input2 += event.unicode

                self.menu_view_new.draw()

            elif self._state == GAME:
                # Spielzustand
                # print( game_config.coder_is_playing, self.last_player_is_coder)

                # print(config.IS_SUPERSUPERHIRN)
                # if game_config.coder_is_playing != self.last_player_is_coder:
                #     if game_config.coder_is_playing: print("Der Kodierer ist an der Reihe.")
                #     else: print("Der Rater ist an der Reihe.")
                #     self.last_player_is_coder = game_config.coder_is_player

                while self.coder is None:
                    self.update_roles()

                if game_config.no_network_connection:
                    self.board_view.textfield_text = game_config.error_message

                elif game_config.current_row == 0 or game_config.game_is_over:
                    game_config.coder_is_playing = True
                    if game_config.guesser_won: self.board_view.textfield_text = "Der Rater hat in " + str(config.ROWS - game_config.current_row) + " Spielzügengewonnen!"
                    else: self.board_view.textfield_text = "Der Kodierer hat gewonnen!"

                else:
                    if not game_config.code_is_coded:
                        # falls der code vom spieler generiert wird, wird self.coder.generate_code in handle_button_click aufgerufen
                        if not game_config.coder_is_player:
                            if game_config.coder_is_computer_local: self.board_view.textfield_text = "Der Computer denkt sich einen Code aus."
                            if game_config.coder_is_computer_server: self.board_view.textfield_text = "Der Server denkt sich einen Code aus."
                            self.coder.generate_code(self.board_view)

                            if game_config.coder_is_computer_local:
                                for index in range(len(game_config.solution)):
                                    game_config.board_final[0][index] = game_config.solution[index]
                                    game_config.board_guess[0][index] = game_config.solution[index]
                                    self.board_view.board[0][index] = convert_input_to_color(game_config.solution[index])

                            game_config.coder_is_playing = False
                        else:
                            self.board_view.textfield_text = "Lege den geheimen Code in der ersten\nReihe fest."

                    # Jetzt muss geraten werden
                    elif not game_config.coder_is_playing:
                        if not game_config.guesser_is_player:
                            if game_config.coder_is_computer_local: self.board_view.textfield_text = "Der Computer versucht den Code\nzu knacken."
                            if game_config.coder_is_computer_server: self.board_view.textfield_text = "Der Server versucht den Code\nzu knacken."
                            self.guesser.guess(self.board_view)
                            game_config.coder_is_playing = True
                        else:
                            self.board_view.textfield_text = "Versuche den Code zu knacken!"

                    else:
                        # Coder ist dran. muss also den Zug bewerten
                        if not game_config.coder_is_player:
                            if game_config.coder_is_computer_local: self.board_view.textfield_text = "Der Computer bewerten deinen Zug."
                            if game_config.coder_is_computer_server: self.board_view.textfield_text = "Der Server bewerten deinen Zug."

                            black_pins, white_pins = self.coder.rate_move(self.board_view, self.guesser)
                            self.guesser.evaluate_feedback(black_pins, white_pins)

                            if black_pins == config.COLUMNS:
                                game_config.game_is_over = True
                                game_config.guesser_won = True

                                for index, color in enumerate(game_config.solution):
                                    self.board_view.board[0][index] = convert_input_to_color(color)

                            else:
                                game_config.current_row -= 1

                            if game_config.current_row == 0 and black_pins != config.COLUMNS:
                                game_config.game_is_over = True
                                game_config.guesser_won = False


                            if game_config.game_is_over and not game_config.guesser_won:
                                print("Das Spiel ist vorbei. Der Kodierer hat gewonnen.")
                            elif game_config.game_is_over and game_config.guesser_won:
                                print("Das Spiel ist vorbei. Der Rater hat gewonnen.")

                            game_config.coder_is_playing = False

                        else:
                            if not game_config.rate_was_correct: self.board_view.textfield_text = "Falsche Bewertung."
                            else: self.board_view.textfield_text = "Bitte bewerte den Zug."

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
