"""
AI Group Project Team 7 Spring22/23

Desc: This module contains function to run the loading screen.
      The loading screen will run untill a coroutine is completed. 
      In this project context, it will be IBM text2Speech.
      However, the code below doesn't specified to IBM only.

Created by: Muhammad Kamaludin
Modified by:
Last modified: 18/5/2023
"""

import sys
import pygame
import asyncio
import time

global coro_success_status
coro_success_status = False
async def run(coroutine_status: asyncio.Event):

    

    screen = pygame.display.get_surface()
    

    #background
    background = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
    background_rect = background.get_rect()

    #text related
    FONT = pygame.font.Font('graphics/font/monogram.ttf',40)
    loading_text = FONT.render('Synthesizing speech from text', False, 'White')
    text_banner = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/brown_rectangle_3x14.png"),2.8)
    text_banner_rect = text_banner.get_rect(center=screen.get_rect().center)

    #animation
    loading_dots = [pygame.Rect(screen.get_rect().center[0] + i*30, screen.get_rect().center[1]+20, 10, 10) for i in range(-4,4)]

    #util
    bg_counter = 0
    loading_counter = 0
    inc = 1
    loop = True
    init_time = time.time()
    current_time = -1

    while loop:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
          
        #animate background
        inc = -1 if background_rect.left == 0 else inc
        inc = 1 if background_rect.right == screen.get_width() else inc
        if not bg_counter % 2: background_rect.left += inc  
        
        #animate the loading dots
        loading_counter = (loading_counter + 1) % 12

        for pos, dot in enumerate(loading_dots):

            if pos == loading_counter:
                dot.bottom -= 10
            
            elif pos == loading_counter + 1 :
                dot.bottom -= 5

            elif pos == loading_counter - 1:
                dot.bottom += 5

            else:
                dot.bottom = screen.get_rect().center[1]+20

        #blit everything
        screen.blit(background,background_rect)
        screen.blit(text_banner,text_banner_rect)
        screen.blit(loading_text, loading_text.get_rect(center=(screen.get_rect().center[0],screen.get_rect().center[1]-30)))
        
        for dots in loading_dots:
            pygame.draw.rect(screen, 'White', dots)

        pygame.display.update()

        if coroutine_status.is_set() : 
            loop = False

        await asyncio.sleep(0.09)

        



async def loading_screen(coroutine):

    loop = asyncio.get_running_loop()

    is_coroutine_complete = asyncio.Event()
    
    #start loading screen in background
    loading_task = asyncio.create_task(run(is_coroutine_complete))
    coroutine_task = asyncio.create_task(coroutine())

    #signal the completion of coroutine
    res = await coroutine_task
    is_coroutine_complete.set()

    #wait for loading screen to complete
    await loading_task

    #show a message of the success/failure status of the text2speech for 1 second
    screen = pygame.display.get_surface()
    t_0 = time.time()
    FONT = pygame.font.Font('graphics/font/monogram.ttf',40)
    loading_text = FONT.render('speech synthesis successful', False, 'White') if res else [FONT.render('speech synthesis failed:', False, 'White'),FONT.render('reached text-to-speech limit', False, 'White')]
    text_banner = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/brown_rectangle_3x14.png"),2.8)
    text_banner_rect = text_banner.get_rect(center=screen.get_rect().center)

    while time.time() - t_0 < 1.5:
        screen.blit(text_banner,text_banner_rect)

        if res:
            screen.blit(loading_text, loading_text.get_rect(center=(screen.get_rect().center)))
        else:
            screen.blit(loading_text[0], loading_text[0].get_rect(midbottom=(screen.get_rect().center[0], screen.get_rect().center[1] - 8)))
            screen.blit(loading_text[1], loading_text[1].get_rect(midtop=(screen.get_rect().center[0], screen.get_rect().center[1] + 4)))
        pygame.display.update()


async def test_coroutine():

    await asyncio.sleep(2)
    return True

    
if __name__ == "__main__":

    coro_success_status = False
    pygame.init()
    pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Loading screen: currently ran directly from loading_screen.py")
    asyncio.run(loading_screen(test_coroutine))
