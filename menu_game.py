import pygame
from settings_game import WIDTH, HEIGHT, FONT_NAME

class Menu:
    def __init__(self):
        self.active = True
        self.font_title = pygame.font.SysFont(FONT_NAME, 48)
        self.font_prompt = pygame.font.SysFont(FONT_NAME, 24)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.active = False

    def draw(self, screen):
        screen.fill((0, 0, 0))

        title = self.font_title.render("SPACE INVADERS", True, (0, 255, 0))
        prompt = self.font_prompt.render("Press ENTER to Start", True, (255, 255, 255))

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
