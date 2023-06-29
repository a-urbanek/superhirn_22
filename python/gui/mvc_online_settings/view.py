from gui.commands.menu_command import MenuCommand
import sys
import pygame
from .ui_elements.text_box import TextBox
from .ui_elements.check_box import CheckBox
sys.path.insert(0, '..')


class Label:
    def __init__(self, position, text, font):
        self.position = position
        self.text = text
        self.font = font

    def draw(self, screen):
        text_surface = self.font.render(
            self.text, True, (255, 255, 255))  # Assuming white text
        screen.blit(text_surface, self.position)


class Button:
    def __init__(self, position, width, height, color=(255, 255, 255), text="", callback=None):
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        txt_surface = self.font.render(self.text, True, self.color)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()


class View:
    def __init__(self, screen, main_app, model):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.model = model


        # UI elements
        self.return_button = Button(
            (10, 10), 80, 30, text="Return", callback=MenuCommand(main_app).execute)
        self.super_checkbox = CheckBox((50, 60), 20, 20, self.model, 'super_mode')
        self.super_checkbox_label = Label(
            (80, 60), "supersuper mode", self.font)
        self.online_checkbox = CheckBox((50, 100), 20, 20, self.model, 'online_mode')
        self.online_checkbox_label = Label((80, 100), "online mode", self.font)
        self.port_textbox = TextBox((50, 140), 200, 40, self.model, 'port')
        self.port_label = Label((260, 140), "port", self.font)
        self.ip_textbox = TextBox((50, 190), 200, 40, self.model, 'ip_address')
        self.ip_label = Label((260, 190), "ip", self.font)

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
