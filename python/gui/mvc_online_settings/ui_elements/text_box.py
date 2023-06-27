import pygame


class TextBox:
    def __init__(self, position, width, height, color=(255, 255, 255), text=""):
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        txt_surface = self.font.render(self.text, True, self.color)
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
            if self.rect.collidepoint(event.pos):
                self.active = True
                # print("ACTIVE")
            else:
                self.active = False
                # print("ACTIVE-FALSE")
        if event.type == pygame.KEYDOWN and self.active:  # pylint: disable=E1101
            if event.key == pygame.K_RETURN:  # pylint: disable=E1101
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:  # pylint: disable=E1101
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
