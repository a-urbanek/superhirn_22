from gui.commands.menu_command import MenuCommand
import sys
import pygame
from .ui_elements.text_box import TextBox
from .ui_elements.check_box import CheckBox
from .ui_elements.button import Button
from .ui_elements.label import Label
sys.path.insert(0, '..')

class View:
    def __init__(self, screen, main_app, model):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.model = model

        # UI elements
        self.return_button = Button(
            (10, 10), 90, 40, text="Return", callback=MenuCommand(main_app).execute)
        self.super_checkbox = CheckBox((50, 70), 20, 20, self.model, 'super_mode')  # Added 10 to y position
        self.super_checkbox_label = Label(
            (80, 70), "supersuper mode", self.font)  # Added 10 to y position
        self.online_checkbox = CheckBox((50, 110), 20, 20, self.model, 'online_mode')  # Added 10 to y position
        self.online_checkbox_label = Label((80, 110), "online mode", self.font)  # Added 10 to y position
        self.port_textbox = TextBox((50, 150), 200, 40, self.model, 'port')  # Added 10 to y position
        self.port_label = Label((260, 150), "port", self.font)  # Added 10 to y position
        self.ip_textbox = TextBox((50, 200), 200, 40, self.model, 'ip_address')  # Added 10 to y position
        self.ip_label = Label((260, 200), "ip", self.font)  # Added 10 to y position

    def draw(self):
        """
        This function draws the ui elements on the screen and updates
        the display.
        """
        self.screen.fill((0, 0, 0))
        self.return_button.draw(self.screen)
        self.super_checkbox.draw(self.screen)
        self.super_checkbox_label.draw(self.screen)
        self.online_checkbox.draw(self.screen)
        self.online_checkbox_label.draw(self.screen)
        self.port_textbox.draw(self.screen)
        self.port_label.draw(self.screen)
        self.ip_textbox.draw(self.screen)
        self.ip_label.draw(self.screen)
        pygame.display.flip()

    def update(self, event):
        """
        This function updates the ui elements.

        :param event: The "event" parameter is likely an object that contains information about a user input
        event, such as a mouse click or keyboard press. This method is likely being called within a larger
        program or GUI framework, and the "update" method is responsible for updating the state of various
        UI elements based on the
        """
        self.super_checkbox.update(event)
        self.online_checkbox.update(event)
        self.port_textbox.update(event)
        self.ip_textbox.update(event)
        self.return_button.update(event)
