import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((1280, 720))
screen_r = screen.get_rect()
FONT_PATH = 'graphics/font/PeaberryBase.ttf'
large_font = pygame.font.Font(FONT_PATH, 48)
clock = pygame.time.Clock()

def run_credits():
    loop = True

    background = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"), 2)
    background_rect = background.get_rect()
    counter, inc = 0, 1

    credit_list = ["CREDITS - IBM Village", "A Game For Jon Mcnamara", " ", "Alex - Outside World / CyberSecurity", "Filé - Player House / AI", "Muhammad - Stats / Quiz / Cloud/ Database", "Zhongjie - Database / Data Science", "Kevin - IBM Watson / Blockchain", " ", "Signed, Mcnamara's Band"]

    texts = []
    for i, line in enumerate(credit_list):
        s = large_font.render(line, 1, (255, 255, 255))
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i*2 * 45)
        texts.append((r, s))

    pygame.mixer.init()
    pygame.mixer.music.load('assets/sound/McNamaras-Band.wav')
    pygame.mixer.music.play(-1, 0.0, 1)

    while loop:

        counter += 1

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                loop = False

        screen.blit(background, background_rect)
        #screen.fill((255, 255, 255))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -1)
            # and drawing is as simple as this
            screen.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            loop = False

        inc = -1 if background_rect.left == 0 else inc
        inc = 1 if background_rect.right == screen.get_width() else inc

        background_rect.left += inc

        # only call this once so the screen does not flicker
        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(30.45)

    pygame.mixer.music.stop()

if __name__ == '__main__':
    run_credits()