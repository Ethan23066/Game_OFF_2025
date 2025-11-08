import pygame
from settings_game import FPS
from select_control import select_control
from interface_game import Interface
from menu_game import Menu
from player import Player
from ennemy import Enemy

class Game:
    def __init__(self, screen, control_mode="keyboard"):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.controller = select_control(control_mode)
        self.interface = Interface()
        self.menu = Menu()

        self.player = Player(pygame.Surface((40, 30)))
        self.player.image.fill((0, 255, 0))

        self.enemies = []
        for x in range(10):
            enemy_surface = pygame.Surface((40, 30))
            enemy_surface.fill((255, 0, 0))
            self.enemies.append(Enemy(enemy_surface, x * 60, 50))

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
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

            self.update()
            self.render()

        pygame.quit()

    def update(self):
        self.controller.update()

        if self.controller.is_left():
            self.player.move_left()
        if self.controller.is_right():
            self.player.move_right()

        for enemy in self.enemies:
            enemy.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        for enemy in self.enemies:
            self.screen.blit(enemy.image, enemy.rect)
        self.interface.draw(self.screen)

        # Appel conditionnel pour éviter l'erreur
        if hasattr(self.controller, "draw_mobile_buttons"):
            self.controller.draw_mobile_buttons(self.screen)

        pygame.display.flip()
