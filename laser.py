import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    # A class to manage lasers fired from the ship
    def __init__(self, ai_settings, screen, ship):
        # Create a laser object at the ship's current position
        super(Laser, self).__init__()
        self.screen = screen

        # Create a laser rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.laser_width, ai_settings.laser_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the laser's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.laser_color
        self.speed_factor = ai_settings.laser_speed_factor

    def update(self):
        # Move the laser up the screen
        self.y -= self.speed_factor

        # Update the rect position
        self.rect.y = self.y

    def draw_laser(self):
        # Draw the laser to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
