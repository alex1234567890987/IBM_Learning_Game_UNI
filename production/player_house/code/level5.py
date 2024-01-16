import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

import pygame
from production.player_house.code.settings5 import *
from production.player_house.code.player5 import Player
from production.player_house.code.sprites5 import Generic, Chest, Interaction
from production.player_house.code import chest_screen
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self):
        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()
       
        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        tmx_data = load_pygame('player_house/data/tmx/player_house.tmx')
        self.player = Player((100,200), self.all_sprites, self.collision_sprites, self.interaction_sprites)
        
        # Generic(
        #     pos=(0, 0),
        #     surf=pygame.image.load("player_house/data/tmx/player_house.png").convert_alpha(),
        #     groups=self.all_sprites,
        #     z=LAYERS["Floor"],
        # )


        for x, y, surf in tmx_data.get_layer_by_name('Floor').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for x, y, surf in tmx_data.get_layer_by_name('Carpet').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        

        # layers that should not be traversed over / should force collision (decor, Border)
        for layer in ['Decor', 'Border']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])
        
        
        for x, y, surf in tmx_data.get_layer_by_name('Treasure chest').tiles():
            Chest((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites, self.interaction_sprites], 'Treasure chest')
            Interaction((x,y), (2,2), self.interaction_sprites, 'Treasure Chest')

        

    def run(self, dt):
        
        # self.display_surface.fill('black')
        self.all_sprites.layered_draw(self.player)
        self.all_sprites.update(dt)
        pygame.transform.scale(self.display_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        while self.player.chest_screen_status == True:
            print("Chest page")
            chest_screen.run()
            self.player.chest_screen_status = False



class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # zoom
        self.zoom_scale = 3.5
        self.internal_surf_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center=(self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

        self.banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4)
        self.big_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.15)
        self.biggest_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.3)
        self.smallest_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 14)
        self.small_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 15)
        self.medium_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 18)
        self.chest_text_surf = self.medium_font.render("Press X to Open your Achievements Chest", False, 'Black')

    def layered_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        self.internal_surf.fill('#262B44')

        for layer in LAYERS.values():
            if (layer != 3) and (layer != 4):
                for sprite in self.sprites():
                    if sprite.z == layer:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.internal_surf.blit(sprite.image, offset_rect)
            else:
                for sprite in sorted(self.sprites(), key = lambda sprite: (sprite.rect.centery + sprite.rect.h/1.5)):
                    # print(sprite.rect.centery)
                    if sprite.z == layer:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.internal_surf.blit(sprite.image, offset_rect)

        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))

        self.display_surface.blit(scaled_surf, scaled_rect)


        if player.chest_banner_status:
            self.display_surface.blit(self.biggest_banner_image, (1280*(1/2) - self.biggest_banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.chest_text_surf, (1280*(1/2) - self.chest_text_surf.get_width()/2, 720*(4/5)
                                                          + self.biggest_banner_image.get_height()/2 - 10))
