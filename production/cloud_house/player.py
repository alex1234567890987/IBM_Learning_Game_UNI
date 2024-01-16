import pygame, os
import random
def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(),2.5)
        surfaces.append(image_surface)

    return surfaces

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.speed = 2
        self.animation_status = "forward_idle"
        self.frame_index = 0

        self.animations = {'forward_idle': get_images('assets/graphics/player-animations/forward/idle'),
                           'forward': get_images('assets/graphics/player-animations/forward/movement'),
                           'right_idle': get_images('assets/graphics/player-animations/right/idle'),
                           'right': get_images('assets/graphics/player-animations/right/movement'),
                           'left_idle': get_images('assets/graphics/player-animations/left/idle'),
                           'left': get_images('assets/graphics/player-animations/left/movement'),
                           'backward_idle': get_images(
                               'assets/graphics/player-animations/backward/idle'),
                           'backward': get_images(
                               'assets/graphics/player-animations/backward/movement')}

        # image setup
        self.image = self.animations[self.animation_status][self.frame_index]
        self.rect = self.image.get_rect()

    def animate(self):
        self.frame_index += 0.1

        if self.frame_index >= len(self.animations[self.animation_status]): self.frame_index = 0

        self.image = self.animations[self.animation_status][int(self.frame_index)]

    def update(self):
        self.animate()
