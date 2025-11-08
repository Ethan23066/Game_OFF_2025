import pygame
from assets import load_sprite
# Assure-toi que le nom du fichier est bien assets.py

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, sprite_name="bullet_blue.png"):
        super().__init__()
        self.image = load_sprite(sprite_name)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction  # tuple (dx, dy)
        self.speed = speed

    def update(self, dt):
        dx = self.direction[0] * self.speed * dt
        dy = self.direction[1] * self.speed * dt
        self.rect.x += dx
        self.rect.y += dy

        # Suppression si hors écran
        if (self.rect.bottom < 0 or self.rect.top > 720 or
            self.rect.right < 0 or self.rect.left > 1280):
            self.kill()
