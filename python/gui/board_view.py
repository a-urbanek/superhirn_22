import pygame
import pygame_gui

import config.config as config
import config.game_config as game_config


class BoardView:
    def __init__(self, screen, color_cell_handler, button_callback):
        """
        Initialisiert die BoardView-Klasse.
        :param screen: Der Pygame-Bildschirm, auf dem das Spielbrett angezeigt werden soll
        :param color_cell_handler: Die Handler-Funktion zum Einfärben einer Zelle
        :param button_callback: Die Callback-Funktion, die aufgerufen wird, wenn der Button geklickt wird
        """
        self.screen = screen
        self.color_cell_handler = color_cell_handler
        self.button_callback = button_callback
        self.dragging = False
        self.dragged_color = None
        self.start_pos = (0, 0)
        self.current_pos = (0, 0)
        self.used_colors = config.COLORS if game_config.player_is_guesser or not game_config.code_is_coded else config.FEEDBACK_COLORS

        # Initialisierung des Spielbretts
        self.board = [[None] * config.COLUMNS for _ in range(config.ROWS)]
        self.board_feedback = [[None] * config.COLUMNS for _ in range(config.ROWS)]

        # GUI-Manager erstellen
        self.gui_manager = pygame_gui.UIManager(screen.get_size())

        # Button-Parameter
        self.button_rect = pygame.Rect(len(self.used_colors) * (config.CELL_SIZE + config.GAP_SIZE) + 2 * config.MARGIN,
                                       config.ROWS * (config.CELL_SIZE + config.GAP_SIZE) + 2 * config.MARGIN, 100, 50)
        self.button_color = (255, 0, 0)
        self.button_text = "Button"
        self.button_font = pygame.font.Font(None, 24)

        # Feedback-Kugeln
        self.feedback_balls = [[None] * config.FEEDBACK_COLUMNS for _ in range(config.FEEDBACK_ROWS)]

    def draw(self):
        """
        Zeichnet das Spielbrett auf den Bildschirm.
        """
        # UI-Elemente zeichnen
        self.gui_manager.draw_ui(self.screen)

        self.used_colors = config.COLORS if game_config.player_is_guesser or not game_config.code_is_coded else config.FEEDBACK_COLORS

        # Rahmen um das Spielfeld zeichnen
        board_rect = pygame.Rect(
            config.MARGIN,
            config.MARGIN,
            config.COLUMNS * (config.CELL_SIZE + config.GAP_SIZE),
            config.ROWS * (config.CELL_SIZE + config.GAP_SIZE)
        )

        pygame.draw.rect(self.screen, (255, 0, 0), board_rect, 3)

        # Rahmen um die Feedback-Kugeln zeichnen
        feedback_rect = pygame.Rect(
            config.COLUMNS * (config.CELL_SIZE + config.GAP_SIZE) + 2 * config.MARGIN,
            config.MARGIN + (config.CELL_SIZE + config.GAP_SIZE),
            config.COLUMNS * (config.FEEDBACK_CELL_SIZE + config.GAP_SIZE),
            (config.ROWS - 1) * (config.CELL_SIZE + config.GAP_SIZE)
        )

        pygame.draw.rect(self.screen, (0, 0, 255), feedback_rect, 3)

        # Zeichnen der leeren Zellen des Spielbretts
        for row in range(config.ROWS):
            for column in range(config.COLUMNS):
                cell_x = column * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
                cell_y = row * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
                radius = config.CELL_SIZE // 2
                pygame.draw.circle(
                    self.screen,
                    config.CELL_COLOR,
                    (cell_x, cell_y),
                    radius
                )

        # Zeichnen der schwarzen und weißen Pins
        x_start_feedback = config.COLUMNS * (
                config.CELL_SIZE + config.GAP_SIZE) + 2 * config.MARGIN + config.FEEDBACK_CELL_SIZE // 2
        y_start_feedback = config.MARGIN + config.CELL_SIZE // 2
        for row in range(config.ROWS):
            if (row != 0):
                for column in range(config.COLUMNS):
                    cell_x = x_start_feedback + column * (config.FEEDBACK_CELL_SIZE + config.GAP_SIZE)
                    cell_y = y_start_feedback + row * (config.CELL_SIZE + config.GAP_SIZE)
                    radius = config.FEEDBACK_CELL_SIZE // 2
                    pygame.draw.circle(
                        self.screen,
                        config.CELL_COLOR,
                        (cell_x, cell_y),
                        radius
                    )

        # Zeichnen der bereits eingefärbten Zellen
        for row in range(config.ROWS):
            if (row != 0):
                for column in range(config.COLUMNS):
                    if self.board_feedback[row][column] is not None:
                        cell_x = x_start_feedback + column * (config.FEEDBACK_CELL_SIZE + config.GAP_SIZE)
                        cell_y = y_start_feedback + row * (config.CELL_SIZE + config.GAP_SIZE)
                        radius = config.FEEDBACK_CELL_SIZE // 2
                        pygame.draw.circle(
                            self.screen,
                            self.board_feedback[row][column],
                            (cell_x, cell_y),
                            radius
                        )

        # Zeichnen der Farbzellen
        for i, color in enumerate(self.used_colors):
            circle_x = i * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
            circle_y = (config.ROWS) * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN * 2
            circle_radius = config.CELL_SIZE // 2
            if self.dragging and self.dragged_color == color:
                circle_x = self.current_pos[0]
                circle_y = self.current_pos[1]
            pygame.draw.circle(
                self.screen,
                color,
                (circle_x, circle_y),
                circle_radius
            )

        # Zeichnen der bereits eingefärbten Zellen
        for row in range(config.ROWS):
            for column in range(config.COLUMNS):
                if self.board[row][column] is not None:
                    cell_x = column * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
                    cell_y = row * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
                    radius = config.CELL_SIZE // 2
                    pygame.draw.circle(
                        self.screen,
                        self.board[row][column],
                        (cell_x, cell_y),
                        radius

                    )

        # Zeichnen des Buttons
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        button_text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
        button_text_rect = button_text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text_surface, button_text_rect)

    def start_drag(self, start_pos):
        """
        Startet den Drag-Vorgang.
        :param start_pos: Die Startposition des Drag-Vorgangs
        """
        if not self.dragging:
            self.dragging = True
            self.dragged_color = self.get_clicked_color(start_pos)
            self.start_pos = start_pos
            self.current_pos = start_pos

    def drop(self, drop_pos):
        """
        Behandelt das Ablegen der gezogenen Farbzelle.
        :param drop_pos: Die Position, an der die Farbzelle abgelegt wurde
        """
        if self.button_rect.collidepoint(drop_pos):
            # Überprüfen, ob der Button geklickt wurde
            self.button_callback(self)
        else:
            # Einfärben der Zelle, wenn sie im Spielbrettbereich liegt
            drop_row, drop_column, isLeftBoard = self.get_clicked_cell(drop_pos)
            if drop_row is not None and drop_column is not None:
                self.color_cell_handler(self, drop_row, drop_column, self.dragged_color, isLeftBoard)
        self.dragging = False

    def update(self):
        """
        Aktualisiert den aktuellen Zustand des Drag-Vorgangs.
        """
        if self.dragging:
            self.current_pos = pygame.mouse.get_pos()

        self.gui_manager.update(pygame.time.get_ticks() / 1000.0)

    def get_clicked_cell(self, mouse_pos):
        """
        Ermittelt die Zelle, die anhand der Mausposition angeklickt wurde.
        :param mouse_pos: Die aktuelle Mausposition
        :return: Die Zeilen- und Spaltennummer der angeklickten Zelle
        """
        x, y = mouse_pos
        margin = config.MARGIN
        cell_size = config.CELL_SIZE
        gap_size = config.GAP_SIZE
        feedback_cell_size = config.FEEDBACK_CELL_SIZE
        columns = config.COLUMNS
        rows = config.ROWS
        is_left = True

        column = 0  # Standardwert
        row = 0  # Standardwert

        if margin <= x <= margin + columns * (cell_size + gap_size) and margin <= y <= rows * (
                cell_size + gap_size) + margin:
            updated_x_position = x - margin
            updated_y_position = y - margin
            row = updated_y_position // (cell_size + gap_size)
            column = updated_x_position // (cell_size + gap_size)
        elif 2 * margin + columns * (cell_size + gap_size) <= x <= 2 * margin + columns * (
                cell_size + gap_size + feedback_cell_size + config.FEEDBACK_GAP_SIZE) and \
                margin + cell_size + gap_size <= y <= rows * (cell_size + gap_size) + margin:
            is_left = False
            updated_x_position = x - 2 * margin - columns * (cell_size + gap_size)
            updated_y_position = y - margin - cell_size - gap_size
            column = updated_x_position // (feedback_cell_size + gap_size)
            row = updated_y_position // (cell_size + gap_size)

        return row, column, is_left

    def get_clicked_color(self, mouse_pos):
        """
        Ermittelt die Farbe, die anhand der Mausposition angeklickt wurde.
        :param mouse_pos: Die aktuelle Mausposition
        :return: Die ausgewählte Farbe
        """
        for i, color in enumerate(self.used_colors):
            circle_x = i * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN
            circle_y = (config.ROWS) * (config.CELL_SIZE + config.GAP_SIZE) + config.CELL_SIZE // 2 + config.MARGIN * 2
            circle_radius = config.CELL_SIZE // 2
            if circle_x - circle_radius <= mouse_pos[0] <= circle_x + circle_radius and circle_y - circle_radius <= \
                    mouse_pos[1] <= circle_y + circle_radius:
                return color
        return None
