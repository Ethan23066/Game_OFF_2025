import pygame
from ennemy import Enemy

class WaveManager:
    def __init__(self, enemy_surface, max_waves=5):
        self.enemy_surface = enemy_surface
        self.current_wave = 0
        self.max_waves = max_waves
        self.enemies = []

    def spawn_wave(self):
        if self.current_wave >= self.max_waves:
            return []

        self.enemies = []
        for x in range(10):
            enemy = Enemy(self.enemy_surface, x * 60, 50)
            self.enemies.append(enemy)

        self.current_wave += 1
        return self.enemies

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def is_wave_cleared(self):
        return len(self.enemies) == 0

    def check_player_health(self, player):
        if player.health <= 0:
            self.max_waves = self.current_wave
