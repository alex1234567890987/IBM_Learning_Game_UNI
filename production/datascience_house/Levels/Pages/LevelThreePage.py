"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import time
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.LevelThreePageText import LevelThreePageText


class LevelThreePage:
    def __init__(self):
        self.image_background = pygame.image.load('datascience_house/images/green background.png')
        self.levelThreePageText = LevelThreePageText()

        # The display attributes for the introduction text when the player hasn't answered the question
        self.needToShowIntroduction1Text = True

        # The display attributes for the button options
        self.needToShowButtons = True

        # The display attributes for the reminder text after the player selects an answer
        self.needToShowReminder1Text = True
        self.reminder1_textStartTime = 0
        self.reminder1_textEndTime = 0
        self.reminder1_textLastTime = 0

        # The display attributes for the reminder text when the player fails to answer a questio
        self.reminder2_textStartTime = 0
        self.reminder2_textEndTime = 0
        self.reminder2_textLastTime = 0

        self.showText_beforeGame = True

        # The display attributes for the reminder text when the player successfully answers a question
        self.needToShowReminder3Text = True
        self.reminder3_textStartTime = 0
        self.reminder3_textEndTime = 0
        self.reminder3_textLastTime = 0

        # The display attributes for the introduction text when the player has already answered a question
        self.needToShowIntroduction2Text = False
        self.introduction2_textStartTime = 0
        self.introduction2_textEndTime = 0
        self.introduction2_textLastTime = 0

        # The display attributes for the reminder text about the aircraft's performance
        self.needToShowReminder4Text = False
        self.reminder4_textStartTime = 0
        self.reminder4_textEndTime = 0
        self.reminder4_textLastTime = 0

        # The display attributes for the reminder text when the game is over
        self.needToShowEndText = True
        self.end_textStartTime = 0
        self.end_textEndTime = 0
        self.end_textLastTime = 0

        # The display attributes for the reminder text when exiting the level
        self.needToShowExitText = False

        self.needToShowDefeatedText = True
        self.defeated_text_startTime = 0
        self.defeated_text_endTime = 0
        self.defeated_text_lastTime = 0

        # The button for the player to choose to answer the questions
        self.button_acceptChallenge = pygame.Rect(375, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_acceptChallenge)
        self.text_acceptChallenge = font.render("Click here to start!", True, (125, 125, 125))
        self.text_rect_acceptChallenge = self.text_acceptChallenge.get_rect(center=self.button_acceptChallenge.center)

        # The button for the player to refuse answering the questions
        self.button_refuseChallenge = pygame.Rect(685, 500, 210, 40)
        pygame.draw.rect(window, (0, 255, 0), self.button_refuseChallenge)
        self.text_refuseChallenge = font.render("Click here to go back!", True, (125, 125, 125))
        self.text_rect_refuseChallenge = self.text_refuseChallenge.get_rect(center=self.button_refuseChallenge.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showTextBeforeQuestions(self, levelTwo):
        if not levelTwo.acceptChallenge:
            self.showIntroduction1Text()
            self.showButtons()

    def showIntroduction1Text(self):
        if self.needToShowIntroduction1Text:
            window.blit(self.levelThreePageText.introduction1_textLine1, (280, 170))
            window.blit(self.levelThreePageText.introduction1_textLine2, (280, 220))
            window.blit(self.levelThreePageText.introduction1_textLine3, (280, 270))
            window.blit(self.levelThreePageText.introduction1_textLine4, (280, 320))
            window.blit(self.levelThreePageText.introduction1_textLine5, (280, 370))
            window.blit(self.levelThreePageText.introduction1_textLine6, (280, 420))

    def showButtons(self):
        if self.needToShowButtons:
            window.blit(self.text_acceptChallenge, self.text_rect_acceptChallenge)
            window.blit(self.text_refuseChallenge, self.text_rect_refuseChallenge)

    def showReminder1Text(self):
        if self.needToShowReminder1Text:
            if self.reminder1_textStartTime == 0:
                self.reminder1_textStartTime = time.time()
            self.reminder1_textEndTime = time.time()
            self.reminder1_textLastTime = self.reminder1_textEndTime - self.reminder1_textStartTime
            countdown_text_time_left = 7 - self.reminder1_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (125, 125, 125))
            if (7 - self.reminder1_textLastTime) >= 0:
                window.blit(self.levelThreePageText.reminder1_textLine1,
                            (380, 290))
                window.blit(self.levelThreePageText.reminder1_textLine2,
                            (380, 340))
                window.blit(self.levelThreePageText.reminder1_textLine3,
                            (563, 390))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder1Text = False
                self.reminder1_textStartTime = 0
                self.reminder1_textEndTime = 0
                self.reminder1_textLastTime = 0

    def showReminder2Text(self, levelThree):
        if self.reminder2_textStartTime == 0:
            self.reminder2_textStartTime = time.time()
        self.reminder2_textEndTime = time.time()
        self.reminder2_textLastTime = self.reminder2_textEndTime - self.reminder2_textStartTime
        countdown_text_time_left = 7 - self.reminder2_textLastTime
        countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (125, 125, 125))
        if (7 - self.reminder2_textLastTime) >= 0:
            window.blit(self.levelThreePageText.reminder2_textLine1,
                        (380, 270))
            window.blit(self.levelThreePageText.reminder2_textLine2,
                        (380, 320))
            window.blit(self.levelThreePageText.reminder2_textLine3, (380, 370))
            window.blit(countdown_text, (10, 690))
        else:
            self.needToShowIntroduction1Text = True
            self.needToShowButtons = True
            levelThree.acceptChallenge = False
            levelThree.needToDoQuestions = True
            self.reminder2_textStartTime = 0
            self.reminder2_textEndTime = 0
            self.reminder2_textLastTime = 0

    def showTextBeforeGame(self):
        self.showReminder3Text()
        self.showIntroduction2Text()

    def showReminder3Text(self):
        if self.needToShowReminder3Text:
            if self.reminder3_textStartTime == 0:
                self.reminder3_textStartTime = time.time()
            self.reminder3_textEndTime = time.time()
            self.reminder3_textLastTime = self.reminder3_textEndTime - self.reminder3_textStartTime
            countdown_text_time_left = 7 - self.reminder3_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (125, 125, 125))
            if (7 - self.reminder3_textLastTime) >= 0:
                window.blit(self.levelThreePageText.reminder3_textLine1,
                            (260, 230))
                window.blit(self.levelThreePageText.reminder3_textLine2,
                            (260, 280))
                window.blit(self.levelThreePageText.reminder3_textLine3,
                            (260, 330))
                window.blit(self.levelThreePageText.reminder3_textLine4,
                            (260, 370))
                window.blit(self.levelThreePageText.reminder3_textLine5,
                            (260, 420))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder3Text = False
                self.needToShowIntroduction2Text = True
                self.reminder3_textStartTime = 0
                self.reminder3_textEndTime = 0
                self.reminder3_textLastTime = 0

    def showIntroduction2Text(self):
        if self.needToShowIntroduction2Text:
            if self.introduction2_textStartTime == 0:
                self.introduction2_textStartTime = time.time()
            self.introduction2_textEndTime = time.time()
            self.introduction2_textLastTime = self.introduction2_textEndTime - self.introduction2_textStartTime
            countdown_text_time_left = 12 - self.introduction2_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (125, 125, 125))
            if (12 - self.introduction2_textLastTime) >= 0:
                window.blit(self.levelThreePageText.introduction2_textLine1, (300, 160))
                window.blit(self.levelThreePageText.introduction2_textLine2, (300, 210))
                window.blit(self.levelThreePageText.introduction2_textLine3, (300, 260))
                window.blit(self.levelThreePageText.introduction2_textLine4, (300, 310))
                window.blit(self.levelThreePageText.introduction2_textLine5, (300, 360))
                window.blit(self.levelThreePageText.introduction2_textLine6, (300, 410))
                window.blit(self.levelThreePageText.introduction2_textLine7, (300, 460))
                window.blit(self.levelThreePageText.introduction2_textLine8, (527, 510))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowIntroduction2Text = False
                self.needToShowReminder4Text = True
                self.showText_beforeGame = False
                self.introduction2_textStartTime = 0
                self.introduction2_textEndTime = 0
                self.introduction2_textLastTime = 0

    def showReminder4Text(self):
        if self.needToShowReminder4Text:
            if self.reminder4_textStartTime == 0:
                self.reminder4_textStartTime = time.time()
            self.reminder4_textEndTime = time.time()
            self.reminder4_textLastTime = self.reminder4_textEndTime - self.reminder4_textStartTime
            countdown_text_time_left = 7 - self.reminder4_textLastTime
            countdown_text = font.render("Time left: " + str(int(countdown_text_time_left)), True, (125, 125, 125))
            if (7 - self.reminder4_textLastTime) >= 0:
                window.blit(self.levelThreePageText.reminder4_textLine1,
                            (160, 500))
                window.blit(self.levelThreePageText.reminder4_textLine2,
                            (430, 550))
                window.blit(countdown_text, (10, 690))
            else:
                self.needToShowReminder4Text = False
                self.reminder4_textStartTime = 0
                self.reminder4_textEndTime = 0
                self.reminder4_textLastTime = 0

    def showEndText(self):
        window.blit(self.levelThreePageText.end_textLine1, (365, 250))
        window.blit(self.levelThreePageText.end_textLine2, (365, 300))
        window.blit(self.levelThreePageText.end_textLine3, (365, 350))
        window.blit(self.levelThreePageText.end_textLine4, (365, 400))

    def showExitText(self):
        window.blit(self.levelThreePageText.exit_textLine1, (314, 315))
        window.blit(self.levelThreePageText.exit_textLine2, (410, 365))
