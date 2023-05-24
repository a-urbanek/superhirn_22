class Game:
    def __init__(self):
        """
        Initialisiert ein neues Spiel.
        """
        self.code = None  # Speichert den zu erratenden Farbcode
        self.guesses = [] # Liste mit allen bisherigen Rateversuchen
        self.hints = [] # Liste mit allen bisherigen Hinweisen

    def generate_code(self):
        """
        Generiert einen zufälligen Farbcode für das Spiel.
        """
        # Hier Code zum Generieren des Farbcodes

    def is_game_over(self):
        """
        Überprüft, ob das Spiel beendet ist.
        """
        # Hier Code zur Überprüfung des Spielendes

    def get_solution(self):
        """
        Gibt den generierten Farbcode zurück.
        """
        return self.code
