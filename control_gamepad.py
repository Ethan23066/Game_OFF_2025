import pygame

class GamepadController:
    def __init__(self):
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def update(self):
        # Rien à faire ici, les événements sont gérés dans la boucle
        pass

    def is_left(self):
        return self.joystick and self.joystick.get_axis(0) < -0.5

    def is_right(self):
        return self.joystick and self.joystick.get_axis(0) > 0.5

    def is_fire(self):
        return self.joystick and self.joystick.get_button(0)  # bouton A

    def is_enter(self):
        return self.joystick and self.joystick.get_button(7)  # bouton Start

    def is_escape(self):
        return self.joystick and self.joystick.get_button(6)  # bouton Back
