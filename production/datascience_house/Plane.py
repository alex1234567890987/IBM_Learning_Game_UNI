"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import math
from production.datascience_house.Window import pygame, window


class Plane:
    def __init__(self):
        # health points of the aircraft
        self.HP_max = 100
        self.HP_current = 100
        self.healthBar_width = 42

        # The position of the aircraft
        self.position_x = 0
        self.position_y = 675

        # The speed and numerical value of the aircraft
        self.speed_x = 0  # level speed
        self.speed_y = 0  # vertical speed
        self.velocity1 = 3  # velocity size (one direction)
        self.velocity2 = -3  # velocity size (one direction)

        # All bullets fired by the aircraft
        self.all_bullets = []

    # Displaying the life points of the aircraft
    def showHealth(self):
        pygame.draw.rect(window, (0, 255, 0), (self.position_x, self.position_y - 7, self.healthBar_width, 5))

    # Upgrading spacecraft performance to increase speed.
    def move_speed_improve(self):
        self.velocity1 = 5.5
        self.velocity2 = -5.5

    # Upgrading spacecraft performance to enable bullets to automatically track enemies.
    @staticmethod
    def auto_track(bullet, enemies):
        if enemies:
            distances = []
            for enemy in enemies:
                distance = math.sqrt(((bullet.position_x + 5) - (enemy.position_x + 15)) ** 2 + (
                        bullet.position_y - enemy.position_y) ** 2)
                distances.append(distance)
            distance_min = min(distances)  # The nearest enemy to the bullet (Euclidean distance).
            indices = [i for i, d in enumerate(distances) if d == distance_min]
            enemy = enemies[indices[0]]
            bullet_level_distance_enemy = bullet.position_x - enemy.position_x
            bullet_vertical_distance_enemy = bullet.position_y - enemy.position_y

            if 1260 < abs(bullet_level_distance_enemy):
                bullet.speed_x = 9.2
            elif 1230 < abs(bullet_level_distance_enemy) <= 1260:
                bullet.speed_x = 9
            elif 1200 < abs(bullet_level_distance_enemy) <= 1230:
                bullet.speed_x = 8.8
            elif 1170 < abs(bullet_level_distance_enemy) <= 1200:
                bullet.speed_x = 8.6
            elif 1140 < abs(bullet_level_distance_enemy) <= 1170:
                bullet.speed_x = 8.4
            elif 1110 < abs(bullet_level_distance_enemy) <= 1140:
                bullet.speed_x = 8.2
            elif 1080 < abs(bullet_level_distance_enemy) <= 1110:
                bullet.speed_x = 8
            elif 1050 < abs(bullet_level_distance_enemy) <= 1080:
                bullet.speed_x = 7.8
            elif 1020 < abs(bullet_level_distance_enemy) <= 1050:
                bullet.speed_x = 7.6
            elif 990 < abs(bullet_level_distance_enemy) <= 1020:
                bullet.speed_x = 7.4
            elif 960 < abs(bullet_level_distance_enemy) <= 990:
                bullet.speed_x = 7.2
            elif 930 < abs(bullet_level_distance_enemy) <= 960:
                bullet.speed_x = 7
            elif 900 < abs(bullet_level_distance_enemy) <= 930:
                bullet.speed_x = 6.8
            elif 870 < abs(bullet_level_distance_enemy) <= 900:
                bullet.speed_x = 6.6
            elif 840 < abs(bullet_level_distance_enemy) <= 870:
                bullet.speed_x = 6.4
            elif 810 < abs(bullet_level_distance_enemy) <= 840:
                bullet.speed_x = 6.2
            elif 780 < abs(bullet_level_distance_enemy) <= 810:
                bullet.speed_x = 6
            elif 750 < abs(bullet_level_distance_enemy) <= 780:
                bullet.speed_x = 5.8
            elif 720 < abs(bullet_level_distance_enemy) <= 750:
                bullet.speed_x = 5.6
            elif 690 < abs(bullet_level_distance_enemy) <= 720:
                bullet.speed_x = 5.4
            elif 660 < abs(bullet_level_distance_enemy) <= 690:
                bullet.speed_x = 5.2
            elif 630 < abs(bullet_level_distance_enemy) <= 660:
                bullet.speed_x = 5
            elif 600 < abs(bullet_level_distance_enemy) <= 630:
                bullet.speed_x = 4.8
            elif 570 < abs(bullet_level_distance_enemy) <= 600:
                bullet.speed_x = 4.6
            elif 540 < abs(bullet_level_distance_enemy) <= 570:
                bullet.speed_x = 4.4
            elif 510 < abs(bullet_level_distance_enemy) <= 540:
                bullet.speed_x = 4.2
            elif 480 < abs(bullet_level_distance_enemy) <= 510:
                bullet.speed_x = 4
            elif 450 < abs(bullet_level_distance_enemy) <= 480:
                bullet.speed_x = 3.8
            elif 420 < abs(bullet_level_distance_enemy) <= 450:
                bullet.speed_x = 3.6
            elif 390 < abs(bullet_level_distance_enemy) <= 420:
                bullet.speed_x = 3.4
            elif 360 < abs(bullet_level_distance_enemy) <= 390:
                bullet.speed_x = 3.2
            elif 330 < abs(bullet_level_distance_enemy) <= 360:
                bullet.speed_x = 3
            elif 300 < abs(bullet_level_distance_enemy) <= 330:
                bullet.speed_x = 2.8
            elif 270 < abs(bullet_level_distance_enemy) <= 300:
                bullet.speed_x = 2.6
            elif 240 < abs(bullet_level_distance_enemy) <= 270:
                bullet.speed_x = 2.4
            elif 210 < abs(bullet_level_distance_enemy) <= 240:
                bullet.speed_x = 2.2
            elif 180 < abs(bullet_level_distance_enemy) <= 210:
                bullet.speed_x = 2
            elif 150 < abs(bullet_level_distance_enemy) <= 180:
                bullet.speed_x = 1.8
            elif 120 < abs(bullet_level_distance_enemy) <= 150:
                bullet.speed_x = 1.6
            elif 90 < abs(bullet_level_distance_enemy) <= 120:
                bullet.speed_x = 1.4
            elif 60 < abs(bullet_level_distance_enemy) <= 90:
                bullet.speed_x = 1.2
            elif 30 < abs(bullet_level_distance_enemy) <= 60:
                bullet.speed_x = 0.8
            elif abs(bullet_level_distance_enemy) <= 30:
                bullet.speed_x = 0.6

            if 690 < abs(bullet_vertical_distance_enemy):
                bullet.speed_y = 5.4
            elif 660 < abs(bullet_vertical_distance_enemy) <= 690:
                bullet.speed_y = 5.2
            elif 630 < abs(bullet_vertical_distance_enemy) <= 660:
                bullet.speed_y = 5
            elif 600 < abs(bullet_vertical_distance_enemy) <= 630:
                bullet.speed_y = 4.8
            elif 570 < abs(bullet_vertical_distance_enemy) <= 600:
                bullet.speed_y = 4.6
            elif 540 < abs(bullet_vertical_distance_enemy) <= 570:
                bullet.speed_y = 4.4
            elif 510 < abs(bullet_vertical_distance_enemy) <= 540:
                bullet.speed_y = 4.2
            elif 480 < abs(bullet_vertical_distance_enemy) <= 510:
                bullet.speed_y = 4
            elif 450 < abs(bullet_vertical_distance_enemy) <= 480:
                bullet.speed_y = 3.8
            elif 420 < abs(bullet_vertical_distance_enemy) <= 450:
                bullet.speed_y = 3.6
            elif 390 < abs(bullet_vertical_distance_enemy) <= 420:
                bullet.speed_y = 3.4
            elif 360 < abs(bullet_vertical_distance_enemy) <= 390:
                bullet.speed_y = 3.2
            elif 330 < abs(bullet_vertical_distance_enemy) <= 360:
                bullet.speed_y = 3
            elif 300 < abs(bullet_vertical_distance_enemy) <= 330:
                bullet.speed_y = 2.8
            elif 270 < abs(bullet_vertical_distance_enemy) <= 300:
                bullet.speed_y = 2.6
            elif 240 < abs(bullet_vertical_distance_enemy) <= 270:
                bullet.speed_y = 2.4
            elif 210 < abs(bullet_vertical_distance_enemy) <= 240:
                bullet.speed_y = 2.2
            elif 180 < abs(bullet_vertical_distance_enemy) <= 210:
                bullet.speed_y = 2
            elif 150 < abs(bullet_vertical_distance_enemy) <= 180:
                bullet.speed_y = 1.8
            elif 120 < abs(bullet_vertical_distance_enemy) <= 150:
                bullet.speed_y = 1.6
            elif 90 < abs(bullet_vertical_distance_enemy) <= 120:
                bullet.speed_y = 1.4
            elif 60 < abs(bullet_vertical_distance_enemy) <= 90:
                bullet.speed_y = 1.2
            elif 30 < abs(bullet_vertical_distance_enemy) <= 60:
                bullet.speed_y = 1
            elif abs(bullet_vertical_distance_enemy) <= 30:
                bullet.speed_y = 0.8

            # If the bullet is on the left or right of the enemy.
            if bullet_level_distance_enemy < 0:
                bullet.position_x += bullet.speed_x
            elif bullet_level_distance_enemy > 0:
                bullet.position_x -= bullet.speed_x

            # If the bullet is above or below the enemy.
            if bullet_vertical_distance_enemy < 0:
                bullet.position_y += bullet.speed_y
            elif bullet_vertical_distance_enemy > 0:
                bullet.position_y -= bullet.speed_y
        else:
            bullet.position_y -= bullet.speed_default

    def shoot(self, position_x, position_y):
        new_bullet = Bullet(position_x, position_y)
        self.all_bullets.append(new_bullet)

    def shoot_threeBullets(self, position_x, position_y):
        new_bullet1 = Bullet(position_x, position_y, 2, 'right')
        new_bullet2 = Bullet(position_x, position_y, 2, 'middle')
        new_bullet3 = Bullet(position_x, position_y, 2, 'left')
        self.all_bullets.append(new_bullet1)
        self.all_bullets.append(new_bullet2)
        self.all_bullets.append(new_bullet3)

    def shoot_auto_track(self, position_x, position_y):
        new_bullet = Bullet(position_x, position_y, 0, 'auto_track')
        self.all_bullets.append(new_bullet)


class Bullet:
    def __init__(self, position_x, position_y, speed_x=0, position=None):
        # The position of the bullet
        self.position_x = position_x
        self.position_y = position_y

        # The speed of the bullet
        self.speed_x = speed_x
        self.speed_y = 0
        self.speed_default = 10

        # The movement direction of the bullet
        self.position = position

        # Whether the bullet hit the enemy
        self.hitEnemy = False
