import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
import unittest
from production.datascience_house.Levels.CommonFunctions import showPlane_setPlaneMoveRange, showEnemy, hitByEnemy_judge, hit_judge
from production.datascience_house.Plane import Plane, Bullet
from production.datascience_house.Enemy import Enemy
from production.datascience_house.Levels.LevelOne import LevelOne


class MinigameTest(unittest.TestCase):
    def test_showPlane(self):
        # Test whether the plane's position has changed correctly when it gets a speed
        plane = Plane()
        plane.speed_x = 3
        plane.speed_y = -4
        showPlane_setPlaneMoveRange(plane)
        self.assertEqual(plane.position_x, 3)
        self.assertEqual(plane.position_y, 671)

    def test_showEnemy(self):
        # Test whether the enemy's position has changed correctly when it gets a speed
        levelOne = LevelOne()
        enemy = Enemy(0, 100, 3, 4)
        levelOne.enemies.append(enemy)
        showEnemy(levelOne)
        self.assertEqual(enemy.position_x, 3)
        self.assertEqual(enemy.position_y, 104)

    def test_hitByEnemy_judge(self):
        # Test whether an enemy is removed from the list of enemies when it hits the plane
        levelOne = LevelOne()
        levelOne.plane.position_x = 400
        levelOne.plane.position_y = 500
        enemy1 = Enemy(400, 500, 0, 0)
        enemy2 = Enemy(0, 100, 0, 0)
        levelOne.enemies.append(enemy1)
        levelOne.enemies.append(enemy2)
        hitByEnemy_judge(levelOne)
        self.assertEqual(len(levelOne.enemies), 1)

    def test_hit_judge(self):
        # Test whether an enemy and a bullet are both removed from the list of enemies and list of bullets when they hit each other
        levelOne = LevelOne()
        bullet1 = Bullet(300, 400, 0)
        bullet2 = Bullet(0, 100, 0)
        enemy1 = Enemy(300, 400, 0, 0)
        enemy2 = Enemy(0, 600, 0, 0)
        levelOne.plane.all_bullets.append(bullet1)
        levelOne.plane.all_bullets.append(bullet2)
        levelOne.enemies.append(enemy1)
        levelOne.enemies.append(enemy2)
        hit_judge(levelOne)
        self.assertEqual(len(levelOne.plane.all_bullets), 1)
        self.assertEqual(len(levelOne.enemies), 1)


if __name__ == '__main__':
    unittest.main()
