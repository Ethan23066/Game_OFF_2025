from control_keyboard import KeyboardController
from control_gamepad import GamepadController
from control_mobile import MobileController

def select_control(mode="keyboard"):
    if mode == "keyboard":
        return KeyboardController()
    elif mode == "gamepad":
        return GamepadController()
    elif mode == "mobile":
        return MobileController()
    else:
        raise ValueError(f"Unknown control mode: {mode}")
