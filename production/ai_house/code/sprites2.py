import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame
from production.ai_house.code.settings2 import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['Main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy()



# class Decor(Generic):
#     def __init__(self, pos, surf, groups, name, z=LAYERS['Decor']):
#         super().__init__(pos, surf, groups, z)

class NPC(Generic):
    def __init__(self, pos, surf, groups, name, z=LAYERS['NPC']):
        super().__init__(pos, surf, groups, z)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy()
        self.name = name

class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.name = name


