"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import random
import sqlite3

from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Window import window
from production.datascience_house.Levels.CommonFunctions import image_bullet, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, showRemainingEnemies, hitByEnemy_judge, hit_judge, end, gainScoreAndExp
from production.datascience_house.Levels.Pages.LevelOnePage import LevelOnePage
from production.datascience_house.Levels.Pages.PageText.CommonText import showDefeatedText


class LevelOne:
    def __init__(self):
        self.name = 'level one'
        self.passed = 'False'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.levelOnePage = LevelOnePage()
        self.enemies = []  # All enemies
        self.allEnemies = 15  # Total number of enemies
        self.enemiesPresent = 0  # Enemies that have appeared
        self.enemyDestroyed = 0
        self.score = 0  # Score

    # Call this method after the start of the current level/game.
    def loadStuff(self):
        self.levelOnePage.showBackground()
        self.levelOnePage.showIntroductionText()
        self.levelOnePage.showReminderText()

        if not self.levelOnePage.needToShowIntroductionText:
            if self.plane.HP_current > 0:
                showPlane_setPlaneMoveRange(self.plane)
                self.plane.showHealth()
                self.showBullet()
            else:
                if not (self.plane.position_x == 0 and self.plane.position_y == -100):
                    self.plane.position_x = 0
                    self.plane.position_y = -100
                if self.levelOnePage.needToShowDefeatedText:
                    showDefeatedText(self.levelOnePage)
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
                    self.levelOnePage.needToShowIntroductionText = True
                    self.levelOnePage.showText_beforeGame = True
                    self.levelOnePage.needToShowDefeatedText = True

            if not self.levelOnePage.needToShowReminderText:
                showScoreObtained(self)

                # Up to five enemies can exist simultaneously.
                if self.enemiesPresent < self.allEnemies:
                    while len(self.enemies) < 5:
                        self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-2, -2), 0.15))
                        self.enemiesPresent += 1
                # If no enemies, end the game
                if not self.enemies and self.plane.HP_current > 0:
                    end(self.levelOnePage, self, 12)

                showEnemy(self)
                showRemainingEnemies(self)

                hitByEnemy_judge(self)
                hit_judge(self)  # To check whether a bullet has hit an enemy

    def showBullet(self):
        for bullet in self.plane.all_bullets:
            window.blit(image_bullet, (bullet.position_x, bullet.position_y))
            bullet.position_y -= bullet.speed_default
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
            self.levelOnePage.needToShowIntroductionText = True
            self.levelOnePage.needToShowEndText = True
            self.levelOnePage.needToShowExitText = False
            self.passed = 'True'
            with sqlite3.connect('general/db/AIGame.db') as connection:
                cursor = connection.cursor()
                cursor.execute(
                    f"UPDATE DATASCIENCELEVELSTATE SET levelOne = {self.passed} WHERE id = 1")
                connection.commit()
