import pygame
from .menu_model import MenuModel 
from config import config

class MenuView:
    def __init__(self, screen):
        """
        This is the constructor function that initializes its attributes including a MenuModel
        object, a screen object, and a font object.
        
        :param screen: The "screen" parameter is a reference to the Pygame display surface where the
        menu will be rendered. It is used to create a MenuView object that will handle the visual
        representation of the menu
        """
        self.model = MenuModel()
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
