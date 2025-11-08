import pygame

class KeyboardController:
    def __init__(self):
        self.keys = pygame.key.get_pressed()

    def update(self):
        self.keys = pygame.key.get_pressed()

    def is_left(self):
        return self.keys[pygame.K_LEFT]

    def is_right(self):
        return self.keys[pygame.K_RIGHT]

    def is_space(self):
        return self.keys[pygame.K_SPACE]

    def is_enter(self):
        return self.keys[pygame.K_RETURN]

    def is_escape(self):
        return self.keys[pygame.K_ESCAPE]
