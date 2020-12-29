import sys
import pygame

def check_events(ship):
    # This function listens for and responds to keypresses and mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right one space
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    # This function updates images on the screen and flips to the new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()