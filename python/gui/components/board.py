from python.config.settings import NUM_ROWS, NUM_COLUMNS


class Board:
    def __init__(self):
        """
        Initialisiert das Spielbrett.
        """
        self.grid = [[None] * NUM_COLUMNS for _ in range(NUM_ROWS)]

    def draw(self, screen):
        """
        Zeichnet das Spielbrett auf den Bildschirm.
        """
        # Hier Code zum Zeichnen des Spielbretts

    def update(self, row, column, color):
        """
        Aktualisiert die Farbe an der angegebenen Position im Spielbrett.
        """
        # Hier Code zum Aktualisieren des Spielbretts

    def clear(self):
        """
        Löscht alle Farben im Spielbrett.
        """
        # Hier Code zum Zurücksetzen des Spielbretts
