import pygame
import sys
from .menu_model import MenuModel
from .menu_view import MenuView
from config import config


# This class handles events for the menu in the Pygame application.
class MenuController:
    def __init__(self, screen, main_app):
        """
        This is the constructor function for a menu object that initializes a model, view, and main
        application.
        
        :param screen: The screen parameter is an object that represents the display screen on which the
        menu will be displayed. It is used by the MenuView class to render the menu on the screen
        :param main_app: The `main_app` parameter is an instance of the main application class that is using
        the `Menu` class. It is passed to the `Menu` class so that the `Menu` class can communicate with the
        main application and perform any necessary actions or updates
        """
        self.model = MenuModel()
        self.view = MenuView(screen)
        self.main_app = main_app

    def handle_event(self, event):
        """
        This function handles events in a Pygame application, including quitting the application and
        executing menu commands based on mouse clicks.
        
        :param event: The event parameter is an object that represents a user input or system event that has
        occurred in the Pygame application. It could be a mouse click, keyboard press, or window close
        event, among others
        """
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, command in enumerate(self.model.menu_items):
                text = self.view.font.render(str(command), 1, (255, 255, 255))
                text_rect = text.get_rect(center=(config.WIDTH / 2, 200 + i * 50))
                if text_rect.collidepoint(x, y):
                    command.execute(self.main_app)