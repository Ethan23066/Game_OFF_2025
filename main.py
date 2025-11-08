import pygame
from settings_game import WIDTH, HEIGHT
from game import Game
from menu_select_control import MenuSelectControl

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")

    # Menu de sélection du contrôleur
    menu = MenuSelectControl()
    control_mode = "keyboard"

    while menu.active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            result = menu.handle_input(event)
            if result:
                control_mode = result
        menu.draw(screen)

    # Lancement du jeu avec le contrôleur choisi
    game = Game(screen, control_mode=control_mode)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    run_game()