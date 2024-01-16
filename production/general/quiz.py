"""
AI Group Project Team 7 Spring22/23

Desc: This module contains Quiz and Quiz.Option classes that is used for the general quiz template

Created by: Muhammad Kamaludin
Modified by:
Last modified: 18/5/2023
"""

import sys, os
if __name__ == "__main__":  
    sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import pygame
import asyncio
from typing import Optional
from production.general.loading_screen import loading_screen
from production.general.watson import Text2Speech
from ibm_watson import ApiException

pygame.init()
screen = pygame.display.set_mode((1280,720))

class MultilineText():

    """
    Formatting algo 
    1) check maximum char per text
    2) get a string
    3) slice them into a list of words
    4) make a new list representing lines
    5) iterate over list of word, append a row in the list of lines if len(current line) < maximum char else append the next line
    6) get the text wr
    7) set the text rects relative to the text wrapper
    """

    def __init__(self, text: str, max_char: int=30, font: pygame.font.Font= None, color: str="Black"):
        pygame.init()
        
        self.MAX_CHAR_PER_LINE = max_char

        #set wrappers object to None, it'll be updated later based on the text
        self.wrapper_surf = None  
        self.wrapper_rect = None

        if font:
            self.font = font

        self.color = color
        self.surfs = []
        self.rects = []

        self.raw_text = text
        self.words = self.raw_text.split(" ")
        self.formatted_text = [[]]

        self.process_text()

    def process_text(self):

        """
        Process the raw text, and update the surfs and rects
        the wrapper also will automatically resized to fit the texts
        """

        line_index = 0

        for word in self.words:

            current_len = sum([ len(word) + 1 for word in self.formatted_text[line_index]])

            if len(word) + current_len + 1 < self.MAX_CHAR_PER_LINE: #add 1 space to indicate extra spacing
                #in the same line
                self.formatted_text[line_index].append(word)

            else:

                #move to the new line
                self.formatted_text.append([word])
                line_index += 1


        #format them in to a string instead of list of words, and update the txt and wrapper surfs and rects
        temp_y = 0
        temp_width = 0

        
        for i, line in enumerate(self.formatted_text):

            self.formatted_text[i] = " ".join(line)                                        #turn into 1 string
            self.surfs.append(self.font.render(self.formatted_text[i], False, self.color)) #make the txt surf of that string

            temp_y = pygame.font.Font.get_linesize(self.font)*i + 4*i

            self.rects.append(self.surfs[i].get_rect(topleft = (0, temp_y)))               #make the txt rect of that txt surf
            
            if temp_width < self.surfs[i].get_size()[0]:
                temp_width = self.surfs[i].get_size()[0]

        self.wrapper_surf = pygame.Surface((temp_width, self.rects[len(self.rects)-1].bottom)).convert_alpha()
        self.wrapper_surf.fill((0,0,0,0)) #wrapper surf should be transparent
        self.wrapper_rect = self.wrapper_surf.get_rect()

    def display(self):

        for txt_surf, txt_rect in zip(self.surfs, self.rects ):

            self.wrapper_surf.blit(txt_surf, txt_rect)

class Quiz:
    pygame.init()
    #Essential graphics object
    screen = None
    background,background_rect = None, None
    question_bg_surf, question_bg_rect = None, None
    question, question_rect = None, None
    button_txt, button_txt_rect = None, None 
    submit_button , submit_button_rect = None, None

    FONT_PATH = "graphics/font/monogram.ttf"
    question_font = pygame.font.Font(FONT_PATH, 34)
    button_font = pygame.font.Font(FONT_PATH, 40)
    
    CLOUD_CROSS = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_cross.png"),4)
    CLOUD_CIRCLE = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_circle.png"),4)
    CLOUD_TICK = pygame.transform.scale_by(pygame.image.load("graphics/art/cloud_tick.png"),4)

    #Non graphics object
    clock = pygame.time.Clock()
    on_click = False

    class Option(pygame.sprite.Sprite):

        option_font = None

        def __init__(self, txt: str, is_answer: bool, quiz: Optional[any] = None):
            super().__init__()

            self.quiz = quiz
            self.option_font = pygame.font.Font(self.quiz.FONT_PATH, 30) if self.quiz  else pygame.font.Font(pygame.font.get_default_font(), 20)
            self.image = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/beige_rectangle_2x7.png"),4.5)
            self.rect = self.image.get_rect()
            self.txt = MultilineText(txt, 40, self.option_font, "Black")
            self.txt_rect = self.txt.wrapper_rect
    
            self.is_answer = is_answer

        def set_position(self, sides: list[int]):

            self.rect.left = int(sides[0]) if sides[0] else self.rect.left
            self.rect.top = int(sides[1]) if sides[1] else self.rect.top
            self.rect.right = int(sides[2]) if sides[2] else self.rect.right
            self.rect.bottom = int(sides[3]) if sides[3] else self.rect.bottom
            self.txt_rect.center = self.rect.center

        def update(self, quiz):


            self.quiz.screen.blit(self.image, self.rect)               #blit option banner bg
            self.txt.display()                                         #blit the lines of text into the wrapper
            self.quiz.screen.blit(self.txt.wrapper_surf,self.txt_rect) #blit the wrapper into the screen

            #click effect
            if self == quiz.selected_option:
                self.quiz.screen.blit(Quiz.CLOUD_CIRCLE, (self.rect.right - 64 -16,self.rect.top + 32))

            if quiz.is_submitted:
                if self.is_answer:
                    self.quiz.screen.blit(Quiz.CLOUD_TICK, (self.rect.right - 64 -16,self.rect.top + 32))
                if self == quiz.selected_option and not self.is_answer:
                    self.quiz.screen.blit(Quiz.CLOUD_CROSS, (self.rect.right - 64 -16,self.rect.top + 32))

    def __init__(self, question: str, choice: list[str], answer: str):

        pygame.display.set_mode((1280,720))
        self.question = MultilineText(question, 70, self.question_font, "White")
        self.options = [self.Option(opt, opt == answer,self) for opt in choice]
        self.options_group = pygame.sprite.Group()
        for opt in self.options:
            self.options_group.add(opt)
        self.selected_option = None
        self.is_submitted = False
        self.speech_synthesized = False

    def display(self):
        """
        Blit or draw everything
        """
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.question_bg_surf,self.question_bg_rect)
        
        #Blit the text wrapper into the screen, blit the text into the wrapper using 
        self.screen.blit(self.question.wrapper_surf, self.question_rect)
        self.question.display()

        self.screen.blit(self.submit_button, self.submit_button_rect)
        self.screen.blit(self.button_txt, self.button_txt_rect)

        #objects in option group is drawn in update function
        self.options_group.update(self)
    
    def setup(self):
        """
        Initialize essential graphics objects
        """


        T2S_AUDIO_FILE_PATH = 'graphics/audio/text2speech.wav'

        #display the loading screen while synthesizing speech from the quiz prompt simultaneously
        asyncio.run(loading_screen(self.convert_question_to_speech))

        #set the background
        self.screen = pygame.display.get_surface()
        self.background = pygame.transform.scale_by(pygame.image.load("graphics/art/bg_1.png"),2)
        self.background_rect = self.background.get_rect()

        #Set the question
        self.question_bg_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/brown_rectangle_3x14.png"),4.5)
        self.question_bg_rect = self.question_bg_surf.get_rect(midtop=(self.screen.get_width()/2,64))
        self.question_rect = self.question.wrapper_rect
        self.question_rect.center = self.question_bg_rect.center

        #set the answer options
        REF_POINT = (self.screen.get_width()/2 , self.screen.get_height()*3/4-50) # the center between four option blocks (x,y)
        for index, opt in enumerate(self.options):
            binary_index = format(index, '02b')
            sides = [0,0,0,0] #value of [left, top, right, bottom]
            if int(binary_index[0]):
                sides[1] = REF_POINT[1] + 4
            else:
                sides[3] = REF_POINT[1] - 4

            if int(binary_index[1]):
                sides[0] = REF_POINT[0] + 4
            else:
                sides[2] = REF_POINT[0] - 4
            
            opt.set_position(sides)
            self.options_group.add(opt)
        
        #set submit button
        self.button_txt = self.button_font.render("submit", False, 'White')
        self.button_txt_rect = self.button_txt.get_rect()
        self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)
        self.submit_button_rect = self.submit_button.get_rect(midbottom=(REF_POINT[0], self.screen.get_height() - 16))
        self.button_txt_rect.center = self.submit_button_rect.center

        #play BGM
        pygame.mixer.init()
        pygame.mixer.Channel(0).set_volume(0.1)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_bgm.wav'),-1)
        #only play audio file when it's synthesized, bcs otherwise, the audio file will have the old audio
        if self.speech_synthesized: 
            pygame.mixer.Channel(2).set_volume(0.1)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(T2S_AUDIO_FILE_PATH))
        

    def run(self):

        self.setup()

        #some variable for animation
        counter,inc = 0, 1
        temp_rect = self.button_txt_rect.bottom
        mouse_hold = False

        #Actual quiz logic
        is_finished = False
        while not is_finished:
            counter += 1
            self.on_click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.on_click = True

            
            #Handle interaction(s) with the answer options
            if not self.is_submitted and self.on_click:
                for opt in self.options:
                    #self.selected_option = opt if opt.rect.collidepoint(pygame.mouse.get_pos()) else self.selected_option
                    if opt.rect.collidepoint(pygame.mouse.get_pos()):
                        self.selected_option = opt
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/quiz_select_answer.wav'))

            #Handle interaction(s) with the submit button 
            if self.submit_button_rect.collidepoint(pygame.mouse.get_pos()):
                
                #button click micro interaction
                if pygame.mouse.get_pressed()[0]:
                    self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1_clicked.png").convert_alpha(),4.5)
                    self.button_txt_rect.bottom = temp_rect + 4
                    if not mouse_hold:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('graphics/audio/button_click.wav'))
                    mouse_hold = True   
                else:
                    mouse_hold = False
                    self.submit_button = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png").convert_alpha(),4.5)
                    self.button_txt_rect.bottom = temp_rect

                #Update quiz state
                if self.on_click and self.selected_option:
                    is_finished = self.is_submitted if self.is_submitted else is_finished
                    self.is_submitted = True
                    self.button_txt = self.button_font.render("Continue", False, 'White')
                    self.button_txt_rect = self.button_txt.get_rect(center=self.submit_button_rect.center)

                    pygame.mixer.Channel(2).set_volume(0)
                    if self.selected_option.is_answer:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_correct.wav'))
                    else:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('graphics/audio/quiz_wrong.wav'))

            #animate background
            inc = -1 if self.background_rect.left == 0 else inc
            inc = 1 if self.background_rect.right == self.screen.get_width() else inc

            if not counter % 2: self.background_rect.left += inc    
            
            self.display()

            pygame.display.update()
            self.clock.tick(60)

    def get_score(self):

        if self.selected_option:
            return int(self.selected_option.is_answer)
        else:
            return 0
    
    def reset(self):
        self.is_submitted = False
        self.selected_option = None


    async def convert_question_to_speech(self):

        await asyncio.sleep(1.1)
        '''T2S_API_KEY = ''     add api here
        T2S_URL = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/35d8bb6c-9061-4ed2-82ba-d46e558cdec8'
        #T2S_API_KEY = ''       add api here
        #T2S_URL = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/39bd2aae-af32-48c2-8c04-20131d0adde1'

        watson = Text2Speech.Text2Speech(T2S_API_KEY,T2S_URL)
        #watson.synthesize_by_str(self.question.raw_text) 
        self.speech_synthesized = watson.success
        return self.speech_synthesized'''


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Quiz page")

    #create quiz object
    test_question ="One of the challenges of a multi-cloud approach is that different cloud solutions run in different software environments. Organizations want to build applications that can easily move across a wide range of these environments without creating integration difficulties. Which of the following helps mitigate such challenges?"
    s = "Incidents where attackers gain access to vulnerable systems left exposed by inexperienced administrators or users (e.g., default factory settings"
    test_options = ["Use private and public cloud in your business", s, "Use Container technologies","All of them"]
    q1 = Quiz(test_question, test_options, "Use Container technologies")

    #run the page
    #By running the object, it will run the quiz page. all of the interactions will be handled automatically
    q1.run()

    #get score
    #print(q1.get_score())