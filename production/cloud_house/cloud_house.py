"""
AI Group Project Team 7 Spring22/23

Desc: This module control and display the minigame of the cloud house.
It imports level_builder so it can display the the minigame level 

Created by: Muhammad Kamaludin
Modified by:
Last modified: 18/5/2023
"""

import pygame
from production.cloud_house import minigame, border, player
import production.general.db.DatabaseService as DB
from sys import exit

ZOOM_SCALE = 2.5

def setup():
    """
    Declare essential variables and objects
    """

    global screen, clock, bg, bg_rect, bg_inc, bg_counter, house_surf, house_rect
    global npcs_surf, npcs_rect
    global player_sprite, player_feet_rect, player_stats
    global text_banner_surf, text_banner_rect, display_text_banner
    global walkable_area_border # an object of Border
    global key_hold, key_hold_counter
    global all_text_messages, displayed_text_messages
    FONT = pygame.font.Font('graphics/font/PeaberryBase.ttf', 17)
    
    #pygame essential objects
    screen = pygame.display.get_surface()
    screen.fill((25,36,40))
    clock = pygame.time.Clock()

    #background
    bg = pygame.transform.scale_by(pygame.image.load("cloud_house/assets/bg_sky.png"),ZOOM_SCALE*2)
    bg_rect = bg.get_rect(center=screen.get_rect().center)
    bg_inc = 1 #the changes of x coordinate every frame (for animation)
    bg_counter = 0

    #house and the map
    house_surf = pygame.transform.scale_by(pygame.image.load("cloud_house/assets/base.png"),ZOOM_SCALE) 
    house_rect = house_surf.get_rect(center=screen.get_rect().center)
    
    points = [(592,526),(592,458),(612,458),(612,334),(508,334),(508,206),(550,206),(550,186),
              (766,186),(766,228),(800,228),(800,334),(668,334),(668,458),(720,458),(720,526),
              (592,526)]
    
    walkable_area_border = border.Border(points)    

    #player
    player_sprite = player.Player()
    player_sprite.rect.center = (640,508-25)
    player_feet_rect = pygame.Rect((0,0),(20,20))
    player_feet_rect.midbottom = (640,508)
    player_stats = DB.get_user()
    
    #npc
    npcs_surf = [pygame.transform.scale_by(pygame.image.load(f"cloud_house/assets/npc_{i+1}.png"), 0.9) for i in range(3)]
    npcs_rect = [ npcs_surf[i].get_rect(midbottom=coord)for i, coord in enumerate([(640,208), (502,249), (796,296)])]

    #Text banner
    text_banner_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4)
    text_banner_rect = text_banner_surf.get_rect(topleft=((1280*(1/2) - text_banner_surf.get_size()[0]/2, 720*(4/5))))
    display_text_banner = False

    temp_txt = ["Hey buddy, come try this minigame :D", "Wow you got potential! Try the medium one",
            "Come beat this 'Boss' level" , "You need more experience to beat this level", "Welcome to the Cloud House!",
            "Hold [F] to play", "Go explore and interact with the NPC :D"]

    all_text_messages = [ FONT.render(txt, False, 'Black') for txt in temp_txt]
    displayed_text_messages = [None,None] #some text banner requires 2 lines of text

    key_hold, key_hold_counter = False, 0

def animate_bg():
    """
    Make the background move left and right
    """
    global bg_rect, bg_inc, bg_counter
    bg_counter += 1
    bg_inc = -1 if bg_rect.left == 0 else bg_inc
    bg_inc = 1 if bg_rect.right == screen.get_width() else bg_inc

    if not bg_counter % 2: bg_rect.left += bg_inc

def display_level_page():
    """
    Blit everything
    """
    global display_text_banner, displayed_text_messages

    #the bg and map
    animate_bg()
    screen.blit(bg,bg_rect)
    screen.blit(house_surf, house_rect)

    #npcs
    for i in range(3):
        screen.blit(npcs_surf[i], npcs_rect[i])

    #for coord1, coord2 in walkable_area_border.edges:
    #    pygame.draw.line(screen, "Black", coord1, coord2) <--uncomment to see walkable area

    #pygame.draw.rect(screen,"Black",player_feet_rect) <-player hitbox

    #animate the player every 1 second, and blit the player

    player_sprite.animate()
    screen.blit(player_sprite.image, player_sprite.rect)
    
    #text banner overlay
    if display_text_banner: 
        screen.blit(text_banner_surf,text_banner_rect)
        display_text_banner = False

        #first line
        line_1_rect = displayed_text_messages[0].get_rect(center=text_banner_rect.center)
        screen.blit(displayed_text_messages[0], line_1_rect)

        #2nd line
        if displayed_text_messages[1]:
            line_2_rect = displayed_text_messages[1].get_rect(center=line_1_rect.center)
            line_2_rect.y += 18
            screen.blit(displayed_text_messages[1], line_2_rect)
    

def check_player_movement():
    """
    player can navigate using wasd or arrow keys inside the specified walkable area, the player will also stop if it hit any npc
    """
    keys = pygame.key.get_pressed()

    is_idle = True
    #update player rect if the condition are met
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and not (walkable_area_border.is_colliding(player_feet_rect.midtop) or any([ npc.collidepoint(player_feet_rect.midtop) for npc in npcs_rect])):
        player_sprite.animation_status = "backward"
        player_sprite.rect.y -= player_sprite.speed
        player_feet_rect.y -= player_sprite.speed
        is_idle = False
    
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not (walkable_area_border.is_colliding(player_feet_rect.midbottom) or any([ npc.collidepoint(player_feet_rect.midbottom) for npc in npcs_rect])):
        player_sprite.animation_status = "forward"
        player_sprite.rect.y += player_sprite.speed
        player_feet_rect.y += player_sprite.speed
        is_idle = False

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not (walkable_area_border.is_colliding(player_feet_rect.midleft) or any([ npc.collidepoint(player_feet_rect.midleft) for npc in npcs_rect])):
        player_sprite.animation_status = "left"
        player_sprite.rect.x -= player_sprite.speed
        player_feet_rect.x -= player_sprite.speed
        is_idle = False

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not (walkable_area_border.is_colliding(player_feet_rect.midright) or any([ npc.collidepoint(player_feet_rect.midright) for npc in npcs_rect])):
        player_sprite.animation_status = "right"
        player_sprite.rect.x += player_sprite.speed
        player_feet_rect.x += player_sprite.speed
        is_idle = False
    
    if is_idle:
        player_sprite.animation_status = player_sprite.animation_status.split('_')[0] + '_idle'

def check_npc_interaction():
    """
    This function controls the interaction of player with the minigame access point

    There is an internal function that is used to check player holding a key for certain period of time
    """
    
    def hold_f_to_enter(difficulty: int = 0):
        """
        This detects player holding f for until counter hits 100.
        The counter resets if the key is released or after it reaches 100
        """
        global key_hold, key_hold_counter

        if not pygame.key.get_pressed()[pygame.K_f]: return
        
        if key_hold:
            key_hold_counter += 1

            if key_hold_counter == 50:
                print("successfully hold")
                key_hold_counter = 0
                minigame.run(difficulty, player_stats)

        else:
            key_hold = True
            key_hold_counter = 0

    global display_text_banner, displayed_text_messages, all_text_messages
    any_collision = False

    #Upon collision, it shows instruction to access the game and handle all necessary input
    for i, npc_rect, exp_threshold in zip([0,1,2],npcs_rect,[0,100,200]):
        
        if player_stats.exp_cloud >= exp_threshold and player_feet_rect.colliderect(npc_rect):
            
            displayed_text_messages[0] = all_text_messages[i]
            displayed_text_messages[1] = all_text_messages[5]
            any_collision = True
            hold_f_to_enter( i + 1)

        if player_stats.exp_cloud < exp_threshold and player_feet_rect.colliderect(npc_rect):
            displayed_text_messages[0] = all_text_messages[3]
            displayed_text_messages[1] = None
            any_collision = True

    display_text_banner = any_collision

def check_sign_interaction():
    
    global display_text_banner, all_text_messages, displayed_text_messages
    if border.Border([(720,458),(720,526)]).is_colliding(player_feet_rect.midright):
        display_text_banner = True
        displayed_text_messages[0] = all_text_messages[4]
        displayed_text_messages[1] = all_text_messages[len(all_text_messages)-1]

def run():
    """
    The cloud house entry point and it controls all stuff
    """

    global key_hold
    loop = True
    setup()

    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                key_hold = False

            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                loop = False

        check_player_movement()
        check_npc_interaction()
        check_sign_interaction()
        display_level_page()

        pygame.display.update()
        clock.tick()

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Cloud house: Currently running directly from cloud_house.py')
    run()