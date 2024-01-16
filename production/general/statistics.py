"""
AI Group Project Team 7 Spring22/23

Desc: This module responsible for the statistics page
Created by: Muhammad Kamaludin
Modified by:
Last modified: 9/4/2023
"""
import pygame
from typing import Optional
from production.general.db import DatabaseService as DB

pygame.init()

HOUSES = ["A.I.","Blockchain","Cloud Computing","Cybersecurity","Data Science", "Internet of Things"]
page_title = "Statistics"
money = 0
exp = 0
exps = [0,0,0,0,0,0]
personal_bests = [0,0,0,0,0,0]
clock = pygame.time.Clock()
stats_blocks = [ None for i in exps]

#graphis object
FONT_PATH = 'graphics/font/PeaberryBase.ttf'
large_font = pygame.font.Font(FONT_PATH, 48)
medium_font = pygame.font.Font(FONT_PATH, 24)
small_font = pygame.font.Font(FONT_PATH, 16)
screen = None
bg_surf, bg_rect = None, None
statsblocks_wrapper_surf, statsblocks_wrapper_rect = None, None
title_surf, title_rect = None, None
title_bg_surf, title_bg_rect = None, None
button_surf, button_rect = None, None
exp_bg_surf, exp_bg_rect = None, None
exp_surfs, exp_rects = [None,None], [None, None] 

class StatsBlock(pygame.sprite.Sprite):

    """
    This text block is a wrapper consists of three types text surfaces(header,subheader and data).
    This is used for example to handle the display of data like 
    
    'AI House              <-- Header
    
     exp:            20    <-- subheader:    data
     personal best:  40'   <-- subheader:    data *number of subheaders is dynamic

    """

    def __init__(self, header: str, subheaders: list[str], data: list[float|str], asset_path: Optional[str] = None):
        temp_path = asset_path if asset_path else 'graphics/art/UI/beige_rectangle_3x2.png'
        self.image = pygame.transform.scale_by(pygame.image.load(temp_path),6.7)
        self.rect = self.image.get_rect()
        self.set_header(header)
        min_len = min(len(subheaders),len(data))
        self.set_subheaders(subheaders[:min_len])
        self.set_data(data[:min_len])

    def set_size(self, width: int, height:int):
        self.image = pygame.Surface((width,height))
        self.image.fill(self.SECONDARY_COLOUR)
        self.rect = self.image.get_rect()

    def set_header(self, header: str):
        self.header = header
        self.header_surf = medium_font.render(header, False, "Black")
        self.header_rect = self.header_surf.get_rect()

    def set_subheaders(self, subheaders: list[str]):
        self.subheaders_surf, self.subheaders_rect = [ None for i in range(len(subheaders)) ],[ None for i in range(len(subheaders))]
        self.subheaders = subheaders
        for i in range(len(subheaders)):
            self.subheaders_surf[i] = small_font.render(self.subheaders[i], False, "Black")
            self.subheaders_rect[i] = self.subheaders_surf[i].get_rect()

    def set_data(self, data: list[str|float]):
        self.data, self.data_surf, self.data_rect = ["" for i in range(len(data))],[ None for i in range(len(data)) ],[ None for i in range(len(data))]

        for i in range(len(data)):
            self.data[i] = f"{data[i]:,.2f}" if isinstance(data[i], float) else str(data[i])
            self.data_surf[i] = small_font.render(self.data[i], False, "Black")
            self.data_rect[i] = self.data_surf[i].get_rect()

    def format(self, left: Optional[int] = None, top: Optional[int] = None, right: Optional[int] = None, bottom: Optional[int] = None):
        """
        Format the size of the wrapper or to position the text surfaces nicely
        Assuming the wrapper using image, size is fixed
        """
  
        self.rect.left = left if left is not None else self.rect.left
        self.rect.top = top if top is not None else self.rect.top
        self.rect.right = right if right is not None else self.rect.right
        self.rect.bottom = bottom if bottom is not None else self.rect.bottom
        
        #pos the header and data in a stack
        SPACING = (8,16,24,32)
        self.header_rect.topleft = (self.rect.left + SPACING[2], self.rect.top + SPACING[2])
        
        for i in range(len(self.subheaders)):
            if i:
                self.subheaders_rect[i].topleft = (self.header_rect.left, self.subheaders_rect[i-1].bottom + SPACING[1]) 
            else:
                self.subheaders_rect[i].topleft = (self.header_rect.left, self.header_rect.bottom + SPACING[2]) 
            self.data_rect[i].topright = (self.rect.right - SPACING[1], self.subheaders_rect[i].top)
    
    def display(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.header_surf, self.header_rect)
        for i in range(len(self.subheaders)):
            screen.blit(self.subheaders_surf[i], self.subheaders_rect[i])
            screen.blit(self.data_surf[i], self.data_rect[i])

def setup():
    """
    Initialise necessary things
    """
    global screen, bg_surf,bg_rect, stats_blocks, statsblocks_wrapper_surf, statsblocks_wrapper_rect
    global title_surf, title_rect, title_bg_surf, title_bg_rect, button_surf, button_rect
    global exp, exp_bg_surf, exp_bg_rect, exp_surfs, exp_rects

    screen = pygame.display.get_surface()
    bg_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
    bg_rect = bg_surf.get_rect()
    title_surf = large_font.render(page_title, False, 'White')
    title_rect = title_surf.get_rect(topleft=(64,64))
    title_bg_surf = pygame.image.load('graphics/art/UI/black_bar1_6x1.png')
    title_bg_surf = pygame.transform.scale(title_bg_surf, (title_rect.width+16, title_rect.height/2))
    title_bg_rect = title_bg_surf.get_rect(bottomleft=(title_rect.left-8, title_rect.bottom))

    player_stats = DB.get_user()

    exp = f"{exp:,.2f}" if isinstance(exp, float) else str(exp)
    exp_bg_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/black_bar2_6x1.png'), 3)
    exp_bg_rect = exp_bg_surf.get_rect(bottomleft = (title_bg_rect.right+16, title_bg_rect.bottom))
    exp_surfs = [small_font.render('Overall Exp:', False, 'White'), small_font.render(exp, False, 'White')]
    exp_rects[0] = exp_surfs[0].get_rect(left=exp_bg_rect.left+10, bottom=exp_bg_rect.bottom-8)
    exp_rects[1] = exp_surfs[1].get_rect(right=exp_bg_rect.right-10, bottom=exp_bg_rect.bottom-8)

    exps = [player_stats.exp_ai, player_stats.exp_blockchain, player_stats.exp_cloud, player_stats.exp_cybersecurity, player_stats.exp_datascience, player_stats.exp_iot]
    personal_bests = [player_stats.highscore_ai, player_stats.highscore_blockchain, player_stats.highscore_cloud, player_stats.highscore_cybersecurity, player_stats.highscore_datascience, player_stats.highscore_iot]

    print(exps)
    #initialize all stats blocks
    for i, header in enumerate(HOUSES):
        stats_blocks[i] = StatsBlock(header, ['Experience','Personal Best'], [exps[i],personal_bests[i]])

    #Position the stats block in a wrapper and 2x3 grid below it
    statsblocks_wrapper_surf = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/brown_rectangle_14x6.png'),5.2)
    statsblocks_wrapper_rect = statsblocks_wrapper_surf.get_rect()
    statsblocks_wrapper_rect.midbottom = (screen.get_width()/2, screen.get_height() - 64)
    
    REF_POINT = statsblocks_wrapper_rect.center # the center between sixoption blocks
    temp_spacing = ((statsblocks_wrapper_rect.height - 2*stats_blocks[0].rect.height - 64)/3,
                    (statsblocks_wrapper_rect.width - 3*stats_blocks[0].rect.width - 64)/4 ) #(row,col)
    for index, block in enumerate(stats_blocks):
        binary_index = format(index+1, '03b')
        #set the row
        if sum([ int(n) for n in binary_index]) == 2:
            block.format(top=REF_POINT[1] + temp_spacing[0]/2)
        else:
            block.format(bottom=REF_POINT[1] - temp_spacing[0]/2)

        #set the column
        if binary_index[0] == binary_index[1]:
            block.format(right=REF_POINT[0] - block.rect.width/2 - temp_spacing[1])
        elif binary_index[0] == binary_index[2]:
            block.format(left=REF_POINT[0] + block.rect.width/2 + temp_spacing[1])
        elif binary_index[1] == binary_index[2]:
            block.format(left=REF_POINT[0] - block.rect.width/2)

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

        #Blit everything
        #pygame.draw.rect(screen,"#262b44",screen.get_rect())
        screen.blit(bg_surf, bg_rect)
        screen.blit(title_bg_surf, title_bg_rect)
        screen.blit(title_surf, title_rect)
        screen.blit(exp_bg_surf, exp_bg_rect)
        for s, r in zip(exp_surfs,exp_rects):
            screen.blit(s,r)
        screen.blit(button_surf, button_rect)
        screen.blit(statsblocks_wrapper_surf,statsblocks_wrapper_rect)
        for block in stats_blocks:
            block.display()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    
    #How to use run this page?
    # 1) import this page
    # 2) Get pygame initiated
    # 3) Make Player object
    # 4) run!

    screen = pygame.display.set_mode((1280,720))
    player_obj = "Yo"
    run(player_obj)

