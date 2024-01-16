"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import random
import sqlite3

from production.datascience_house.Window import pygame, window
from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Levels.CommonFunctions import showQuestions, image_bullet, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, showRemainingEnemies, hitByEnemy_judge, hit_judge, end, gainScoreAndExp
from production.datascience_house.Levels.Pages.LevelTwoPage import LevelTwoPage
from production.datascience_house.Levels.Pages.PageText.CommonText import showDefeatedText


class LevelTwo:
    def __init__(self):
        self.name = 'level two'
        self.passed = 'False'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.levelTwoPage = LevelTwoPage()
        self.enemies = []  # All enemies
        self.allEnemies = 30  # Total number of enemies
        self.enemiesPresent = 0  # Enemies that have appeared
        self.enemyDestroyed = 0
        self.score = 0  # Score
        self.acceptChallenge = False  # Control of whether the player accepts answering questions
        self.refuseChallenge = False  # Control of whether the player refuses answering questions
        self.questionScore = 0  # The player's score in answering questions
        self.questionAnswered = False  # Control of whether the player has answered questions
        self.needToDoQuestions = True

    # Call this method after the start of the current level/game.
    def loadStuff(self):
        self.levelTwoPage.showBackground()

        if not self.questionAnswered:
            self.levelTwoPage.showTextBeforeQuestions(self)
            if self.acceptChallenge:
                self.levelTwoPage.showReminder1Text()
                if not self.levelTwoPage.needToShowReminder1Text:
                    if self.needToDoQuestions:
                        pygame.mixer.music.pause()
                        showQuestions(self, 2)
                        if self.questionScore / 6 >= 0.7:
                            pygame.mixer.music.unpause()
                            self.questionAnswered = True
                            self.questionScore = 0
                        else:
                            pygame.mixer.music.unpause()
                            self.needToDoQuestions = False
                            self.questionScore = 0
                if not self.needToDoQuestions:
                    self.levelTwoPage.showReminder2Text(self)
            elif self.refuseChallenge:
                self.gameIsOn = False
                self.refuseChallenge = False
                self.levelTwoPage.needToShowReminder1Text = True
        else:
            self.levelTwoPage.showTextBeforeGame()
            self.levelTwoPage.showReminder4Text()

            if not self.levelTwoPage.showText_beforeGame:
                if self.plane.HP_current > 0:
                    showPlane_setPlaneMoveRange(self.plane)
                    self.plane.showHealth()
                    self.showBullet()
                else:
                    if not (self.plane.position_x == 0 and self.plane.position_y == -100):
                        self.plane.position_x = 0
                        self.plane.position_y = -100
                    if self.levelTwoPage.needToShowDefeatedText:
                        showDefeatedText(self.levelTwoPage)
                    else:
                        self.gameIsOn = False
                        self.plane.HP_current = 100
                        self.plane.healthBar_width = 42
                        i = 0
                        while self.plane.all_bullets:
                            del self.plane.all_bullets[i]
                        while self.enemies:
                            del self.enemies[i]
                        self.plane.position_x, self.plane.position_y = 0, 675
                        self.plane.speed_x, self.plane.speed_y = 0, 0
                        self.enemiesPresent = 0
                        self.enemyDestroyed = 0
                        self.score = 0
                        self.levelTwoPage.needToShowDefeatedText = True

                if not self.levelTwoPage.needToShowReminder4Text:
                    showScoreObtained(self)

                    # Up to ten enemies can exist simultaneously,
                    # and the total number of enemies and their movement speed are increased compared to the first level.
                    if self.enemiesPresent < self.allEnemies:
                        while len(self.enemies) < 10:
                            self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-3, 3), 0.23))
                            self.enemiesPresent += 1
                    if not self.enemies and self.plane.HP_current > 0:
                        end(self.levelTwoPage, self, 12)

                    showEnemy(self)
                    showRemainingEnemies(self)

                    hitByEnemy_judge(self)
                    hit_judge(self)  # To check whether a bullet has hit an enemy

    def showBullet(self):
        for bullet in self.plane.all_bullets:
            window.blit(image_bullet, (bullet.position_x, bullet.position_y))
            if bullet.position == 'right':
                bullet.position_y -= bullet.speed_default
                bullet.position_x -= bullet.speed_x
            elif bullet.position == 'middle':
                bullet.position_y -= bullet.speed_default
            elif bullet.position == 'left':
                bullet.position_y -= bullet.speed_default
                bullet.position_x += bullet.speed_x
        i = 0
        while i < len(self.plane.all_bullets):
            if self.plane.all_bullets[i].position_y < -100:
                del self.plane.all_bullets[i]
            else:
                i += 1

    # To reset all the states of the level when the player exits,
    # call this method to ensure that the player can restart the level without encountering errors.
    def finish(self):
        if 1150 > self.plane.position_x > 1070 and 60 < self.plane.position_y < 160:
            gainScoreAndExp(self)
            self.gameIsOn = False
            self.plane.position_x, self.plane.position_y = 0, 675
            self.plane.speed_x, self.plane.speed_y = 0, 0
            self.plane.HP_current = 100
            self.plane.healthBar_width = 42
            self.enemiesPresent = 0
            self.enemyDestroyed = 0
            self.score = 0
            self.acceptChallenge = False
            self.questionScore = 0
            self.questionAnswered = False
            self.levelTwoPage.needToShowIntroduction1Text = True
            self.levelTwoPage.needToShowButtons = True
            self.levelTwoPage.needToShowReminder1Text = True
            self.levelTwoPage.showText_beforeGame = True
            self.levelTwoPage.needToShowReminder3Text = True
            self.levelTwoPage.needToShowEndText = True
            self.levelTwoPage.needToShowExitText = False
            self.passed = 'True'
            with sqlite3.connect('general/db/AIGame.db') as connection:
                cursor = connection.cursor()
                cursor.execute(
                    f"UPDATE DATASCIENCELEVELSTATE SET levelTwo = {self.passed} WHERE id = 1")
                connection.commit()
