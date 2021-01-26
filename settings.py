class Settings:
    # A class to store all settings for Alien Invasion

    def __init__(self):
        # Initialize the game's settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Laser settings
        self.laser_speed_factor = 1
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (255, 0, 0)
        self.lasers_allowed = 3

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 means right, -1 means left
        self.fleet_direction = 1
        
