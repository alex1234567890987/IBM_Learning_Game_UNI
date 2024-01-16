"""
this is a temporary file to run the cloud house

some of the file in cloud_house cannot be directly run because of path&import issue

so it is safe to execute from this file
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

import pygame
import cloud_house.minigame as mg
import cloud_house.cloud_house as ch

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Cloud house: Currently running directly from cloudhouse main')



ch.run()