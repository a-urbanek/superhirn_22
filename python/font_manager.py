"""
Module for managing fonts
"""
import pygame


class FontManager:
    """The `FontManager` class initializes a dictionary of fonts and provides 
    a method to retrieve the current font."""

    def __init__(self):
        """
        The function initializes a dictionary of fonts with a default font and font size.
        """
        pygame.font.init()
        self.fonts = {"PressStart2P": pygame.font.Font(
            'PressStart2P-Regular.ttf', 18)}
        self.current_font ="PressStart2P"

    def get_font(self):
        """
        The function `get_font` returns the current font from a list of fonts.
        :return: The font corresponding to the current_font value.
        """
        return self.fonts[self.current_font]
