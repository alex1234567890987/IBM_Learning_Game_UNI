"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import time
from production.datascience_house.Window import window, font

defeated_text_textLine1 = font.render(
    "Unfortunately you have been defeated, you are",
    True, (255, 255, 255))
defeated_text_textLine2 = font.render(
    " about to be sent out of this interstellar.",
    True, (255, 255, 255))
defeated_text_textLine3 = font.render(
    "Welcome to try again.",
    True, (255, 255, 255))


def showDefeatedText(levelPage):
    if levelPage.defeated_text_startTime == 0:
        levelPage.defeated_text_startTime = time.time()
    levelPage.defeated_text_endTime = time.time()
    levelPage.defeated_text_lastTime = levelPage.defeated_text_endTime - levelPage.defeated_text_startTime
    countdown_text_time_left = 7 - levelPage.defeated_text_lastTime
    countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
    if (7 - levelPage.defeated_text_lastTime) >= 0:
        window.blit(defeated_text_textLine1, (380, 280))
        window.blit(defeated_text_textLine2, (380, 330))
        window.blit(defeated_text_textLine3, (530, 380))
        window.blit(countdown_text, (10, 690))
    else:
        levelPage.needToShowDefeatedText = False
        levelPage.defeated_text_startTime = 0
        levelPage.defeated_text_endTime = 0
        levelPage.defeated_text_lastTime = 0
