import pygame
from config import config
from config import game_config
import numpy as np


class MenuView:
    def __init__(self, screen, model):
        """
        This is the constructor function that initializes its attributes including a MenuModel
        object, a screen object, and a font object.

        :param screen: The "screen" parameter is a reference to the Pygame display surface where the
        menu will be rendered. It is used to create a MenuView object that will handle the visual
        representation of the menu
        """
        self.model = model
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """
        This function draws menu items on the screen in white color centered at specific positions.
        """
        self.screen.fill((0, 0, 0))
        for i, command in enumerate(self.model.menu_items):
            text = self.font.render(str(command), 1, (255, 255, 255))
            text_rect = text.get_rect(center=(config.WIDTH / 2, 200 + i * 50))
            self.screen.blit(text, text_rect)
        pygame.display.flip()

    def clearSetting(self):
        game_config.game_is_over = False
        game_config.board_guess = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.board_final = np.empty((config.ROWS, config.COLUMNS), dtype=object)
        game_config.feedback_board_final = np.empty(((config.ROWS - 1), config.COLUMNS), dtype=object)
        game_config.solution = np.empty(config.COLUMNS, dtype=object)
        game_config.code_is_coded = False
        game_config.current_row = config.ROWS - 1
        pass
