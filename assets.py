import pygame
import os

SPRITE_DIR = "assets"
_sprite_cache = {}

def load_sprite(name):
    """
    Charge un sprite PNG généré depuis assets/, avec cache.
    """
    if name in _sprite_cache:
        return _sprite_cache[name]

    path = os.path.join(SPRITE_DIR, name)
    sprite = pygame.image.load(path).convert_alpha()
    _sprite_cache[name] = sprite
    return sprite
