import pygame

class MobileController:
    def __init__(self):
        self.buttons = {
            "left": pygame.Rect(20, 560, 60, 60),
            "right": pygame.Rect(100, 560, 60, 60),
            "fire": pygame.Rect(400, 560, 60, 60)
        }
        self.active = {"left": False, "right": False, "fire": False}

    def handle_touch(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for name, rect in self.buttons.items():
                if rect.collidepoint(pos):
                    self.active[name] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for name in self.active:
                self.active[name] = False

    def is_left(self):
        return self.active["left"]

    def is_right(self):
        return self.active["right"]

    def is_fire(self):
        return self.active["fire"]

    def draw(self, screen):
        for name, rect in self.buttons.items():
            pygame.draw.rect(screen, (100, 100, 100), rect)
            label = pygame.font.SysFont("Arial", 20).render(name.upper(), True, (255, 255, 255))
            screen.blit(label, (rect.x + 5, rect.y + 15))
