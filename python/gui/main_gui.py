import pygame

from python.gui.components.board import Board
from python.gui.components.menu import Menu
from python.logic.computer_player import ComputerPlayer
from python.logic.game import Game


class MainGUI:
    def __init__(self):
        """
        Initialisiert die Haupt-GUI des Mastermind-Spiels.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mastermind")

        self.board = Board()
        self.menu = Menu()

        self.game = Game()
        self.computer_player = ComputerPlayer()

    def run(self):
        """
        Startet die Hauptschleife der GUI.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    def handle_events(self):
        """
        Behandelt die Ereignisse der GUI.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Weitere Ereignisbehandlung hier

    def update(self):
        """
        Aktualisiert den Spielzustand.
        """
        # Hier Code zur Aktualisierung des Spielzustands

    def render(self):
        """
        Rendert das Spiel auf den Bildschirm.
        """
        self.screen.fill((255, 255, 255))  # Beispielhafte Hintergrundfarbe
        self.board.draw(self.screen)
        self.menu.draw(self.screen)
        # Weitere Rendervorgänge hier
        pygame.display.flip()
