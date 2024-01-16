import statistics

import pygame
from pygame import mixer
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))
print(sys.path)
from production.general import statistics
from production.cloud_house import cloud_house
from production.player_house.code.main import Game
from production.ai_house_main import game
from production.datascience_house import Minigame
from production.cybersecurity_house import minigame_cyber
from production.general.credits import run_credits

#import production
from production.outside_world.code.settings import *
from production.outside_world.code.player import Player
from production.outside_world.code.sprites import Generic, Portal, Blacksmith, Wave, Fish, Tree, Interaction
from pytmx.util_pygame import load_pygame





def get_images_portal(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        image_surface_resized = pygame.transform.scale(image_surface, (75, 75))
        surfaces.append(image_surface_resized)

    return surfaces


def get_images(folder_dir):
    surfaces = []

    for filename in os.listdir(folder_dir):
        full_path = folder_dir + '/' + filename
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces.append(image_surface)

    return surfaces


class Level:
    def __init__(self):
        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()

        #self.banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),6.7)

        self.setup()

    def setup(self):
        # importing tmx file (tiled map)
        tmx_data = load_pygame('outside_world/data/tmx/outside_world.tmx')

        # importing static tiles
        # water
        for x, y, surf in tmx_data.get_layer_by_name('Water Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # ground
        for x, y, surf in tmx_data.get_layer_by_name('Ground Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # paths
        for x, y, surf in tmx_data.get_layer_by_name('Path Layer').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        #cliffs
        for x, y, surf in tmx_data.get_layer_by_name('Cliffs').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # layers that can be traversed over (grass, grass overlay, shrubs, flowers)
        for layer in ['Grass', 'Grass Overlay', 'Shrubs', 'Flowers', 'Water Rocks', 'Water Flora']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # layers that should not be traversed over / should force collision (bush, rocks)
        for layer in ['Bush', 'Rocks']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # ladder
        for x, y, surf in tmx_data.get_layer_by_name('Ladder').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # more layers that can be traversed over (stairs)
        for x, y, surf in tmx_data.get_layer_by_name('Stairs').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # more layers that can not be traversed over (environment, ground tree trucks)
        for layer in ['Environment', 'Ground Tree Trunks']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

        # house entrance
        for x, y, surf in tmx_data.get_layer_by_name('House Entrance').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for x, y, surf in tmx_data.get_layer_by_name('Frame').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # trees
        for obj in tmx_data.get_layer_by_name('Tree Objects'):
            Tree((obj.x, obj.y), obj.image, self.all_sprites, obj.name, LAYERS['tree'])

        # importing animated object tiles
        # blacksmith / stat man
        blacksmith_frames = get_images('assets/graphics/outside_world_graphics/Blacksmith')
        for obj in tmx_data.get_layer_by_name('Blacksmith'):
            Blacksmith((obj.x, obj.y), blacksmith_frames, [self.all_sprites, self.collision_sprites])

        # waves
        for obj in tmx_data.get_layer_by_name('Waves'):
            Wave((obj.x, obj.y), obj.name, self.all_sprites)

        # fish
        for obj in tmx_data.get_layer_by_name('Fish'):
            Fish((obj.x, obj.y), obj.name, self.all_sprites)

        # TODO Make animation smooth or replace portals
        # portals
        portal_frames = get_images_portal('assets/graphics/outside_world_graphics/Portal/animated')
        for obj in tmx_data.get_layer_by_name('Portal'):
            # obj_image = pygame.transform.scale(obj.image, (obj.width, obj.width))
            Portal((obj.x, obj.y), portal_frames, [self.all_sprites, self.collision_sprites])

        # player
        for obj in tmx_data.get_layer_by_name('Player'):
            if obj.name == 'Start':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.interaction_sprites)
            if obj.name == 'Blacksmith':
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Ladder1":
                Interaction((obj.x,obj.y), (obj.width,obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Ladder2":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "AI_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)#
            if obj.name == "Blockchain_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "IOT_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "DS_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "CS_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Cloud_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Player_House":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Credits":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)
            if obj.name == "Start_Zone":
                Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)

        # image of tiled map for testing
        '''Generic(
            pos=(0, 0),
            surf=pygame.image.load("../data/tmx/outside_world.png").convert_alpha(),
            groups=self.all_sprites,
            z=LAYERS["ground"],
        )'''

    def run(self, dt):
        self.display_surface.fill('black')
        #self.display_surface.blit(Generic.hitbox)
        self.all_sprites.layered_draw(self.player)
        self.all_sprites.update(dt)

        

        while self.player.run_stats_status == True:
            print("running stats page")
            statistics.run()  # stuck in loop
            self.player.run_stats_status = False  # only runs when exits the run loop

        while self.player.run_ai_status == True:
            #if self.player.run_ai_status == True:
                #mixer.music.load('ai_house\sounds\Sleepless-City-Synthwave-Retrowave-Music.mp3')
                #mixer.music.play(-1)
            print("running ai page")
            game.run()
            self.player.run_ai_status = False
            #if self.player.run_ai_status == False:
                #mixer.music.pause()
            

        while self.player.run_cloud_status == True:
            print("running cloud page")
            cloud_house.run()
            self.player.run_cloud_status = False

        while self.player.run_player_house_status == True:
            print("running house page")
            gamePlayerHouse = Game()
            gamePlayerHouse.run()
            self.player.run_player_house_status = False

        while self.player.run_data_sci_status == True:
            print("running data science house")
            self.display_surface.fill('black')
            Minigame.startGame()
            self.player.run_data_sci_status = False

        while self.player.run_cyber_status == True:
            print("running cybersec minigame")
            gameCyber = minigame_cyber.Game("cybersecurity")
            gameCyber.run()
            self.player.run_cyber_status = False

        while self.player.run_credits_status == True:
            print("running credit page")
            run_credits()
            self.player.run_credits_status = False

        while self.player.run_iot_status:
            print("running iot house")
            gameIOT = minigame_cyber.Game("blockchain")
            gameIOT.run()
            self.player.run_iot_status = False




        '''while self.player.run_blockchain_status == True:
            blockchain_house.run()
            self.player.run_blockchain_status'''


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # zoom
        self.zoom_scale = 2.5
        self.internal_surf_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center=(self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

        #self.bg_surf = pygame.image.load('graphics/art/bg_1.png')
        #self.bg_surf_sized = pygame.transform.scale(self.bg_surf, (1280, 720))

        self.title_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_4x3.png'),5)
        self.banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4)
        self.big_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.15)
        self.biggest_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.3)
        self.smallest_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 14)
        self.small_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 15)
        self.medium_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 18)
        self.large_font = pygame.font.Font('graphics/font/PeaberryBase.ttf', 32)

        self.ai_text_surf = self.medium_font.render("This is the AI Mini-Game, Press X to Play", False, 'Black')
        self.blockchain_text_surf = self.small_font.render("This is the Blockchain Mini-Game, Press X to Play",
                                                            False, 'Black')
        self.iot_text_surf = self.medium_font.render("This is the I.O.T Mini-Game, Press X to Play", False, 'Black')
        self.ds_text_surf = self.small_font.render("This is the Data Science Mini-Game, Press X to Play", False, 'Black')
        self.cs_text_surf = self.small_font.render("This is the Cybersecurity Mini-Game, Press X to Play", False, 'Black')
        self.cloud_text_surf = self.medium_font.render("This is the Cloud Mini-Game, Press X to Play", False, 'Black')
        self.stats_text_surf = self.medium_font.render("View Stats Here, Press X", False, 'Black')
        self.house_text_surf = self.medium_font.render("Enter Home Here, Press X", False, 'Black')
        self.ladder_text_surf = self.medium_font.render("Enter Ladder to other Island, Press X", False, 'Black')
        self.credits_text_surf = self.medium_font.render("View Credits, Press X", False, 'Black')

        self.title_text_surf = self.large_font.render("Welcome to IBM Village", False, 'Black')

    def layered_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        self.internal_surf.fill('#262B44')
        # self.internal_surf.blit(self.bg_surf_sized, (0,0))

        for layer in LAYERS.values():
            if (layer != 8) and (layer != 9):
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

        '''if player.title_status:
            self.display_surface.blit(self.big_banner_image, (1280*(1/2) - self.big_banner_image.get_width()/2, 720*(4/5) - self.big_banner_image.get_height()/2))
            self.display_surface.blit(self.title_text_surf, (self.display_surface.get_width()/2 - self.title_text_surf.get_width()/2, 720*(4/5) - self.title_text_surf.get_height()/2))'''

        if player.ai_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.ai_text_surf, (1280*(1/2) - self.ai_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))
        if player.blockchain_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.blockchain_text_surf, (1280*(1/2) - self.blockchain_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))

        if player.iot_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.iot_text_surf, (1280*(1/2) - self.iot_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))

        if player.ds_banner_status:
            self.display_surface.blit(self.big_banner_image, (1280*(1/2) - self.big_banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.ds_text_surf, (1280*(1/2) - self.ds_text_surf.get_width()/2, 720*(4/5)
                                                          + self.big_banner_image.get_height()/2 - 10))

        if player.cs_banner_status:
            self.display_surface.blit(self.biggest_banner_image, (1280*(1/2) - self.biggest_banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.cs_text_surf, (1280*(1/2) - self.cs_text_surf.get_width()/2, 720*(4/5)
                                                          + self.biggest_banner_image.get_height()/2 - 10))

        if player.cloud_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.cloud_text_surf, (1280*(1/2) - self.cloud_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))
        if player.stats_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.stats_text_surf, (1280*(1/2) - self.stats_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))

        if player.house_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.house_text_surf, (1280*(1/2) - self.house_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))

        if player.ladder_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.ladder_text_surf, (1280*(1/2) - self.ladder_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))

        if player.credits_banner_status:
            self.display_surface.blit(self.banner_image, (1280*(1/2) - self.banner_image.get_width()/2, 720*(4/5)))
            self.display_surface.blit(self.credits_text_surf, (1280*(1/2) - self.credits_text_surf.get_width()/2, 720*(4/5)
                                                          + self.banner_image.get_height()/2 - 10))



