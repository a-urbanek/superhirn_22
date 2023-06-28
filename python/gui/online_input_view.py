import pygame
import pygame.freetype

import pygame
from .menu_model import MenuModel
from config import config
from config import game_config
import numpy as np

# pygame.init()


# screen = pygame.display.set_mode(size)



class OnlineInputView:
    def __init__(self, screen):
        """
        This is the constructor function that initializes its attributes including a MenuModel
        object, a screen object, and a font object.

        :param screen: The "screen" parameter is a reference to the Pygame display surface where the
        menu will be rendered. It is used to create a MenuView object that will handle the visual
        representation of the menu
        """
        self.size = (config.WIDTH, config.HEIGHT)
        self.model = MenuModel()
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        # FONT = pygame.freetype.Font(None, 24)

    def draw_text_input_box(self, text, rect, active, label):
        color = pygame.Color('dodgerblue2') if active else pygame.Color('gray15')
        pygame.draw.rect(self.screen, color, rect, 2)
        text_surface, _ = self.font.render(text, True, pygame.Color('white'))
        self.screen.blit(text_surface, (rect.x+5, rect.y+5))
        label_surface, _ = self.font.render(label, True, pygame.Color('white'))
        self.screen.blit(label_surface, (rect.x, rect.y-30))

    def draw_button(self, rect, label, color):
        pygame.draw.rect(self.screen, color, rect)
        label_surface, _ = self.font.render(label, pygame.Color('white'))
        self.screen.blit(label_surface, (rect.x + (rect.w - label_surface.get_width()) // 2, rect.y + (rect.h - label_surface.get_height()) // 2))

    def draw(self):
        # clock = pygame.time.Clock()
        input_box1 = pygame.Rect(50, config.HEIGHT / 4, 200, 50)
        input_box2 = pygame.Rect(50, config.HEIGHT / 2, 200, 50)
        network_button = pygame.Rect(50, config.HEIGHT * 3 / 4, 200, 50)
        network_status = game_config.computer_is_network
        active1 = False
        active2 = False
        text1 = game_config.IP_ADDRESS
        text2 = str(game_config.PORT)

        done = False

        # while not done:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             done = True
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if input_box1.collidepoint(event.pos):
        #                 active1 = not active1
        #             else:
        #                 active1 = False
        #             if input_box2.collidepoint(event.pos):
        #                 active2 = not active2
        #             else:
        #                 active2 = False
        #             if network_button.collidepoint(event.pos):
        #                 # Toggle für den Netzwerkstatus
        #                 game_config.computer_is_network = not game_config.computer_is_network
        #                 print(f'Computer_is_network is now: {game_config.computer_is_network}')
        #         if event.type == pygame.KEYDOWN:
        #             if active1:
        #                 if event.key == pygame.K_BACKSPACE:
        #                     text1 = text1[:-1]
        #                 else:
        #                     text1 += event.unicode
        #             if active2:
        #                 if event.key == pygame.K_BACKSPACE:
        #                     text2 = text2[:-1]
        #                 else:
        #                     text2 += event.unicode
        #         if event.type == pygame.MOUSEBUTTONUP:
        #             # Übernehmen der Eingaben in die entsprechenden Variablen
        #             if active1:
        #                 game_config.IP_ADDRESS = text1
        #                 print(f'IP_ADDRESS is now: {game_config.IP_ADDRESS}')
        #             if active2:
        #                 game_config.PORT = int(text2)
        #                 print(f'PORT is now: {game_config.PORT}')

        self.screen.fill((30, 30, 30))
        self.draw_text_input_box(text1, input_box1, active1, "IP-Adresse:")
        self.draw_text_input_box(text2, input_box2, active2, "Port:")
        self.draw_button(network_button, "Netzwerk", pygame.Color('green') if game_config.computer_is_network else pygame.Color('red'))
        pygame.display.flip()
            # clock.tick(30)

        # pygame.quit()

# if __name__ == '__main__':
#     draw()
