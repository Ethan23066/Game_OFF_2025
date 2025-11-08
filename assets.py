import pygame
import os

# Chemins relatifs
SPRITE_DIR = "assets/"

def load_sprite(name):
    path = os.path.join(SPRITE_DIR, name)
    return pygame.image.load(path).convert_alpha()

# Exemple d’usage
bullet_sprite = load_sprite("pixl-frame-0.png")
