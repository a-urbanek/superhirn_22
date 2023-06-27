import pygame
from .model import Model
from config import config
from .ui_elements.text_box import TextBox 
from .ui_elements.check_box import CheckBox

class View:
    def __init__(self, screen):
        self.model = Model()
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        # UI elements
        self.online_checkbox = CheckBox((50, 50), 20, 20)
        self.hostname_textbox = TextBox((50, 80), 200, 40)
        self.ip_textbox = TextBox((50, 120), 200, 40)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.online_checkbox.draw(self.screen)
        self.hostname_textbox.draw(self.screen)
        self.ip_textbox.draw(self.screen)
        pygame.display.flip()
    
    def update(self, event):
        self.online_checkbox.update(event)
        self.hostname_textbox.update(event)
        self.ip_textbox.update(event)
        self.draw()
