import pygame

class GamepadController:
    def __init__(self):
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def update(self):
        pass

    def is_left(self):
        return (
            self.joystick
            and self.joystick.get_numaxes() > 0
            and self.joystick.get_axis(0) < -0.5
        )

    def is_right(self):
        return (
            self.joystick
            and self.joystick.get_numaxes() > 0
            and self.joystick.get_axis(0) > 0.5
        )

    def is_fire(self):
        return (
            self.joystick
            and self.joystick.get_numbuttons() > 0
            and self.joystick.get_button(0)
        )

    def is_enter(self):
        return (
            self.joystick
            and self.joystick.get_numbuttons() > 7
            and self.joystick.get_button(7)
        )

    def is_escape(self):
        return (
            self.joystick
            and self.joystick.get_numbuttons() > 6
            and self.joystick.get_button(6)
        )

    def draw_mobile_buttons(self, screen):
        pass
