# Konfigurationen für das Spiel

# Anzahl der Reihen (eine zusätzliche Reihe für die Farben)
ROWS = 10
# ROWS = 3  # Beispiel: Anzahl der Reihen auf 3 reduziert

# Anzahl der Spalten
COLUMNS = 5

# Größe einer Zelle im Spielbrett
CELL_SIZE = 50

# Abstand zwischen den Zellen
GAP_SIZE = 5

# Farbe einer Zelle
CELL_COLOR = (128, 128, 128)

# Farbe des Spielbrett-Rahmens
BORDER_COLOR = (0, 0, 0)

# Breite des Spielbrett-Rahmens
BORDER_WIDTH = 2

# Anzahl der Spalten im Feedback-Board
FEEDBACK_COLUMNS = 5

# Anzahl der Reihen im Feedback-Board
FEEDBACK_ROWS = 10

# Größe einer Zelle im Feedback-Board
FEEDBACK_CELL_SIZE = 30

# Abstand zwischen den Zellen im Feedback-Board
FEEDBACK_GAP_SIZE = GAP_SIZE

# Farben für die Zellen im Spielbrett
COLORS = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 128, 0), (153, 76, 0), (255, 255, 255), (0, 0, 0)]

# Farbennummern für die Zellen im Spielbrett
COLORS_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]

# Farben für die Zellen im Feedback-Board
FEEDBACK_COLORS = [(255, 255, 255), (0, 0, 0)]

# Farbennummern für die Zellen im Feedback-Board
FEEDBACK_COLORS_NUMBERS = [7, 8]

# Framerate des Spiels
FPS = 60

# Randabstand des Spielbretts vom Bildschirmrand
MARGIN = 30

# Höhe des Textfelds
TEXTFIELD_HEIGHT = 100

# Berechnung der Breite des Fensters basierend auf der Anzahl der Spalten und der Zellengröße
WIDTH = (
    COLUMNS * (CELL_SIZE + FEEDBACK_CELL_SIZE)
    + (COLUMNS - 1) * (FEEDBACK_GAP_SIZE + GAP_SIZE)
    + 3 * MARGIN
) if (
    COLUMNS * (CELL_SIZE + FEEDBACK_CELL_SIZE)
    + (COLUMNS - 1) * (FEEDBACK_GAP_SIZE + GAP_SIZE)
    + 3 * MARGIN
) > (
    3 * MARGIN + len(COLORS) * (CELL_SIZE + GAP_SIZE) + 100
) else (
    3 * MARGIN + len(COLORS) * (CELL_SIZE + GAP_SIZE) + 100
)

# Berechnung der Höhe des Fensters basierend auf der Anzahl der Reihen und der Zellengröße
HEIGHT = (
    (ROWS + 1) * (CELL_SIZE + GAP_SIZE)
    + 5 * MARGIN
    + TEXTFIELD_HEIGHT
) if (
    (ROWS + 1) * (CELL_SIZE + GAP_SIZE)
    + 5 * MARGIN
    + TEXTFIELD_HEIGHT
) > 500 else 500

# Breite des Buttons
button_width = 100

# Höhe des Buttons
button_height = 30
