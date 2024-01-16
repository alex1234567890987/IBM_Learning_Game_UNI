"""
AI Group Project Team 7 Spring22/23

Desc: This module control and display the minigame of the cloud house.
It imports level_builder so it can display the the minigame level 

Created by: Muhammad Kamaludin
Modified by:
Last modified: 18/5/2023
"""

import pygame
import production.general.db.DatabaseService as DB
import production.general.quiz as quiz
from production.cloud_house import level_builder

def score_screen():
    """
    Game loop for score screen
    """
    global screen, bg, bg_banner, score, FONTS
    global next_button_surf, next_button_rect
    global button_text_surf, button_text_rect
    loop = True
    on_click = False

    TXTS_REF_POINT = (screen.get_size()[0]/2, screen.get_size()[1]/2 - 70)
    message_txt = FONTS[1].render("Well Done, you cleared all sublevels!", False, "Black")
    score_txt = FONTS[1].render(f"score: {score}", False, "Black")
    exp_txt = FONTS[1].render(f"cloud exp: +{int(score/5)}", False, "Black")
    next_button_rect.center = (screen.get_size()[0]/2, screen.get_size()[1]*3/4 - 70)
    button_text_surf = FONTS[0].render("CONTINUE", False, "White")
    button_text_rect = button_text_surf.get_rect(center = next_button_rect.center)

    while loop:
        on_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                on_click = True

        pygame.draw.rect(screen,(25,36,40),bg)
        screen.blit(bg_banner, bg_banner.get_rect(center=bg.center))
        screen.blit(message_txt, message_txt.get_rect(midbottom= (TXTS_REF_POINT[0],TXTS_REF_POINT[1]- 16)))
        screen.blit(score_txt, score_txt.get_rect(center= (TXTS_REF_POINT[0],TXTS_REF_POINT[1])))
        screen.blit(exp_txt, exp_txt.get_rect(midtop=(TXTS_REF_POINT[0],TXTS_REF_POINT[1]+ 16)))
        screen.blit(next_button_surf,next_button_rect)
        screen.blit(button_text_surf, button_text_rect)

        #button click micro interation and animation 
        if next_button_rect.collidepoint(pygame.mouse.get_pos()):
                
            if pygame.mouse.get_pressed()[0]:
                next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1_clicked.png"),4.5)
                    
                if not mouse_hold:
                    button_text_rect.y += 4
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                mouse_hold = True
            else:
                mouse_hold = False
                next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)

            if on_click: button_text_rect.y -= 4
            loop = False if on_click else True
    
        pygame.display.update()
        clock.tick(24)

def display_level_page(level: level_builder.Level):
    """
    Draw everything for the level page
    """
    global screen, bg, bg_banner, FONTS
    global levels, level_counter, initial_time
    global next_button_surf, next_button_rect
    global button_text_surf, button_text_rect

    #diplay bg stuff
    pygame.draw.rect(screen,(25,36,40),bg)
    screen.blit(bg_banner, bg_banner.get_rect(center=bg.center))
    
    #display multilines texts of instruction
    x, y = 24,160 #tiles wrapper rect (x=440 y=160 width=400 height=400)
    for sentence_surfs in instructions_txts_surfs:
        for i, txt_surfs in enumerate(sentence_surfs):
            screen.blit(txt_surfs, (x,y))
            y += (txt_surfs.get_size()[1] + 8) if not (i == len(sentence_surfs) - 1) else 0
        y += 48

    #display time in {minute:2digits}:{seconds:2digits} format
    time_elapsed = int(pygame.time.get_ticks()/1000 - (initial_time))
    screen.blit(FONTS[1].render("TIME " + str(int(time_elapsed/60)).zfill(2) + ":"+ str(time_elapsed%60).zfill(2) , False,"Black"), (440+400+24, 200))

    #display current sublevel count
    screen.blit(FONTS[1].render(f"SUBLEVEL {level_counter} OF {len(levels)}", False,"Black"), (440+400+24, 160))

    #display next button
    if in_between_sublevel:
        screen.blit(next_button_surf,next_button_rect)
        screen.blit(button_text_surf, button_text_rect)
    #display tiles
    level.display_on_screen(screen)

def run_level(level: level_builder.Level):
    """
    Execute the level as well as the quiz
    """

    global screen, bg, bg_banner, clock, in_between_sublevel
    global next_button_surf, next_button_rect
    global button_text_rect

    mouse_hold = False
    on_click = False
    loop = True
    locked_tile = None

    #It will stays in the loop until it is complete or if it changes to quiz state, as it will enter new loop to render quiz
    while loop:

        on_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                on_click = True

        display_level_page(level)
        
        if in_between_sublevel:

            #button click micro interation and animation 
            if next_button_rect.collidepoint(pygame.mouse.get_pos()):
                
                if pygame.mouse.get_pressed()[0]:
                    next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1_clicked.png"),4.5)
                    
                    if not mouse_hold:
                        button_text_rect.y += 4
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                    mouse_hold = True
                else:
                    mouse_hold = False
                    next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)

                if on_click: button_text_rect.y -= 4
                loop = False if on_click else True

        else:

            #Interaction on tiles
            for tile in [tile for row in level.layout for tile in row]: #flatten the list
            
                if tile.type in ['blank','input','output','4branch']: continue
            
                #hover effect
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    temp_surf = pygame.transform.scale_by(tile.surf,1.2)
                    temp_rect = temp_surf.get_rect(center=tile.rect.center)
                    screen.blit(temp_surf,temp_rect)

                #rotate tile on click (it will check if the puzzle is completed after every rotation if the quiz is answered)
                if (not tile.locked) and on_click and tile.rect.collidepoint(pygame.mouse.get_pos()):
                    tile.rotate()

                    in_between_sublevel = level.is_answered and level.is_complete()
            
                #run quiz page if locked tile is clicked
                elif tile.locked and on_click and tile.rect.collidepoint(pygame.mouse.get_pos()):

                    locked_tile = tile
                    level.quiz.run()

                    if level.quiz.get_score():
                        locked_tile.unlock()
                        locked_tile = None
                        level.is_answered = True
                    else:
                        level.quiz.reset()
        

        pygame.display.update()
        clock.tick(24)
    
    in_between_sublevel = False


def setup(**setting):

    global screen, bg, bg_banner, clock
    global levels, score
    global player_stats
    global next_button_surf, next_button_rect
    global button_text_surf, button_text_rect
    global instructions_txt, instructions_txts_surfs
    # Boolean value to indicate the status when your have finished a sublevel,
    # but hasn/t proceed to the next sublevel, this is used to pause some rendering during that phase
    global in_between_sublevel
    global FONTS

    #graphics objects
    screen = pygame.display.get_surface()
    bg = pygame.Rect((0,0),screen.get_size())
    bg_banner = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/beige_rectangle_2x7.png"),20)

    FONTS = [pygame.font.Font('graphics/font/PeaberryBase.ttf', 18), pygame.font.Font('graphics/font/PeaberryBase.ttf', 32)]
    instructions_txts = [["HOW TO PLAY?"], 
                         ["The goal is to connect the power supply", "to the other endpoint by rotating the","cable to a specific direction"],
                         ["Click on the cables to rotate them"],
                         ["Some tiles are locked, you may answer","a quiz before you can rotate them"],
                         ["The faster you complete this level","the higher the score"]]
    
    #turn those texts into txt surface but maintaining the list strcture
    instructions_txts_surfs = [ [ FONTS[0].render(txt,False,"Black") if i else FONTS[1].render(txt,False,"Black") for txt in sentence] for i, sentence in enumerate(instructions_txts)]
    next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)
    next_button_rect = next_button_surf.get_rect(bottomleft=(440+400+24,160+400))
    button_text_surf = FONTS[0].render("NEXT  >>", False, "White")
    button_text_rect = button_text_surf.get_rect(center = next_button_rect.center)
    #essential non_graphics objects/var
    clock = pygame.time.Clock()
    difficulty = setting["difficulty"]
    player_stats = setting["player_stats"]
    levels = level_builder.get_levels( 3*(difficulty-1),3*(difficulty-1)+2)
    quizzes = DB.get_questions(difficulty,"cloud")
    score = 0
    in_between_sublevel = False

    #set quizzes to the sublevels
    for i, level in enumerate(levels):
        level.quiz = quizzes[i]


def run(diff: int = 0, user=None):
    """
    This is the entry point of the minigame
    """
    setup(difficulty = diff, player_stats = user)

    global player_stats, score 
    global levels, level_counter
    global initial_time

    level_counter = 0
    initial_time = pygame.time.get_ticks()/1000 + 1
    for level in levels:
        level_counter += 1
        run_level(level)

    MAX_SCORE = 20000
    score = int( MAX_SCORE / int(pygame.time.get_ticks()/1000 - initial_time))

    
    player_stats.exp_cloud += int(score/5)  
    player_stats.highscore_cloud = score
    DB.update_user(player_stats)

    score_screen()


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('Cloud house: Currently running directly from minigame.py')
    run()