import pygame
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))
print(sys.path)
from production.outside_world.code.settings import *

def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces.append(image_surface)

    return surfaces


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy()


class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.name = name


class Tree(Generic):
    def __init__(self, pos, surf, groups, name, z=LAYERS['tree']):
        super().__init__(pos, surf, groups, z)


class Blacksmith(Generic):
    def __init__(self, pos, frames, groups):
        # animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
            z=LAYERS['blacksmith'])

        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)

    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class Wave(Generic):
    def __init__(self, pos, name, groups):
        self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/small-waves')
        # animation setup
        if name == "small":
            self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/small-waves')
        elif name == "med":
            self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/med-waves')
        elif name == "big":
            self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/big-waves')

        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
            z=LAYERS['water ambience'])

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class Fish(Generic):
    def __init__(self, pos, name, groups):
        self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/small-fish')
        # animation setup
        if name == "small":
            self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/small-fish')
        elif name == "big":
            self.frames = get_images('assets/graphics/outside_world_graphics/Water Ambience Split/big-fish')

        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
            z=LAYERS['water ambience'])

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class Portal(Generic):
    def __init__(self, pos, frames, groups):
        # animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
            z=LAYERS['tree'])

        self.hitbox = self.rect.copy().inflate(-self.rect.width, -self.rect.height * 0.9)

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class PortalTimed(Generic):
    def __init__(self, pos, frames, groups, animation_time=0.125):
        # animation setup
        self.frames = frames
        self.frame_index = 0
        self.animation_time = animation_time
        self.animation_timer = 0

        # sprite setup
        super().__init__(
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
            z=LAYERS['portal'])

    def animate(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_time:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

    def update(self, dt):
        self.animate(dt)
