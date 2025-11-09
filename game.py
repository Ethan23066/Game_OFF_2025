import pygame
from settings_game import FPS
from select_control import select_control
from interface_game import Interface
from menu_game import Menu
from player import Player
from wave_manager import WaveManager
from hud import HUD

class Game:
    def __init__(self, screen, control_mode="keyboard"):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.controller = select_control(control_mode)
        self.interface = Interface()
        self.menu = Menu()

        self.player = Player(pygame.Surface((40, 30)))
        self.player.image.fill((0, 255, 0))

        self.enemy_surface = pygame.Surface((40, 30))
        self.enemy_surface.fill((255, 0, 0))
        self.wave_manager = WaveManager(self.enemy_surface)
        self.wave_manager.spawn_wave()

        self.bullets = pygame.sprite.Group()
        self.hud = HUD(self.player)

        self.bg_offset = 0
        self.bg_speed = 30  # pixels/sec

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.menu.active:
                    self.menu.handle_input(event)
                elif hasattr(self.controller, "handle_touch"):
                    self.controller.handle_touch(event)

            if self.menu.active:
                self.menu.draw(self.screen)
            else:
                if not self.interface.game_over:
                    self.update(dt)
                self.render()

        pygame.quit()

    def update(self, dt):
        self.bg_offset += self.bg_speed * dt
        if self.bg_offset >= self.screen.get_height():
            self.bg_offset = 0

        self.controller.update()

        if self.player:
            self.player.regen_stamina(dt)
            if self.controller.is_left(): self.player.move_left()
            if self.controller.is_right(): self.player.move_right()
            if hasattr(self.controller, "is_fire") and self.controller.is_fire():
                bullet = self.player.fire()
                if bullet: self.bullets.add(bullet)

        self.wave_manager.update(dt)
        self.bullets.update(dt)

        for bullet in self.bullets.copy():
            for enemy in self.wave_manager.enemies.copy():
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.wave_manager.enemies.remove(enemy)
                    self.interface.add_kill()
                    break

        if self.player:
            for enemy in self.wave_manager.enemies:
                if enemy.rect.colliderect(self.player.rect):
                    self.player.health = 0
                    break

            self.wave_manager.check_player_health(self.player)

        if self.wave_manager.is_wave_cleared():
            self.wave_manager.spawn_wave()

        if self.wave_manager.max_waves is not None and self.wave_manager.current_wave >= self.wave_manager.max_waves:
            self.interface.set_game_over(self.wave_manager, self.player)
            self.wave_manager.enemies.clear()
            self.bullets.empty()
            self.player = None

    def render(self):
        self.screen.fill((0, 0, 0))

        for y in range(-self.screen.get_height(), self.screen.get_height(), 40):
            rect = pygame.Rect(0, y + int(self.bg_offset), self.screen.get_width(), 20)
            pygame.draw.rect(self.screen, (10, 10, 10), rect)

        if self.player:
            self.screen.blit(self.player.image, self.player.rect)

        for enemy in self.wave_manager.enemies:
            self.screen.blit(enemy.image, enemy.rect)

        self.bullets.draw(self.screen)
        self.hud.draw(self.screen)
        self.interface.draw(self.screen)

        if hasattr(self.controller, "draw_mobile_buttons"):
            self.controller.draw_mobile_buttons(self.screen)

        pygame.display.flip()
