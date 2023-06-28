import pygame
import pygame.freetype

import config.config

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Fenstergröße
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# Button-Größe
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

# Texteingabe-Größe
TEXT_INPUT_WIDTH = 200
TEXT_INPUT_HEIGHT = 60


class MenuViewUpdate:
    def __init__(self, screen, handle_button_start_game_click):
        self.screen = screen
        self.marked_buttons = []
        self.text_input1 = ""
        self.text_input2 = ""
        self.server_button_selected = False
        self.button_exit_callback = handle_button_start_game_click

    def check_button_collision(self, mouse_pos, button_rect):
        if button_rect.collidepoint(mouse_pos):
            return True
        return False

    def draw_buttons(self):
        # Spielmodus-Reihe
        pygame.draw.rect(self.screen, GRAY, (50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, GRAY, (250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, GRAY, (450, 50, BUTTON_WIDTH, BUTTON_HEIGHT))

        # Ratende Person-Reihe
        pygame.draw.rect(self.screen, GRAY, (50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, GRAY, (250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))

        # Kodierende Person-Reihe
        pygame.draw.rect(self.screen, GRAY, (50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, GRAY, (250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, GRAY, (450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

        # Markierte Buttons zeichnen
        for button in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, button, 3)

    # def check_selected_buttons(self):
    #     print("Aufgerufen")
    #     selected_buttons = []
    #     if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Superhirn")
    #     if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Supersuperhirn")
    #     if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Spieler")
    #     if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Computer")
    #     if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Spieler")
    #     if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Computer")
    #     if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
    #         selected_buttons.append("Server")
    #     print("Ausgewählte Buttons:", selected_buttons)
    #     print(self.text_input1)
    #     print(self.text_input2)

    def draw_text_inputs(self):
        pygame.draw.rect(self.screen, WHITE, (300, 400, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT))
        pygame.draw.rect(self.screen, WHITE, (550, 400, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT))
        font = pygame.freetype.Font(None, 20)
        font.render_to(self.screen, (305, 405), "Eingabe 1:", BLACK)
        font.render_to(self.screen, (555, 405), "Eingabe 2:", BLACK)
        font.render_to(self.screen, (305, 425), self.text_input1, BLACK)
        font.render_to(self.screen, (555, 425), self.text_input2, BLACK)

    def draw(self):
        self.screen.fill(BLACK)

        # Button-Texte erstellen
        font = pygame.font.Font(None, 24)
        superhirn_text = font.render("Superhirn", True, WHITE)
        supersuperhirn_text = font.render("Supersuperhirn", True, WHITE)
        spieler_text = font.render("Spieler", True, WHITE)
        computer_text = font.render("Computer", True, WHITE)
        server_text = font.render("Server", True, WHITE)
        bestaetigen_text = font.render("Spiel Starten!", True, WHITE)

        # Spielmodus-Reihe
        self.screen.blit(superhirn_text, (65, 65))
        self.screen.blit(supersuperhirn_text, (265, 65))

        # Überprüfen, ob Superhirn-Button markiert ist
        if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (50, 50, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (250, 50, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        # Ratende Person-Reihe
        self.screen.blit(spieler_text, (80, 165))
        self.screen.blit(computer_text, (280, 165))

        # Überprüfen, ob Spieler-Button markiert ist
        if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (50, 150, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (250, 150, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        # Kodierende Person-Reihe
        self.screen.blit(spieler_text, (80, 265))
        self.screen.blit(computer_text, (280, 265))
        self.screen.blit(server_text, (480, 265))

        # Überprüfen, ob Spieler-Button markiert ist
        if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (50, 250, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (250, 250, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            pygame.draw.rect(self.screen, RED, (450, 250, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

        # Bestätigen-Button
        pygame.draw.rect(self.screen, GRAY, (config.config.MARGIN, 600, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.screen.blit(bestaetigen_text, (config.config.MARGIN, 600))

        # Texteingabefelder zeichnen, wenn der "Server"-Button ausgewählt ist
        if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
            self.server_button_selected = True
        else:
            self.server_button_selected = False
        if self.server_button_selected:
            self.draw_text_inputs()

        pygame.display.flip()

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.check_button_collision(mouse_pos, pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(250, 50, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(250, 150, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(50, 150, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        if pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                            self.marked_buttons.remove(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                        else:
                            self.marked_buttons.append(pygame.Rect(450, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(50, 250, BUTTON_WIDTH, BUTTON_HEIGHT))
                            if pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT) in self.marked_buttons:
                                self.marked_buttons.remove(pygame.Rect(250, 250, BUTTON_WIDTH, BUTTON_HEIGHT))

                    elif self.check_button_collision(mouse_pos, pygame.Rect(config.config.MARGIN, 600, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        self.handle_button_start_game_click()

                elif event.type == pygame.KEYDOWN:
                    self.check_selected_buttons()
                    if self.server_button_selected:
                        if pygame.Rect(300, 400, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT).collidepoint(
                                pygame.mouse.get_pos()):
                            if event.key == pygame.K_BACKSPACE:
                                if len(self.text_input1) > 0:
                                    self.text_input1 = self.text_input1[:-1]
                            elif event.key == pygame.K_RETURN:
                                pass
                            else:
                                self.text_input1 += event.unicode
                        elif pygame.Rect(550, 400, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT).collidepoint(
                                pygame.mouse.get_pos()):
                            if event.key == pygame.K_BACKSPACE:
                                if len(self.text_input2) > 0:
                                    self.text_input2 = self.text_input2[:-1]
                            elif event.key == pygame.K_RETURN:
                                pass
                            else:
                                self.text_input2 += event.unicode