import pygame

class Label:
    def __init__(self, position, text, font):
        self.position = position
        self.text = text
        self.font = font

    def draw(self, screen):
        text_surface = self.font.render(
            self.text, True, (255, 255, 255))  # Assuming white text
        screen.blit(text_surface, self.position)
