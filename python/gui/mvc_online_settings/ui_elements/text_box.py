import pygame

class TextBox:
    def __init__(self, position, width, height, model, prop_name, color=(255, 255, 255)):
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.color = color
        self.model = model  # Store a reference to the model
        self.prop_name = prop_name  # The name of the property in the model
        self.font = pygame.font.Font(None, 36)
        self.active = False

    @property
    def text(self):
        return getattr(self.model, self.prop_name)

    @text.setter
    def text(self, value):
        setattr(self.model, self.prop_name, value)

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)  # Red border with increased thickness
        else:
            pygame.draw.rect(screen, self.color, self.rect, 2)  # Original color and thickness

        txt_surface = self.font.render(self.text, True, self.color)
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:  # pylint: disable=E1101
            if event.key == pygame.K_RETURN:  # pylint: disable=E1101
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:  # pylint: disable=E1101
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
