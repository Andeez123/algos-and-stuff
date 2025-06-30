import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image abd get its rect
        self.image = pygame.image.load('alien_invasion game/images/starship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)