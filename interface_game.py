import pygame

class Interface:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 32)
        self.reset()

    def reset(self):
        self.game_over = False
        self.waves_survived = 0
        self.enemies_killed = 0
        self.total_enemies_last_wave = 0
        self.remaining_enemies_at_death = 0
        self.stamina_used = 0
        self.total_time_survived = 0.0

    def set_game_over(self, wave_manager, player):
        self.game_over = True
        self.waves_survived = wave_manager.current_wave

        last_wave_id = wave_manager.current_wave - 1
        self.total_enemies_last_wave = sum(1 for e in wave_manager.enemies if e.wave_id == last_wave_id)
        self.remaining_enemies_at_death = sum(1 for e in wave_manager.enemies if e.wave_id == last_wave_id)

        self.total_time_survived = wave_manager.virtual_time_total
        self.stamina_used = player.stamina_spent

    def add_kill(self):
        self.enemies_killed += 1

    def draw(self, screen):
        if self.game_over:
            y = screen.get_height() // 2 - 100
            lines = [
                "GAME OVER",
                f"Waves survived: {self.waves_survived}",
                f"Enemies killed: {self.enemies_killed}",
                f"Remaining enemies: {self.remaining_enemies_at_death}",
                f"Stamina used: {int(self.stamina_used)}",
                f"Time survived: {int(self.total_time_survived)}s"
            ]
            for line in lines:
                text = self.font.render(line, True, (255, 0, 0))
                screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, y))
                y += 40
