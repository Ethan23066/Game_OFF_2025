import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 5, y - 10, 10, 20)
        self.speed = -6

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)

    def is_off_screen(self):
        return self.rect.bottom < 0

    def get_rect(self):
        return self.rect
