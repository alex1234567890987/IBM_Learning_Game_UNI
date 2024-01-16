import pygame
from pygame.locals import *
import sys, os
from pygame import mixer
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import production.general.db.DatabaseService as DB
import random





#initialise pygame
pygame.init()
    
screen_width = 1280
screen_height = 720
pygame.display.set_caption('AI House')
player_stats = DB.get_user()
#gets player's stats
db_questions = DB.get_questions(1, 'ai')
#gets questions from database




screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.Rect((0,0),screen.get_size())
end = False

#define background image
bg_img = pygame.image.load('ai_house/images/game_bg.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))





#define game variables
margin = 50
fps = 70
live_ball = False
fps_clock = pygame.time.Clock()
i=0
exp = 0
quiz_status = None




#define colours
white = (255, 255, 255)
blue = (3, 165, 252)
green = (3, 252, 74)
red = (252, 3, 3)

#define font
font = pygame.font.Font('graphics/font/Gameplaya.ttf', 20)


mixer.init()
mixer.music.load('ai_house/sounds/Sleepless-City-Synthwave-Retrowave-Music.mp3')
#music


def score_screen(exp):
    """
    Game loop for score screen
    """
    global screen, player_stats, player_score, cpu_score,i
    loop = True
    on_click = False

    TXTS_REF_POINT = (screen.get_size()[0]/2, screen.get_size()[1]/2 - 70)
    medium_font = pygame.font.Font('graphics/font/Gameplaya.ttf', 18)
    biggest_banner_image = pygame.transform.scale_by(pygame.image.load('graphics/art/UI/beige_rectangle_2x7.png'),4.3)
    text_surf1 = medium_font.render("WELL DONE! YOU'VE BEATEN THE AI", False, 'Black')
    text_surf2 = medium_font.render(F"YOU'VE EARNED {exp} EXP ", False, 'Black')
    text_surf3 =  medium_font.render(F"YOU HAVE A NEW HIGHSCORE OF  {player_score} ", False, 'Black')
    next_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/art/UI/button_2x1.png"),4.5)
    next_button_rect = next_button_surf.get_rect(bottomleft=(440+400+24,160+400))
    button_text_surf = medium_font.render("NEXT  >>", False, "White")
    button_text_rect = button_text_surf.get_rect(center = next_button_rect.center)

    
    next_button_rect.center = (screen.get_size()[0]/2, screen.get_size()[1]*3/4 - 70)
    button_text_surf = medium_font.render("CONTINUE", False, "White")
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
        screen.blit(biggest_banner_image, biggest_banner_image.get_rect(center=bg.center))
        screen.blit(text_surf1, text_surf1.get_rect(midbottom= (TXTS_REF_POINT[0],TXTS_REF_POINT[1]+55)))
        screen.blit(text_surf2, text_surf2.get_rect(center= (TXTS_REF_POINT[0],TXTS_REF_POINT[1]+60)))
        

        if player_stats.highscore_ai < player_score:
            print("high score")
            screen.blit(text_surf3, text_surf3.get_rect(center= (TXTS_REF_POINT[0],TXTS_REF_POINT[1]+70)))


        screen.blit(next_button_surf,next_button_rect)
        screen.blit(button_text_surf, button_text_rect)

        player_stats.exp_ai += exp
        if player_stats.highscore_ai < player_score:
            player_stats.highscore_ai = player_score
        DB.update_user(player_stats)

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
            player_score, cpu_score = 0,0
            exp, i = 0,0
    
        pygame.display.update()
        fps_clock.tick(24)


def miniquiz():
    """
    logic for miniquiz after getting a point against AI
    """
    global  quiz_status, exp, i
    
    mixer.music.pause()
    

    db_questions[i].run()
    # quiz_status = False

    if db_questions[i].get_score() == 1:
        #if player gets the question right
        exp += 10
        i+=1
        cpu_paddle.speed -= 1
        

    elif db_questions[i].get_score() == 0:
        #if the player gets the question wrong
        i+=1
        cpu_paddle.speed += 2
    
    if i > (len(db_questions)-1):#
        #when the list of questions is empty, score screeen will
        score_screen(exp)
        

    

def draw_board():
    """Draws pong layout"""
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)



def draw_text(text, font, text_col, x, y):
    """Allows us to write text"""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))




class paddle():
    #paddle class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(x, y, 20, 90)
        self.speed = 7
        self.ai_speed = 6

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)
            
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
            

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def ai(self):
        #ai to move the paddle automatically
        #move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.ai_speed)
        #move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.ai_speed)



class ball():
    #ball/pong class
    def __init__(self, x, y):
        self.reset(x, y)
        self.speed_x = -7
        self.speed_y = 5
       


    def move(self):

        #check collision with top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check collision with bottom of the screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1

        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.left > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner


    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)


    def reset(self, x, y ):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
        self.winner = 0
 # 1 is the player and -1 is the CPU



 


def run():
    mixer.music.play()
    global quiz_status, player_score, cpu_score
    live_ball = False
    winner = 0
    speed_increase = 0
    player_score, cpu_score = 0,0
    max_speed = -11
    
    #create game loop
    run = True
    
    while run:
        
        screen.blit(bg_img,(0,0))
        fps_clock.tick(fps) 
        draw_board()
        draw_text('CPU: ' + str(cpu_score), font, red, 20, 15)
        draw_text('P1: ' + str(player_score), font, blue, screen_width - 100, 15)
        draw_text('BALL SPEED: ' + str(abs(pong.speed_x)), font, white, screen_width // 2 - 100 , 15)
        draw_text('EXP: ' + str(exp), font, white, screen_width // 2 + 200  , 15)
        
        #draw paddles
        player_paddle.draw()
        cpu_paddle.draw()
        

        

        if live_ball == True:
            speed_increase += 1
            winner = pong.move()
            if winner == 0:
                #draw ball
                pong.draw()
                #move paddles
                player_paddle.move()
                cpu_paddle.ai()
            else:
                live_ball = False
                if winner == 1:
                    player_score += 1
                    
                    

                elif winner == -1:
                    cpu_score += 1


        #print player instructions
        if live_ball == False:
            if winner == 0:
                draw_text('CLICK ANYWHERE TO START', font, green,425 , screen_height // 2 -100)
                draw_text('USE ARROW KEYS TO MOVE', font, green, (screen_width //2)-200 , screen_height // 2 -50)
                draw_text("YOU WILL BE QUIZZED EVERYTIME YOU SCORE AGAINST THE AI", font, green, (screen_width //2)-400 , screen_height // 2 -10)
                draw_text("YOU'LL RECIEVE 10 EXP FOR EVERY CORRECT ANSWER", font, green, (screen_width //2)-350 , screen_height // 2 + 20 )
                draw_text("BUT THE AI AND BALL WILL GET FASTER, SO BE READY!", font, green, (screen_width //2)-350 , screen_height // 2 + 40 )



                
            if winner == 1:
                #runs the miniquiz when player scores
                print("Running quiz page")
                quiz_status = True
                miniquiz()
                winner = 0
                
                
                   
                
            if winner == -1:
                #what happens when cpu scores
                draw_text('CPU SCORED!', font, white, 520, screen_height // 2 -100)
                draw_text('CLICK ANYWHERE TO START', font, white, (screen_width //2)-200 , screen_height // 2 -50)
                draw_text("YOU CAN DO BETTER THAN THAT!", font, white, (screen_width //2)-250 , screen_height // 2 -10)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and live_ball == False:
                live_ball = True
                pong.reset(screen_width - 700, screen_height // 2 + 50)#resets ball position
                cpu_paddle.y = pong.y#matches with the ball
                
                if pong.speed_x < max_speed:
                    pong.speed_x,pong.speed_y = -7,5 # resets ball speed

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #allows player to leave state
                run = False
                player_stats.exp_ai += exp
                if player_stats.highscore_ai < player_score:
                    player_stats.highscore_ai = player_score
                
                DB.update_user(player_stats)#updates database

               
                


        if speed_increase > 500:
            speed_increase = 0
            if pong.speed_x < 0:
                pong.speed_x -= 1
            if pong.speed_x > 0:
                pong.speed_x += 1
            if pong.speed_y < 0:
                pong.speed_y -= 1
            if pong.speed_y > 0:
                pong.speed_y += 1
        
        
            
           

            
        pygame.display.update()
    

#create paddles
player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)

#create pong ball
pong = ball(screen_width - 60, screen_height // 2 + 50)

print(f"questions {db_questions}")


    
    
    
   
   