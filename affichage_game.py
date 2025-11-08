import pygame

class AffichageGame:
    def __init__(self, screen, assets, interface, controller):
        self.screen = screen
        self.assets = assets
        self.interface = interface
        self.controller = controller

    def draw_background(self):
        self.screen.fill((0, 0, 0))

    def draw_entities(self, player, enemies, bullets):
        self.screen.blit(self.assets["player"], player.rect)
        for enemy in enemies:
            self.screen.blit(self.assets["enemy"], enemy.rect)
        for bullet in bullets:
            self.screen.blit(self.assets["bullet"], bullet.rect)

    def draw_interface(self):
        self.interface.draw(self.screen)

    def draw_mobile_buttons(self):
        self.controller.draw_mobile_buttons(self.screen)

    def render_all(self, player, enemies, bullets):
        self.draw_background()
        self.draw_entities(player, enemies, bullets)
        self.draw_interface()
        self.draw_mobile_buttons()
        pygame.display.flip()
