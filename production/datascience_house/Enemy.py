"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
import random


class Enemy:
    def __init__(self, position_x, position_y, speed_x, speed_y):
        # The position of the enemy
        self.position_x = position_x
        self.position_y = position_y

        # The speed of the enemy
        self.speed_x = speed_x
        self.speed_y = speed_y

        # All bullets fired by the enemy
        self.all_bullets = []

        # Controlling the frequency of enemy bullet firing
        self.fire_StartTime = 0
        self.fire_EndTime = 0
        self.fire_LastTime = 0

        # Whether the enemy is hit by the bullets (from the aircraft)
        self.hitByBullet = False

        # Whether the enemy collides with the aircraft
        self.hitByPlane = False

    def shoot(self):
        new_bullet = Bullet(self.position_x, self.position_y, random.randint(-2, 2))
        self.all_bullets.append(new_bullet)


class Bullet:
    def __init__(self, position_x, position_y, speed_x):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = 4
        self.hitPlane = False
