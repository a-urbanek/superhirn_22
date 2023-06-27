import pygame
import sys
from .model import Model
from .view import View
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import MainApp    

class Controller:
    def __init__(self, screen, main_app: 'MainApp'):
        self.model = Model()
        self.view = View(screen)
        self.main_app = main_app

    def handle_event(self, event):
        if event.type == pygame.QUIT: # pylint: disable=E1101
            sys.exit()
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]: # pylint: disable=E1101
            self.view.update(event)
