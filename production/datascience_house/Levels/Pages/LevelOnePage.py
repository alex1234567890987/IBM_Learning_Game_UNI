"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import time
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.LevelOnePageText import LevelOnePageText


class LevelOnePage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/blue background.png')
        self.levelOnePageText = LevelOnePageText()

        # Introduction text Properties
        self.needToShowIntroductionText = True
        self.introduction_textStartTime = 0
        self.introduction_textEndTime = 0
        self.introduction_textLastTime = 0

        # Properties for reminder text (aircraft control)
        self.needToShowReminderText = False
        self.reminder_textStartTime = 0
        self.reminder_textEndTime = 0
        self.reminder_textLastTime = 0

        # Properties for reminder text (game over)
        self.needToShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # Properties for reminder text (exit level)
        self.needToShowExitText = False

        self.needToShowDefeatedText = True
        self.defeated_text_startTime = 0
        self.defeated_text_endTime = 0
        self.defeated_text_lastTime = 0

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showIntroductionText(self):
        if self.needToShowIntroductionText:
            if self.introduction_textStartTime == 0:
                self.introduction_textStartTime = time.time()
            self.introduction_textEndTime = time.time()
            self.introduction_textLastTime = self.introduction_textEndTime - self.introduction_textStartTime
            countdown_text_time_left = 12 - self.introduction_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (12 - self.introduction_textLastTime) >= 0:
                window.blit(self.levelOnePageText.introduction_textLine1, (280, 170))
                window.blit(self.levelOnePageText.introduction_textLine2, (280, 220))
                window.blit(self.levelOnePageText.introduction_textLine3, (280, 270))
                window.blit(self.levelOnePageText.introduction_textLine4, (280, 320))
                window.blit(self.levelOnePageText.introduction_textLine5, (565, 370))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowIntroductionText = False
                self.needToShowReminderText = True
                self.introduction_textStartTime = 0
                self.introduction_textEndTime = 0
                self.introduction_textLastTime = 0

    def showReminderText(self):
        if self.needToShowReminderText:
            if self.reminder_textStartTime == 0:
                self.reminder_textStartTime = time.time()
            self.reminder_textEndTime = time.time()
            self.reminder_textLastTime = self.reminder_textEndTime - self.reminder_textStartTime
            countdown_text_time_left = 7 - self.reminder_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (255, 255, 255))
            if (7 - self.reminder_textLastTime) >= 0:
                window.blit(self.levelOnePageText.reminder_textLine1, (325, 500))
                window.blit(self.levelOnePageText.reminder_textLine2, (520, 550))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminderText = False
                self.reminder_textStartTime = 0
                self.reminder_textEndTime = 0
                self.reminder_textLastTime = 0

    def showEndText(self):
        window.blit(self.levelOnePageText.end_textLine1, (215, 170))
        window.blit(self.levelOnePageText.end_textLine2, (215, 220))
        window.blit(self.levelOnePageText.end_textLine3, (215, 270))
        window.blit(self.levelOnePageText.end_textLine4, (215, 320))
        window.blit(self.levelOnePageText.end_textLine5, (450, 370))

    def showExitText(self):
        window.blit(self.levelOnePageText.exit_textLine1, (314, 315))
        window.blit(self.levelOnePageText.exit_textLine2, (337, 365))
