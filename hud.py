import pygame

class HUD:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.SysFont(None, 24)

    def draw_bar(self, screen, x, y, value, max_value, color, label):
        width = 200
        height = 20
        ratio = max(0, min(1, value / max_value))
        filled = int(width * ratio)

        # Fond
        pygame.draw.rect(screen, (50, 50, 50), (x, y, width, height))
        # Barre remplie
        pygame.draw.rect(screen, color, (x, y, filled, height))
        # Texte
        text = self.font.render(f"{label}: {int(value)}", True, (255, 255, 255))
        screen.blit(text, (x, y - 20))

    def draw(self, screen):
        self.draw_bar(screen, 20, 20, self.player.stamina, self.player.max_stamina, (0, 255, 0), "Stamina")
        self.draw_bar(screen, 20, 60, self.player.health, self.player.max_health, (255, 0, 0), "Health")
