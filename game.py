import pygame
from settings_game import FPS
from select_control import select_control
from interface_game import Interface
from menu_game import Menu
from player import Player
from wave_manager import WaveManager

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
                continue

            self.update(dt)
            self.render()

        pygame.quit()

    def update(self, dt):
        self.controller.update()

        if self.controller.is_left():
            self.player.move_left()
        if self.controller.is_right():
            self.player.move_right()
        if hasattr(self.controller, "is_fire") and self.controller.is_fire():
            bullet = self.player.fire()
            if bullet:
                self.bullets.add(bullet)

        self.wave_manager.update()
        self.bullets.update(dt)

        # Collision bullet-enemy
        for bullet in self.bullets.copy():
            for enemy in self.wave_manager.enemies.copy():
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.wave_manager.enemies.remove(enemy)
                    break

        # Collision enemy-player
        for enemy in self.wave_manager.enemies:
            if enemy.rect.colliderect(self.player.rect):
                print("Collision joueur-ennemi")
                self.player.rect.midbottom = (-100, -100)
                break

        # Nouvelle vague si tous les ennemis sont détruits
        if self.wave_manager.is_wave_cleared():
            self.wave_manager.spawn_wave()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.image, self.player.rect)

        for enemy in self.wave_manager.enemies:
            self.screen.blit(enemy.image, enemy.rect)

        self.bullets.draw(self.screen)
        self.interface.draw(self.screen)

        if hasattr(self.controller, "draw_mobile_buttons"):
            self.controller.draw_mobile_buttons(self.screen)

        pygame.display.flip()
