"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import pygame, window, font
from production.datascience_house.Levels.Pages.PageText.MainPageText import MainPageText


class MainPage:
    def __init__(self):
        self.needToShowIntroductionText = True
        self.needToShowButtons = True
        self.needToShowReminderText = False
        self.needToShowButtons_notPassed = False

        self.image_background = pygame.image.load('datascience_house/images/blue-pink-red background.png')
        self.mainPageText = MainPageText()

        # The button to enter the first level
        self.button_levelOne = pygame.Rect(545, 510, 245, 40)
        self.button_levelOne.center = (window.get_width()/2, window.get_height()/2 + 100)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelOne)
        self.text_levelOne = font.render("Click here to start level one!", True, (255, 255, 255))
        self.text_rect_levelOne = self.text_levelOne.get_rect(center=self.button_levelOne.center)

        # The button to enter the second level
        self.button_levelTwo = pygame.Rect(545, 510, 245, 40)
        self.button_levelTwo.midtop = (window.get_width() / 2, self.button_levelOne.midbottom[1] + 16)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelTwo)
        self.text_levelTwo = font.render("Click here to start level two!", True, (255, 255, 255))
        self.text_rect_levelTwo = self.text_levelTwo.get_rect(center=self.button_levelTwo.center)

        # The button to enter the third level
        self.button_levelThree = pygame.Rect(545, 560, 245, 40)
        self.button_levelThree.midtop = (window.get_width() / 2, self.button_levelTwo.midbottom[1] + 16)
        pygame.draw.rect(window, (0, 255, 0), self.button_levelThree)
        self.text_levelThree = font.render("Click here to start level three!", True, (255, 255, 255))
        self.text_rect_levelThree = self.text_levelThree.get_rect(center=self.button_levelThree.center)

        self.goBack = False

        # The button to go back
        self.button_goBack = pygame.Rect(1195, 15, 60, 20)
        pygame.draw.rect(window, (0, 255, 0), self.button_goBack)
        self.text_goBack = font.render("Back", True, (255, 255, 255))
        self.text_rect_goBack = self.text_goBack.get_rect(center=self.button_goBack.center)

        # The button to go back if previous level was not passed
        self.button_goBack_notPassed = pygame.Rect(525, 370, 230, 20)
        pygame.draw.rect(window, (0, 255, 0), self.button_goBack_notPassed)
        self.text_goBack_notPassed = font.render("Click here to go Back", True, (165, 0, 42))
        self.text_rect_goBack_notPassed = self.text_goBack_notPassed.get_rect(center=self.button_goBack_notPassed.center)

    def showBackground(self):
        window.blit(self.image_background, (0, 0))

    def showIntroductionTextLine(self):
        if self.needToShowIntroductionText:
            window.blit(self.mainPageText.introduction_textLine1, (window.get_width()/2 - self.mainPageText.introduction_textLine1.get_width()/2, window.get_height()/4 - self.mainPageText.introduction_textLine1.get_height()/2))
            window.blit(self.mainPageText.introduction_textLine2, (window.get_width() / 2 - self.mainPageText.introduction_textLine2.get_width() / 2, window.get_height() / 4 - self.mainPageText.introduction_textLine2.get_height() / 2 + 50))
            window.blit(self.mainPageText.introduction_textLine3, (window.get_width() / 2 - self.mainPageText.introduction_textLine3.get_width() / 2, window.get_height() / 4 - self.mainPageText.introduction_textLine3.get_height() / 2 + 100))
            window.blit(self.mainPageText.introduction_textLine4, (window.get_width()/2 - self.mainPageText.introduction_textLine4.get_width()/2, window.get_height()/4 - self.mainPageText.introduction_textLine4.get_height()/2 + 150))
            window.blit(self.mainPageText.introduction_textLine5, (window.get_width()/2 - self.mainPageText.introduction_textLine5.get_width()/2, window.get_height()/4 - self.mainPageText.introduction_textLine5.get_height()/2 + 200))

    def showButtons(self):
        # Players need to complete the previous levels before they can proceed to the next levels
        if self.needToShowButtons:
            window.blit(self.text_levelOne, self.text_rect_levelOne)
            window.blit(self.text_levelTwo, self.text_rect_levelTwo)
            window.blit(self.text_levelThree, self.text_rect_levelThree)
            window.blit(self.text_goBack, self.text_rect_goBack)

    def showReminderText(self):
        if self.needToShowReminderText:
            window.blit(self.mainPageText.reminder_textLine, (385, 320))

    def showButtons_notPassed(self):
        if self.needToShowButtons_notPassed:
            window.blit(self.text_goBack_notPassed, self.text_rect_goBack_notPassed)
