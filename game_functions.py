import sys
import pygame
from laser import Laser
from alien import Alien


def create_fleet(ai_settings, screen, aliens):
    # Create a full fleet of aliens
    # Create and alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def check_events(ai_settings, screen, ship, lasers):
    # This function listens for and responds to keypresses and mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, lasers)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, lasers):
    # Responds to keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_laser(ai_settings, screen, ship, lasers)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_laser(ai_settings, screen, ship, lasers):
    # Fire laser if limit is not reached
    # Create a new laser and add it to the lasers group
    if len(lasers) < ai_settings.lasers_allowed:
        new_laser = Laser(ai_settings, screen, ship)
        lasers.add(new_laser)


def check_keyup_events(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, lasers):
    # This function updates images on the screen and flips to the new screen
    screen.fill(ai_settings.bg_color)

    # Redraw all lasers behind the ship and aliens
    for laser in lasers.sprites():
        laser.draw_laser()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_lasers(lasers):
    # This function updates positions of lasers and gets rid of old lasers that are off the screen
    # Update laser position
    lasers.update()

    # Get rid of lasers that have disappeared from the screen.
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)

