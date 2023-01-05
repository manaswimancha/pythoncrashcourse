import pygame

class GameCharacter:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load("alien_invasion/images/download.bmp"),(50,75))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)