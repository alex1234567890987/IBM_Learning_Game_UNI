import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame, sys
from production.ai_house.code.level2 import Level
# from production.ai_house.code.intro import intro_level
from production.ai_house.code.settings2 import *


class Game:
    def __init__(self):
        #pygame.init()
        self.screen = pygame.display.get_surface()

        #pygame.display.set_caption('Player Room')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        i=0
        loop = True
        while loop:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    loop = False

            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
