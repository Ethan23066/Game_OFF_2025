from ennemy import Enemy

class WaveManager:
    def __init__(self, enemy_surface):
        self.enemy_surface = enemy_surface
        self.current_wave = 0
        self.max_waves = None
        self.enemies = []
        self.virtual_time = 0.0
        self.virtual_time_total = 0.0
        self.wave_time_limit = 15.0

    def spawn_wave(self):
        if self.max_waves is not None and self.current_wave >= self.max_waves:
            return []

        enemy_count = 1 + self.current_wave
        for i in range(enemy_count):
            x = (i % 10) * 60
            y = 50 + (i // 10) * 40
            enemy = Enemy(self.enemy_surface, x, y)
            enemy.wave_id = self.current_wave  # ← attribuer l’origine
            self.enemies.append(enemy)

        self.current_wave += 1
        self.virtual_time = 0.0
        return self.enemies

    def update(self, dt):
        self.virtual_time += dt
        self.virtual_time_total += dt
        for enemy in self.enemies:
            enemy.update()

    def is_wave_cleared(self):
        return self.virtual_time >= self.wave_time_limit or len(self.enemies) == 0

    def check_player_health(self, player):
        if player.health <= 0 and self.max_waves is None:
            self.max_waves = self.current_wave
