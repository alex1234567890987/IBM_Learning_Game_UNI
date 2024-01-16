import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame
from os import walk
import os
from production.player_house.code.ph_settings import *


def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces.append(image_surface)

    return surfaces


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, interaction_sprites):
        super().__init__(group)

        # animation setup
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
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS["Decor"]

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

        # collision
        self.hitbox = self.rect.copy().inflate(-60, -60)
        self.collision_sprites = collision_sprites
        self.interaction_sprites = interaction_sprites

        # overlay
        self.chest_banner_status = False

        #chest screen
        self.chest_screen_status = False

    def animate(self, dt):
        self.frame_index += 6 * dt

        if self.frame_index >= len(self.animations[self.animation_status]):
            self.frame_index = 0

        self.image = self.animations[self.animation_status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.animation_status = "backward"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.animation_status = "forward"
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.animation_status = "right"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.animation_status = "left"
        else:
            self.direction.x = 0


        if self.chest_banner_status == True and keys[pygame.K_x] == True:
            self.chest_screen_status = True
        
        collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interaction_sprites, False)
        print(collided_interaction_sprite)
       
        if collided_interaction_sprite:
            if collided_interaction_sprite[0].name == 'Treasure chest':
                self.chest_banner_status = True
        else:
                self.chest_banner_status = False


    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:  # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:  # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0:  # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:  # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery


        


    def check_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.animation_status = self.animation_status.split('_')[0] + '_idle'

    def move(self, dt):
        # normalisation
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # hor movement
         # hor movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx  # change to hitbox
        self.collision('horizontal')

        # ver movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def update(self, dt):
        self.input()
        self.check_status()

        self.move(dt)
        self.animate(dt)
    

    
            
    