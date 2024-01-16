import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

import unittest
from production.general import quiz

class TestOptionClass(unittest.TestCase):
    """
    Test the object initialisation and set pos method
    update method will be tested manually
    """
   
    def test_initialise(self):
         
        o = quiz.Quiz.Option("answer1", True)
        self.assertIsNotNone(o)

    def test_set_position(self):


        #init position
        o = quiz.Quiz.Option("answer1", True)
        self.assertEqual(o.rect.left, 0)
        self.assertEqual(o.rect.top, 0)
        self.assertEqual(o.rect.right, o.rect.width)
        self.assertEqual(o.rect.bottom, o.rect.height)

        #Changed pos
        o.set_position([10,10,0,0])
        self.assertEqual(o.rect.left, 10)
        self.assertEqual(o.rect.top, 10)
        o.set_position([0,0,10,10])
        self.assertEqual(o.rect.right, 10)
        self.assertEqual(o.rect.bottom, 10)

class TestQuizClass(unittest.TestCase):

    def test_initialise(self):
        q = quiz.Quiz("test question", ["Option1", "Option2", "Option3", "Option4"], "Option3")

        self.assertIsNotNone(q)
        self.assertTrue(any([option.is_answer for option in q.options]))

    def test_setup(self):
        """
        Test so all essentials graphics varibles are initialzed to the corresponding object during setup
        """
        q = quiz.Quiz("test question", ["Option1", "Option2", "Option3", "Option4"], "Option3")
        quiz.pygame.init()
        
        #before setup
        self.assertIsNone(q.background)
        self.assertTrue(q.button_txt is None and q.button_txt_rect is None)
        self.assertTrue(q.submit_button is None and q.submit_button_rect is None)

        #after setup
        q.setup()
        self.assertIsNotNone(q.background)
        self.assertFalse(q.button_txt is None or q.button_txt_rect is None)
        self.assertFalse(q.submit_button is None or q.submit_button_rect is None)


if __name__ == '__main__':
    unittest.main()
    

