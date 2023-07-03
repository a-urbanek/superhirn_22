import pygame
from config import config

class BackGroundManager:
    def __init__(self):
        self.background = pygame.image.load('retro.png')
        self.background = pygame.transform.scale(self.background, (config.WIDTH, config.HEIGHT))
