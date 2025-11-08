import pygame
from settings_game import WIDTH, FONT_NAME, WHITE, RED

class Interface:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.game_over = False
        self.font = pygame.font.SysFont(FONT_NAME, 24)

    def reset(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.game_over = False

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.set_game_over()

    def next_level(self):
        self.level += 1

    def set_game_over(self):
        self.game_over = True

    def draw(self, screen):
        screen.blit(self.font.render(f"Score: {self.score}", True, WHITE), (10, 10))
        screen.blit(self.font.render(f"Level: {self.level}", True, WHITE), (10, 40))
        screen.blit(self.font.render(f"Lives: {self.lives}", True, WHITE), (10, 70))

        if self.game_over:
            over = self.font.render("GAME OVER", True, RED)
            screen.blit(over, (WIDTH // 2 - over.get_width() // 2, 300))
