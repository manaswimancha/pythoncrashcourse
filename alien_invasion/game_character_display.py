import sys
import pygame
from game_character import GameCharacter

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (255,255,255)
        self.game_character = GameCharacter(self)

    def run_game(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.game_character.blitme()
            pygame.display.flip()

if __name__=="__main__":
    ai = AlienInvasion()
    ai.run_game()