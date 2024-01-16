import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame, sys
#from settings5 import *
from production.player_house.code.ph_level import Level
from production.player_house.code.ph_settings import *


class Game:
    def __init__(self):
        #pygame.init()
        self.screen = pygame.display.get_surface()

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
