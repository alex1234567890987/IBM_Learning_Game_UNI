"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import sqlite3
import time
import random
import math
from production.datascience_house.Window import pygame, window
from production.datascience_house.Plane import Plane
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Levels.CommonFunctions import showQuestions, image_bullet, image_bullet_auto_track, showPlane_setPlaneMoveRange, showScoreObtained, showEnemy, showRemainingEnemies, image_enemy_weapon, hitByEnemy_judge, hit_judge, end, gainScoreAndExp
from production.datascience_house.Levels.Pages.LevelThreePage import LevelThreePage
from production.datascience_house.Levels.Pages.PageText.CommonText import showDefeatedText


class LevelThree:
    def __init__(self):
        self.name = 'level three'
        self.gameIsOn = False  # Control of whether the player has entered the current level
        self.plane = Plane()
        self.plane.move_speed_improve()
        self.levelThreePage = LevelThreePage()
        self.enemies = []  # All enemies
        self.allEnemies = 60  # Total number of enemies
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
        self.levelThreePage.showBackground()

        if not self.questionAnswered:
            self.levelThreePage.showTextBeforeQuestions(self)
            if self.acceptChallenge:
                self.levelThreePage.showReminder1Text()
                if not self.levelThreePage.needToShowReminder1Text:
                    if self.needToDoQuestions:
                        pygame.mixer.music.pause()
                        showQuestions(self, 3)
                        if self.questionScore / 9 >= 0.7:
                            pygame.mixer.music.unpause()
                            self.questionAnswered = True
                            self.questionScore = 0
                        else:
                            pygame.mixer.music.unpause()
                            self.needToDoQuestions = False
                            self.questionScore = 0
                if not self.needToDoQuestions:
                    self.levelThreePage.showReminder2Text(self)
            elif self.refuseChallenge:
                self.gameIsOn = False
                self.refuseChallenge = False
                self.levelThreePage.needToShowReminder1Text = True
        else:
            self.levelThreePage.showTextBeforeGame()
            self.levelThreePage.showReminder4Text()

            if not self.levelThreePage.showText_beforeGame:
                if self.plane.HP_current > 0:
                    showPlane_setPlaneMoveRange(self.plane)
                    self.plane.showHealth()
                    self.showPlaneBullet()
                else:
                    if not (self.plane.position_x == 0 and self.plane.position_y == -100):
                        self.plane.position_x = 0
                        self.plane.position_y = -100
                    if self.levelThreePage.needToShowDefeatedText:
                        showDefeatedText(self.levelThreePage)
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
                        self.levelThreePage.needToShowDefeatedText = True

                if not self.levelThreePage.needToShowReminder4Text:
                    showScoreObtained(self)

                    # Up to fifteen enemies can exist simultaneously,
                    # and the total number of enemies and their movement speed are increased compared to the second level.
                    if self.enemiesPresent < self.allEnemies:
                        while len(self.enemies) < 15:
                            self.enemies.append(Enemy(random.randint(0, 1250), -28, random.randint(-4, 4), 0.25))
                            self.enemiesPresent += 1
                    if not self.enemies and self.plane.HP_current > 0:
                        end(self.levelThreePage, self, 12)

                    showEnemy(self)
                    showRemainingEnemies(self)
                    self.showEnemyBullet()
                    self.hitByEnemyBullet_judge()

                    hitByEnemy_judge(self)
                    hit_judge(self)  # To check whether a bullet has hit an enemy

    def showPlaneBullet(self):
        for bullet in self.plane.all_bullets:
            if bullet.position == 'right':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
                bullet.position_x -= bullet.speed_x
            elif bullet.position == 'middle':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
            elif bullet.position == 'left':
                window.blit(image_bullet, (bullet.position_x, bullet.position_y))
                bullet.position_y -= bullet.speed_default
                bullet.position_x += bullet.speed_x
            elif bullet.position == 'auto_track':
                window.blit(image_bullet_auto_track, (bullet.position_x, bullet.position_y))
                self.plane.auto_track(bullet, self.enemies)
            i = 0
            while i < len(self.plane.all_bullets):
                if self.plane.all_bullets[i].position_y < -100:
                    del self.plane.all_bullets[i]
                else:
                    i += 1

    def showEnemyBullet(self):
        for enemy in self.enemies:
            # In level three, the enemy fires a bullet every three seconds.
            if enemy.fire_StartTime == 0:
                enemy.fire_StartTime = time.time()
            enemy.fire_EndTime = time.time()
            enemy.fire_LastTime = enemy.fire_EndTime - enemy.fire_StartTime
            if enemy.fire_LastTime >= 3:
                enemy.shoot()
                enemy.fire_StartTime = 0
                enemy.fire_EndTime = 0
        for enemy in self.enemies:
            for bullet in enemy.all_bullets:
                window.blit(image_enemy_weapon, (bullet.position_x, bullet.position_y))
                bullet.position_x += bullet.speed_x
                bullet.position_y += bullet.speed_y
            i = 0
            while i < len(enemy.all_bullets):
                if enemy.all_bullets[i].position_y > 750:
                    del enemy.all_bullets[i]
                else:
                    i += 1

    def hitByEnemyBullet_judge(self):
        for enemy in self.enemies:
            for bullet in enemy.all_bullets:
                distance_plane_enemyBullet = math.sqrt(((bullet.position_x + 2) - (self.plane.position_x + 37)) ** 2 + (
                        (bullet.position_y + 2) - (self.plane.position_y + 27)) ** 2)
                if distance_plane_enemyBullet < 30:
                    self.plane.HP_current -= 10
                    self.plane.healthBar_width = (self.plane.HP_current / self.plane.HP_max) * self.plane.healthBar_width
                    if self.score > 0:
                        self.score -= 1
                    bullet.hitPlane = True
            i = 0
            while i < len(enemy.all_bullets):
                if enemy.all_bullets[i].hitPlane:
                    del enemy.all_bullets[i]
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
            self.acceptChallenge = False
            self.questionScore = 0
            self.score = 0
            self.questionAnswered = False
            self.levelThreePage.needToShowIntroduction1Text = True
            self.levelThreePage.needToShowButtons = True
            self.levelThreePage.needToShowReminder1Text = True
            self.levelThreePage.showText_beforeGame = True
            self.levelThreePage.needToShowReminder3Text = True
            self.levelThreePage.needToShowEndText = True
            self.levelThreePage.needToShowExitText = False
            with sqlite3.connect('general/db/AIGame.db') as connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE DATASCIENCELEVELSTATE SET levelOne = 'False', levelTwo = 'False' WHERE id = 1")
                connection.commit()
