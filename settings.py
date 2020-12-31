class Settings:
    # A class to store all settings for Alien Invasion

    def __init__(self):
        # Initialize the game's settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Laser settings
        self.laser_speed_factor = 1
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (255, 0, 0)
        self.lasers_allowed = 3
