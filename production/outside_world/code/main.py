import pygame, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))
print(sys.path)

from production.outside_world.code.settings import *
from production.outside_world.code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('IBM Village')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.loop = True

    def run(self):
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.loop = False


            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
