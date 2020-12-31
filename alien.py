import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship



def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()  # Instantiates from the settings module where all game settings are stored
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store lasers in
    lasers = Group()

    # This is the main loop that runs the game.
    while True:
        # Watch for keyboard and mouse events and process accordingly
        gf.check_events(ai_settings, screen, ship, lasers)
        ship.update()
        lasers.update()
        gf.update_screen(ai_settings, screen, ship, lasers)


run_game()
