import sys
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while(True):
            self._check_events()
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

if __name__=="__main__":
    ai = AlienInvasion()
    ai.run_game()