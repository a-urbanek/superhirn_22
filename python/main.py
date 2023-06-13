import pygame

from config import config
from config import game_config
from constants import MENU, GAME
from gui.board_view import BoardView
from gui.menu_controller import MenuController
from gui.menu_view import MenuView
from logic.computer_local_coder import ComputerLocalCoder
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

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            if value in [MENU, GAME]:
                print("setting..." + value)
                self._state = value
            else:
                raise ValueError("Invalid view state")

        self._state = MENU

        # It creates an instance of the `MenuView` class, passing in the `screen` object as a parameter. This
        # is used to display the menu screen in the game.
        self.menu_view = MenuView(self.screen)
        self.menu_controller = MenuController(self.screen, self)

        # Erstellen eines BoardView-Objekts mit dem Bildschirm und der Farbzellen-Methode
        self.board_view = BoardView(self.screen, self.color_cell, self.handle_button_click)

        # Erstellen eines ComputerCoder-Objekts
        self.computer = ComputerLocalCoder()

        # Erstellen des Players
        self.player = PlayerGuesser()

    def handle_button_click(self, board_view):
        """
        Die Methode, die aufgerufen wird, wenn der Button geklickt wird.
        Überprüft, ob alle Farben in der aktuellen Reihe ausgewählt wurden.
        Wenn ja, wird die Meldung "Row complete" ausgegeben und die aktuelle Reihe verringert.
        """

        if game_config.computer_is_playing == False:
            self.player.make_move()

    def color_cell(self, board_view, row, column, color):
        """
        Färbt eine Zelle in Abhängigkeit von ihrer Zeilennummer ein.
        Wenn die Zeilennummer mit der aktuellen Reihe übereinstimmt und der Spieler der Rater ist,
        wird die Zelle eingefärbt und die entsprechende Farbe im Rate-Board gespeichert.
        :param board_view: Das BoardView-Objekt, auf dem die Zelle eingefärbt werden soll
        :param row: Die Zeilennummer der Zelle
        :param column: Die Spaltennummer der Zelle
        :param color: Die Farbe, mit der die Zelle eingefärbt werden soll
        """
        if row == game_config.current_row and game_config.player_is_guesser:
            game_config.board_guess[row, column] = color
            board_view.board[row][column] = color

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
                if game_config.computer_is_playing:
                    self.computer.rate_moe()

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
                self.screen.fill((0, 0, 0))

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
