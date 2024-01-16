import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

import unittest
from production.cloud_house.border import Border

class TestBorderClass(unittest.TestCase):

    """
    Test the object initialisation 
    """
    def test_initialise(self):
         
         points = [(0,0),(0,10),(10,10),(10,0)]

         b = Border(points)

         self.assertIsNotNone(b)
         self.assertIsNotNone(b.points)
         self.assertIsNotNone(b.edges)

         self.assertTrue(len(b.points) == 4)
         self.assertTrue(len(b.edges) == 3)

    """
    Test if a point is colliding with any of the edges
    """
    def test_collision(self):
                 
        points = [(0,0),(0,10),(10,10),(10,0)]

        b = Border(points)

        test_point = (0,5)
        self.assertTrue(b.is_colliding(test_point))

        test_point = (1,4)
        self.assertFalse(b.is_colliding(test_point))

if __name__ == '__main__':
    unittest.main()