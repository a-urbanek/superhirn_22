# Konfigurationen
ROWS = 11  # Eine zusätzliche Reihe für die Farben
COLUMNS = 5
CELL_SIZE = 50
GAP_SIZE = 5
HEIGHT = ROWS * (CELL_SIZE + GAP_SIZE) + CELL_SIZE
CELL_COLOR = (169, 169, 169)
BORDER_COLOR = (0, 0, 0)
BORDER_WIDTH = 2
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
WIDTH = max(COLUMNS * (CELL_SIZE + GAP_SIZE), (len(COLORS) + 1) * (CELL_SIZE + GAP_SIZE))
FPS = 60

button_width = 100  # Breite des Buttons
button_height = 30  # Höhe des Buttons
