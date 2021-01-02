import sys
import pygame
from laser import Laser


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


def update_screen(ai_settings, screen, ship, alien, lasers):
    # This function updates images on the screen and flips to the new screen
    screen.fill(ai_settings.bg_color)

    # Redraw all lasers behind the ship and aliens
    for laser in lasers.sprites():
        laser.draw_laser()

    ship.blitme()
    alien.blitme()
    pygame.display.flip()


def update_lasers(lasers):
    # This function updates positions of lasers and gets rid of old lasers that are off the screen
    # Update laser position
    lasers.update()

    # Get rid of lasers that have disappeared from the screen.
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)

