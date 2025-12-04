import pygame
from settings_game import WIDTH, HEIGHT, FONT_NAME

class MenuSelectControl:
    def __init__(self):
        self.options = ["keyboard", "gamepad", "mobile"]
        self.selected = 0
        self.active = True
        self.font = pygame.font.SysFont(FONT_NAME, 32)
        self.title_font = pygame.font.SysFont(FONT_NAME, 48)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.active = False
                return self.options[self.selected]
        return None

    def draw(self, screen):
        screen.fill((0, 0, 0))
        title = self.title_font.render("Select Control Mode", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))

        for i, option in enumerate(self.options):
            color = (0, 255, 0) if i == self.selected else (255, 255, 255)
            text = self.font.render(option.upper(), True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + i * 40))

        pygame.display.flip()
