"""
AI Group Project Team 7 Spring22/23

Desc: Unit test for level_builder.py
 
Created by: Muhammad Kamaludin
Modified by:
Last modified: 19/5/2023
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

import unittest
from production.cloud_house.level_builder import Tile, Level

class TestTile(unittest.TestCase):

    """
    Test the object initialisation 
    """
    def test_initialise(self):
         
        #should have a default param value
        t = Tile()
        self.assertIsNotNone(t.current_direction)
        self.assertIsNotNone(t.target_direction)
        self.assertIsNotNone(t.type)
        self.assertIsNotNone(t.locked)
        self.assertIsNotNone(t.rect)
        self.assertIsNotNone(t.surf)

    """
    Test to rotate a tile object, different behaviour should be expected
    for tile object with different 'type' variable
    """
    def test_rotate(self):
        
        #'blank' and  '4branch' tile shouldn't rotate
        t = Tile(type="blank", current_dir=0)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        t = Tile(type="4branch", current_dir=0)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        #'turn' and '3branch', 'input' and 'output' tile can rotate up to 4 direction
        t = Tile(type="turn", current_dir=3)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        t = Tile(type="3branch", current_dir=3)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        t = Tile(type="input", current_dir=3)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        t = Tile(type="output", current_dir=3)
        t.rotate()
        self.assertEqual(t.current_direction,0)

        #'straight' tile can rotate up to 2 direction
        t = Tile(type="straight", current_dir=1)
        t.rotate()
        self.assertEqual(t.current_direction,0)

    def test_unlock(self):

        t = Tile(locked=True)
        t.unlock()
        self.assertFalse(t.locked)

class TestLevel(unittest.TestCase):

    """
    It will create groups of tile objects upon initialisation
    """
    def test_initialise(self):

        l = Level(1,1,"qna",[])
        self.assertTrue(isinstance(l.layout[0][0], Tile))

    """
    A level is considered complete when all the tile which key=True, has current_direction == target_direction  
    """
    def test_completion_check(self):

        specified_tile = [('straight',0,0,False,True,0,0)]
        l = Level(1,1, "qna", specified_tile)

        self.assertTrue(l.is_complete())


if __name__ == '__main__':
    unittest.main()