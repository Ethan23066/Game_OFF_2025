from settings_game import WIDTH
from bullet import Bullet
from assets import load_sprite  # Assure-toi que le nom du fichier est bien assets.py

class Player:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, 580))
        self.speed = 5
        self.bullet_speed = 500
        self.bullet_sprite = load_sprite("bullet_blue.png")

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_position(self):
        return self.rect.center

    def fire(self):
        # Tire un bullet vers le haut
        return Bullet(
            x=self.rect.centerx,
            y=self.rect.top,
            direction=(0, -1),
            speed=self.bullet_speed,
            sprite_name="bullet_blue.png"
        )
