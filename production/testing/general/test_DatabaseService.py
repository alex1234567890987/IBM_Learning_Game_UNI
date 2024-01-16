import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
import unittest
from general.db.DatabaseService import get_user, update_user, get_questions, User
from general.quiz import Quiz


class DatabaseServiceTest(unittest.TestCase):
    def test_get_user(self):
        user = get_user()
        self.assertTrue(isinstance(user, User))
        print('An object of the User class should be created.')
        print('Testing successfully!')

    def test_update_user(self):
        user = get_user()
        self.assertEqual(update_user(user), None)
        print('Nothing should be changed in this case.')
        print('Testing successfully!')

    def test_get_questions(self):
        questions = get_questions(1, 'datascience')
        self.assertTrue(type(questions), list)
        print('It should be returned as a list.')
        for question in range(len(questions)):
            self.assertTrue(isinstance(questions[question], Quiz))
        print('List contains objects of the Quiz class')
        print('Testing successfully!')


if __name__ == '__main__':
    unittest.main()
