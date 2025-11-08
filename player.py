import pygame
from settings_game import WIDTH
from bullet import Bullet
from assets import load_sprite

class Player:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, 580))
        self.speed = 5
        self.bullet_speed = 500
        self.bullet_sprite = load_sprite("bullet_blue.png")

        self.last_fire_time = 0
        self.fire_delay = 200  # ms

        self.stamina = 0
        self.max_stamina = 100
        self.stamina_regen_rate = 5  # par seconde
        self.stamina_move_cost = 1
        self.stamina_fire_cost = 5

        self.health = 100
        self.max_health = 100

    def move_left(self):
        if self.stamina >= self.stamina_move_cost:
            self.rect.x -= self.speed
            self.stamina -= self.stamina_move_cost
            if self.rect.left < 0:
                self.rect.left = 0

    def move_right(self):
        if self.stamina >= self.stamina_move_cost:
            self.rect.x += self.speed
            self.stamina -= self.stamina_move_cost
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_position(self):
        return self.rect.center

    def fire(self):
        now = pygame.time.get_ticks()
        if (
            now - self.last_fire_time >= self.fire_delay
            and self.stamina >= self.stamina_fire_cost
        ):
            self.last_fire_time = now
            self.stamina -= self.stamina_fire_cost
            return Bullet(
                x=self.rect.centerx,
                y=self.rect.top,
                direction=(0, -1),
                speed=self.bullet_speed,
            )
        return None

    def regen_stamina(self, dt):
        self.stamina += self.stamina_regen_rate * dt
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
