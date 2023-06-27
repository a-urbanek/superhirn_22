import pygame
import time

class CheckBox:
    def __init__(self, position, width, height, color=(255, 255, 255), checked=False):
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.color = color
        self.checked = checked
        self.last_event_time = 0
        self.debounce_delay = 0.5  # Debounce delay in seconds

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        if self.checked:
            pygame.draw.rect(screen, (255, 0, 0), self.rect.inflate(-4, -4))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
            current_time = time.time()
            if current_time - self.last_event_time > self.debounce_delay:
                if self.rect.collidepoint(event.pos):
                    self.checked = not self.checked
                    self.last_event_time = current_time

                    if self.checked:
                        print("CHECKED")
                    else:
                        print("UNCHECKED")
