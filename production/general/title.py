import pygame
from pygame.locals import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
print(sys.path)

from production.outside_world.code.main import Game


pygame.init()
pygame.display.set_caption('Title')
screen = pygame.display.set_mode((1280, 720))
screen_r = screen.get_rect()
FONT_PATH = 'graphics/font/PeaberryBase.ttf'
large_font = pygame.font.Font(FONT_PATH, 48)
medium_font = pygame.font.Font(FONT_PATH, 32)
small_font = pygame.font.Font(FONT_PATH, 20)
smallest_font = pygame.font.Font(FONT_PATH, 15)
clock = pygame.time.Clock()

def run_title():
    loop = True

    background = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"), 2)
    background_rect = background.get_rect()
    counter, inc = 0, 1

    '''pygame.mixer.init()
    pygame.mixer.music.load('assets/sound/McNamaras-Band.wav')
    pygame.mixer.music.play(-1, 0.0, 1)'''

    while loop:

        counter += 1

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                loop = False
            if e.type == KEYDOWN and e.key == pygame.K_x:
                game = Game()
                game.run()


        screen.blit(background, background_rect)

        title_text_surf = large_font.render("Welcome to IBM Village", False, (234, 212, 170))
        play_text_surf = small_font.render("This is a Game to Harness Your Skills in The Areas of:", False, 'White')
        play_text_surf3 = smallest_font.render("- A.I", False, 'White')
        play_text_surf4 = smallest_font.render("- CyberSecurity", False, 'White')
        play_text_surf5 = smallest_font.render("- Data Science", False, 'White')
        play_text_surf6 = smallest_font.render("- Cloud Computing", False, 'White')
        play_text_surf7 = smallest_font.render("- Internet of Things", False, 'White')
        play_text_surf8 = smallest_font.render("- Blockchain", False, 'White')

        info_text_surf = small_font.render("Explore the World of IBM and Enter Portals to Play Revision Mini-Games (Use ESC to Go Back at Any Point)", False, 'White')
        info_text_surf2 = small_font.render("Don't Forget to Check your Stats at the Blacksmith", False, 'White')
        info_text_surf3 = small_font.render("As Well as View your Achievements in Your Home", False, 'White')

        to_play_text_surf = medium_font.render("Press X to Play", False, (234, 212, 170))

        screen.blit(title_text_surf, (screen.get_width()/2 - title_text_surf.get_width()/2, screen.get_height()/5 - title_text_surf.get_height()/2))

        screen.blit(play_text_surf, (screen.get_width()/2 - play_text_surf.get_width()/2, screen.get_height()/3 - play_text_surf.get_height()/2))
        screen.blit(play_text_surf3, (screen.get_width()/2 - play_text_surf3.get_width()/2, screen.get_height()/3 - play_text_surf3.get_height()/2 + 50))
        screen.blit(play_text_surf4, (screen.get_width()/2 - play_text_surf4.get_width()/2, screen.get_height()/3 - play_text_surf4.get_height()/2 + 80))
        screen.blit(play_text_surf5, (screen.get_width()/2 - play_text_surf5.get_width()/2, screen.get_height()/3 - play_text_surf5.get_height()/2 + 110))
        screen.blit(play_text_surf6, (screen.get_width()/2 - play_text_surf6.get_width()/2, screen.get_height()/3 - play_text_surf6.get_height()/2 + 140))
        screen.blit(play_text_surf7, (screen.get_width()/2 - play_text_surf7.get_width()/2, screen.get_height()/3 - play_text_surf7.get_height()/2 + 170))
        screen.blit(play_text_surf8, (screen.get_width()/2 - play_text_surf8.get_width()/2, screen.get_height()/3 - play_text_surf8.get_height()/2 + 200))

        screen.blit(info_text_surf, (screen.get_width()/2 - info_text_surf.get_width()/2, screen.get_height()/3 - info_text_surf.get_height()/2 + 250))
        screen.blit(info_text_surf2, (screen.get_width()/2 - info_text_surf2.get_width()/2, screen.get_height()/3 - info_text_surf2.get_height()/2 + 300))
        screen.blit(info_text_surf3, (screen.get_width()/2 - info_text_surf3.get_width()/2, screen.get_height()/3 - info_text_surf3.get_height()/2 + 350))

        screen.blit(to_play_text_surf, (screen.get_width()/2 - to_play_text_surf.get_width()/2, screen.get_height()*4/5 - to_play_text_surf.get_height()/2 + 75))

        inc = -1 if background_rect.left == 0 else inc
        inc = 1 if background_rect.right == screen.get_width() else inc

        background_rect.left += inc

        pygame.display.flip()

        clock.tick(30)

if __name__ == '__main__':
    run_title()