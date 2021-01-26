import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group


def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()  # Instantiates from the settings module where all game settings are stored
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make an alien
    alien = Alien(ai_settings, screen)

    # Make a group to store lasers in
    lasers = Group()

    # Make a group to store the alien fleet in
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # This is the main loop that runs the game.
    while True:
        # Watch for keyboard and mouse events and process accordingly
        gf.check_events(ai_settings, screen, ship, lasers)
        ship.update()
        gf.update_lasers(lasers)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, lasers)


run_game()
