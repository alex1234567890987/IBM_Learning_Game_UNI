
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

import pygame 

from production.ai_house.code.main2 import Game 


pygame.init()



game = Game()

# game.run()