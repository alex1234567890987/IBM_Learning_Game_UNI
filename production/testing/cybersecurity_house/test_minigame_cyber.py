"""
AI Group Project Team 7 Spring22/23

Desc: Unit test for minigame_cyber.py
 
Created by: Muhammad Kamaludin
Modified by:
Last modified: 19/5/2023
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

import unittest
from production.cybersecurity_house.minigame_cyber import TicTacToe, Game


class TestTicTacToe(unittest.TestCase):

    """
    Test the object initialisation 
    """
    def test_initialise(self):
         
        #should have a default param value
        ttt = TicTacToe("game")
        self.assertIsNotNone(ttt)

    """
    Test the tictactoe completion (not winning condition)
    Verify all methods that check matching horizontal,  vertical, and diagonal of the tictactoe 
    """
    def test_completion_condition(self):

        #check horizontal: condition not met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "-",
                           "o", "", "x",
                           "-", "-", "-"]
        
        self.assertNotEqual(ttt.check_horizontal(), True)

        #check horizontal: condition met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "-",
                           "o", "o", "o",
                           "-", "-", "-"]
        
        self.assertTrue(ttt.check_horizontal())
        
        
        #check vertical: condition not met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "-",
                           "o", "", "x",
                           "-", "-", "-"]
        
        self.assertNotEqual(ttt.check_vertical(), True)

        #check vertical: condition met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "-",
                           "o", "x", "o",
                           "-", "x", "-"]
        
        self.assertTrue(ttt.check_vertical())
        
        #check diagonal: condition not met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "-",
                           "o", "-", "x",
                           "-", "-", "-"]
        
        self.assertNotEqual(ttt.check_diagonal(), True)

        #check diagonal: condition met
        ttt = TicTacToe("game")
        ttt.board_array = ["-", "x", "x",
                           "o", "x", "o",
                           "x", "x", "-"]
        
        self.assertTrue(ttt.check_diagonal())
    
    """
    Test the tictactoe not winning condition
    """
    def test_completion_condition(self):

        #tie
        ttt = TicTacToe("game")
        ttt.board_array = ["x", "o", "x",
                           "o", "x", "o",
                           "o", "x", "o"]
        
        self.assertTrue(ttt.check_if_tie())

        #win - condition not met
        ttt = TicTacToe("game")
        ttt.board_array = ["x", "-", "x",
                           "o", "x", "o",
                           "o", "x", "o"]
        
        self.assertFalse(ttt.check_if_win())

        #win - condition met
        ttt = TicTacToe("game")
        ttt.board_array = ["x", "x", "x",
                           "o", "x", "o",
                           "o", "x", "o"]
        
        self.assertTrue(ttt.check_if_win())

class TestGame(unittest.TestCase):

    """
    Test the object initialisation
    """
    def test_initialise(self):
         
        #should have a default param value
        g = Game()
        self.assertIsNotNone(g)

        #it should instantite a tictactoe obj
        self.assertTrue(isinstance(g.tic_tac_toe,TicTacToe))

    """
    Upon executing new game, new tictactoc obj should be created
    while updating the user score
    """
    def test_new_game(self):

        g = Game()

        #simulate a winning condition
        init_ttt = g.tic_tac_toe
        init_score = g.score
        g.tic_tac_toe.board_array = ["x", "x", "x",
                                     "o", "x", "o",
                                     "o", "x", "o"]
        
        g.new_game()

        #compare old and the new tictactoe obj
        self.assertNotEqual(init_ttt,g.tic_tac_toe)
        #see incrment in score
        self.assertEqual(g.score, init_score+1)

        g = Game()

        #simulate a losing condition
        init_ttt = g.tic_tac_toe
        init_score = g.score
        g.tic_tac_toe.board_array = ["x", "-", "x",
                                     "o", "x", "o",
                                     "o", "o", "o"]
        
        g.new_game()

        #compare old and the new tictactoe obj
        self.assertNotEqual(init_ttt,g.tic_tac_toe)
        #see no changes in score
        self.assertEqual(g.score, init_score)


        



if __name__ == '__main__':
    unittest.main()