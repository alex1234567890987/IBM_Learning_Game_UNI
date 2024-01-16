import pygame
from os import walk
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))
print(sys.path)

from production.outside_world.code.settings import *
import time


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
        self.z = LAYERS["tree"]

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

        # collision
        self.hitbox = self.rect.copy().inflate(-60, -60)
        self.collision_sprites = collision_sprites
        self.interaction_sprites = interaction_sprites

        # overlay
        self.ai_banner_status = False
        self.blockchain_banner_status = False
        self.iot_banner_status = False
        self.ds_banner_status = False
        self.cs_banner_status = False
        self.cloud_banner_status = False
        self.stats_banner_status = False
        self.house_banner_status = False
        self.ladder_banner_status = False
        self.credits_banner_status = False
        self.title_status = False

        # mini-game / stats / house
        self.run_stats_status = False
        self.run_player_house_status = False
        self.run_cloud_status = False
        self.run_data_sci_status = False
        self.run_ai_status = False
        self.run_cyber_status = False
        self.run_credits_status = False
        self.run_iot_status = False

        # self.font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 24)
        # self.banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),6.7)

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

        if keys[pygame.K_x]:
            collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interaction_sprites, False)
            if collided_interaction_sprite:
                #print(collided_interaction_sprite)
                if collided_interaction_sprite[0].name == 'Blacksmith':   # stats man
                    self.animation_status = 'left_idle'
                    self.run_stats_status = True
                if collided_interaction_sprite[0].name == 'Cloud_House':
                    self.run_cloud_status = True

                if collided_interaction_sprite[0].name == 'AI_House':
                    self.run_ai_status = True

                if collided_interaction_sprite[0].name == 'CS_House':
                    self.run_cyber_status = True

                if collided_interaction_sprite[0].name == 'Player_House':
                    self.run_player_house_status = True
                if collided_interaction_sprite[0].name == 'DS_House':
                    self.run_data_sci_status = True
                if collided_interaction_sprite[0].name == 'Ladder1':
                    self.pos.x = 901
                    self.pos.y = 219
                    time.sleep(0.1)  # avoids error by allowing collided_interaction_sprite to update
                if collided_interaction_sprite[0].name == 'Ladder2':
                    self.pos.x = 663
                    self.pos.y = 374
                    time.sleep(0.1) # avoids error by allowing collided_interaction_sprite to update
                if collided_interaction_sprite[0].name == 'Credits':
                    self.run_credits_status = True
                if collided_interaction_sprite[0].name == 'IOT_House':
                    self.run_iot_status = True

        collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interaction_sprites, False)
        #print(collided_interaction_sprite)
        if collided_interaction_sprite:
            if collided_interaction_sprite[0].name == 'AI_House':
                self.ai_banner_status = True
            if collided_interaction_sprite[0].name == 'Blockchain_House':
                self.blockchain_banner_status = True
            if collided_interaction_sprite[0].name == 'IOT_House':
                self.iot_banner_status = True
            if collided_interaction_sprite[0].name == 'DS_House':
                self.ds_banner_status = True
            if collided_interaction_sprite[0].name == 'CS_House':
                self.cs_banner_status = True
            if collided_interaction_sprite[0].name == 'Cloud_House':
                self.cloud_banner_status = True
            if collided_interaction_sprite[0].name == 'Blacksmith':
                self.stats_banner_status = True
            if collided_interaction_sprite[0].name == 'Player_House':
                self.house_banner_status = True
            if collided_interaction_sprite[0].name == 'Ladder1' or collided_interaction_sprite[0].name == 'Ladder2':
                self.ladder_banner_status = True
            if collided_interaction_sprite[0].name == 'Credits':
                self.credits_banner_status = True
            if collided_interaction_sprite[0].name == 'Start_Zone':
                self.title_status = True
        else:
            self.ai_banner_status = False
            self.blockchain_banner_status = False
            self.iot_banner_status = False
            self.ds_banner_status = False
            self.cs_banner_status = False
            self.cloud_banner_status = False
            self.stats_banner_status = False
            self.house_banner_status = False
            self.ladder_banner_status = False
            self.credits_banner_status = False
            self.title_status = False
                #print(self.ai_banner_status)

    def check_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.animation_status = self.animation_status.split('_')[0] + '_idle'

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

    def move(self, dt):
        # normalisation
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

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
