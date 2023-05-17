import pygame
from python.gui.components.board import Board
from python.gui.components.menu import Menu

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

    def run(self):
        """
        Startet die Hauptschleife der GUI.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Beispielhafte Hintergrundfarbe
            self.board.draw(self.screen)
            self.menu.draw(self.screen)

            pygame.display.flip()

if __name__ == "__main__":
    main_gui = MainGUI()
    main_gui.run()
