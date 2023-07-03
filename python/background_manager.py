import pygame
import os
import sys
from config import config

class BackGroundManager:
    def __init__(self):
        self.background = pygame.image.load(self.resource_path('retro.png'))
        self.background = pygame.transform.scale(self.background, (config.WIDTH, config.HEIGHT))

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
