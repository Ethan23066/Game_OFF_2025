import pygame
import os

SPRITE_DIR = "assets"


def load_sprite(name):
    path = os.path.join(SPRITE_DIR, name)
    return pygame.image.load(path).convert_alpha()

