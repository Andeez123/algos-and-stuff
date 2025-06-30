import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        
        self.ship = Ship(self)

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen for each iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()