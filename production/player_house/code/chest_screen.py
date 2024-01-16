import pygame
from typing import Optional
from production.general.db import DatabaseService as DB
# from pygame_menu.widgets import ScrollBar
# import pygame_menu



pygame.init()

page_title = "Achievements"
clock = pygame.time.Clock()
#graphis object
FONT_PATH = 'graphics/font/PeaberryBase.ttf'
large_font = pygame.font.Font(FONT_PATH, 48)
medium_font = pygame.font.Font(FONT_PATH, 20)
small_font = pygame.font.Font(FONT_PATH, 15)
screen = None
bg_surf, bg_rect = None, None
statsblocks_wrapper_surf, statsblocks_wrapper_rect = None, None
title_surf, title_rect = None, None
title_bg_surf, title_bg_rect = None, None
button_surf, button_rect = None, None
exp_bg_surf, exp_bg_rect = None, None
exp_surfs, exp_rects = [None,None], [None, None]
biggest_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.3)
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
PADDING = 150

class Achievement(pygame.sprite.Sprite):

    """
    This text block is a wrapper consists of three types text surfaces.
    This is used for example to handle the display of data like 
    
    'Achievemnt name              <-- Header
    
     Achievement explanation               Trophy picture

    """
    #initial parameters
    def __init__(self, name: str, explanation: str, explanation2: str, pos: tuple, locked: bool):
        temp_path =  'graphics/art/UI/beige_rectangle_5x2.png'
        self.image = pygame.transform.scale_by(pygame.image.load(temp_path),(6.5,4.3))
        self.rect = self.image.get_rect()
        self.explan = explanation
        self.explan2 = explanation2
        self.trophy = pygame.image.load('assets/graphics/player_house_graphics/trophy.png') 
        self.lock = pygame.image.load('assets/graphics/player_house_graphics/lock.png') 
        self.name_text_surf = medium_font.render(name, False, 'Black')
        self.explan_text_surf = small_font.render(explanation, False, 'Black')
        self.explan2_text_surf = small_font.render(explanation2, False, 'Black')

        self.pos = pos
        self.locked = locked
        

    #blit all surfaces
    def display(self):
        screen.blit(self.image, self.pos)
        screen.blit(self.name_text_surf, (self.pos[0]+25, self.pos[1]+ 10))
        screen.blit(self.explan_text_surf, (self.pos[0]+25, self.pos[1]+ 40))
        screen.blit(self.explan2_text_surf, (self.pos[0]+25, self.pos[1]+ 60))



        if self.locked == False:
            screen.blit(self.trophy,(self.pos[0]+400, self.pos[1] + 15) )
        else:
            screen.blit(self.lock,(self.pos[0]+400, self.pos[1] + 15) )


        
       
        

def setup():
    """
    Initialise necessary things
    """
    global screen, bg_surf,bg_rect
    global title_surf, title_rect, title_bg_surf, title_bg_rect, button_surf, button_rect


    screen = pygame.display.get_surface()
    bg_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
    bg_rect = bg_surf.get_rect()
    title_surf = large_font.render(page_title, False, 'White')
    title_rect = title_surf.get_rect(topleft=(64,64))
    title_bg_surf = pygame.image.load('graphics/art/UI/black_bar1_6x1.png')
    title_bg_surf = pygame.transform.scale(title_bg_surf, (title_rect.width+16, title_rect.height/2))
    title_bg_rect = title_bg_surf.get_rect(bottomleft=(title_rect.left-8, title_rect.bottom))
    button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button.png'),4.0)
    button_rect = button_surf.get_rect(bottomright=(screen.get_width()-64, title_rect.bottom ))
    pygame.mixer.init()

def run():

    setup()
    global button_surf
    inc, counter = 1,0
    mouse_hold, on_click = False, False
    loop = True
    
    
    
    while loop:
        counter += 1
        on_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                on_click = True
            
            
        #Button microinteraction
        if button_rect.collidepoint(pygame.mouse.get_pos()):

            if pygame.mouse.get_pressed()[0]:
                button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button_clicked.png'),4.0)
                if not mouse_hold:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                mouse_hold = True
            else:
                mouse_hold = False
                button_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/back_button.png'),4.0)
            
            loop = False if on_click else True

       
        #animate bg
        inc = -1 if bg_rect.left == 0 else inc
        inc = 1 if bg_rect.right == screen.get_width() else inc
        if not counter % 2:
            bg_rect.left += inc


        
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255,255,255))

        #Blit everything
        #pygame.draw.rect(screen,"#262b44",screen.get_rect())
        screen.blit(bg_surf, bg_rect)
        screen.blit(title_bg_surf, (50,70))
        screen.blit(title_surf, (50,50))
        
       
        screen.blit(button_surf, button_rect)
        
        
        intro_achi = Achievement("Welcome to IBM Village", "This is a welcome achievement.", "We hope you continue to earn more trophies", (50,100), False)
        ai_achi =  Achievement("AI Mastery!", "Well Done! You've gained over", "100 exp in the AI minigame", (50,250), True)
        cyber_achi =  Achievement("Cyber Mastery!","Well Done! You've gained over",  "100 exp in the Cybersecurity minigame", (50,400), True)
        datasci_achi =  Achievement("Datascience Mastery!","Well Done! You've gained over", "100 exp in the Datascience minigame", (50,550), True)
        cloud_achi =  Achievement("Cloud Mastery!","Well Done! You've gained over", "100 exp in the Cloud Computing minigame", (700,100), True)
        iot_achi =  Achievement("IoT Mastery!","Well Done! You've gained over", "100 exp in the Internet of Things minigame", (700,250), True)
        block_achi =  Achievement("Blockchain Mastery!","Well Done! You've gained over", "100 exp in the Blockchain minigame", (700,400), True)


        #will unlock achievements if player has over 100 exp in that minigame
        player_stats = DB.get_user()

        if player_stats.exp_ai > 100:
            ai_achi.locked = False

        if player_stats.exp_cloud > 100:
            cloud_achi.locked = False
        
        if player_stats.exp_cybersecurity > 100:
            cyber_achi.locked = False
        
        if player_stats.exp_blockchain > 100:
            block_achi.locked = False
        
        if player_stats.exp_datascience > 100:
            datasci_achi.locked = False

        if player_stats.exp_iot > 100:
            iot_achi.locked = False

        #displays all achievements
        intro_achi.display()
        ai_achi.display()
        cyber_achi.display()
        datasci_achi.display()
        cloud_achi.display()
        iot_achi.display()
        block_achi.display()

        
        
        
        pygame.display.update()
        clock.tick(60)



