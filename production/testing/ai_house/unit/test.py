import unittest
from production.ai_house.code.pong_minigame import ball,paddle
from production.ai_house.code.level2 import Level, CameraGroup
from production.ai_house.code.player2 import Player
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))
import pygame

class TestPong(unittest.TestCase):
    def setup(self):
        self.ball = ball(10,10)
        self.paddle = paddle(10,10)

    def test_ball(self):
        self.assertEqual(self.ball.x,10, "Should be 10")
        self.assertEqual(self.ball.y,10, "Should be 10")
        self.assertEqual(self.ball.ball_rad,8, "Should be 8")
        self.assertEqual(self.ball.speed_x,-7, "Should be -7")
        self.assertEqual(self.ball.speed_y,-5, "Should be 5")

    def test_paddle(self):
        self.assertEqual(self.paddle.x,10, "Should be 10")
        self.assertEqual(self.paddle.y,10, "Should be 10")
        self.assertEqual(self.paddle.speed,7, "Should be 7")
        self.assertEqual(self.paddle.ai_speed,6, "Should be 6")


class TestIntro(unittest.TestCase):
    def setup(self):
        self.level = Level()
        self.cg = CameraGroup()

    def test_sprites(self):
        self.assertEqual(self.level.collision_sprites,pygame.sprite.Group())
        self.assertEqual(self.level.interaction_sprites,pygame.sprite.Group())

    def test_scale(self):
        self.assertEqual(self.cg.zoom_scale, 1.5, "Should be 1.5")
        

    
class TestPlayer(unittest.TestCase):
    def setup(self):
        self.player = Player()
    def test_player(self):
        self.assertEqual(self.player.animation_status, "forward_idle", "Should be forward idle")
        self.assertEqual(self.player.frame_index, 0, "Should be 0")
        self.assertEqual(self.player.speed, 150)
        self.assertEqual(self.player.npc_banner_status, False)
        self.assertEqual(self.player.npc_banner_status2, False)
        self.assertEqual(self.player.intro_text_status, False)
        self.assertEqual(self.player.run_mg_status, False)
        self.assertEqual(self.player.z, 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
    

    
        

   

        
    
    


