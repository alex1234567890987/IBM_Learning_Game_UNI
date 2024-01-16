"""
Written by: Zhongjie Huang, Muhammad
Last modified: 29/04/2023
"""

import sqlite3
from production.general import quiz

DB_PATH = "general/db/AIGame.db"
def create_tables():
    """
    This function is used to create all tables needed for this project in the database.
    """
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME TEXT,
            MONEY REAL NOT NULL DEFAULT 0,
            EXPERIENCE REAL NOT NULL DEFAULT 0,
            EXP_AI REAL NOT NULL DEFAULT 0,
            EXP_BLOCKCHAIN REAL NOT NULL DEFAULT 0,
            EXP_CLOUD REAL NOT NULL DEFAULT 0,
            EXP_CYBERSECURITY REAL NOT NULL DEFAULT 0,
            EXP_DATASCIENCE	REAL NOT NULL DEFAULT 0,
            EXP_IOT	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_AI REAL NOT NULL DEFAULT 0,
            HIGHSCORE_BLOCKCHAIN REAL NOT NULL DEFAULT 0,
            HIGHSCORE_CLOUD	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_CYBERSECURITY	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_DATASCIENCE REAL NOT NULL DEFAULT 0,
            HIGHSCORE_IOT REAL NOT NULL DEFAULT 0
            )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS QUESTIONS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            QUESTION TEXT,
            OPTION_A TEXT NOT NULL,
            OPTION_B TEXT NOT NULL,
            OPTION_C TEXT NOT NULL,
            OPTION_D TEXT NOT NULL,
            CORRECT_OPTION TEXT NOT NULL,
            DIFFICULTY INTEGER NOT NULL,
            HOUSE TEXT NOT NULL
            )''')
            connection.commit()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
            connection.rollback()


def get_user():
    """
    This function is used to get the user's data, which will be returned in a tuple
    """
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM USER")
            userData = cursor.fetchone()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)

        if userData:
            userData = User(userData[1],userData[2],userData[3],userData[4],userData[5],userData[6],userData[7],userData[8],userData[9],userData[10],userData[11],userData[12],userData[13],userData[14],userData[15])

    return userData


def update_user(user):
    """
    This function is used to update user's data, each time when it is called, the user's data will be updated automatically if
    there is a change. e.g. part of save game progress.
    It takes a user instance as the parameter
    """

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT money, experience, exp_ai, exp_blockchain, exp_cloud, "
                           "exp_cybersecurity, exp_datascience, exp_iot, highscore_ai, highscore_blockchain, "
                           "highscore_cloud, highscore_cybersecurity, highscore_datascience, highscore_iot FROM USER")
            userData = cursor.fetchone()

        except sqlite3.Error as e:
            print("An error has occurred: ", e)
        
        #record all changes into a list
        changes = []
        if user.money != userData[0]:                   changes.append(f"money = {user.money}")
        if user.experience > userData[1]:               changes.append(f"experience = {user.experience}")
        if user.exp_ai > userData[2]:                   changes.append(f"exp_ai = {user.exp_ai}")
        if user.exp_blockchain > userData[3]:           changes.append(f"exp_blockchain = {user.exp_blockchain}")
        if user.exp_cloud > userData[4]:                changes.append(f"exp_cloud = {user.exp_cloud}")
        if user.exp_cybersecurity > userData[5]:        changes.append(f"exp_cybersecurity = {user.exp_cybersecurity}")
        if user.exp_datascience > userData[6]:          changes.append(f"exp_datascience = {user.exp_datascience}")
        if user.exp_iot > userData[7]:                  changes.append(f"exp_iot = {user.exp_iot}")
        if user.highscore_ai > userData[8]:             changes.append(f"highscore_ai = {user.highscore_ai}")
        if user.highscore_blockchain > userData[9]:     changes.append(f"highscore_blockchain = {user.highscore_blockchain}")
        if user.highscore_cloud > userData[10]:         changes.append(f"highscore_cloud = {user.highscore_cloud}")
        if user.highscore_cybersecurity > userData[11]: changes.append(f"highscore_cybersecurity = {user.highscore_cybersecurity}")
        if user.highscore_datascience > userData[12]:   changes.append(f"highscore_datascience = {user.highscore_datascience}")
        if user.highscore_iot > userData[13]:           changes.append(f"highscore_iot = {user.highscore_iot}")

        if not len(changes): return #return if no changes detected

        #format the execute statement string, it'll combine all changes in the list into a string. it'll add comma automatically
        execute_str = "UPDATE USER SET "
        for i, c in enumerate(changes):
            execute_str += c
            execute_str += "," if i != len(changes) - 1 else ""
        #execute update
        try:
            cursor.execute(execute_str)
            connection.commit()
            print("User's data has been updated successfully")
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
            connection.rollback()
            
def get_questions(difficulty: int, house: str):
    """
    This function is used to get all questions from the questions table.
    All questions corresponding to the difficulty condition will be returned in a tuple
    It takes a degree of difficulty and house name as parameters

    list of house:
    ai
    cloud
    cybersecurity
    blockchain
    datascience
    iot
    """
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"SELECT QUESTION, OPTION_A, OPTION_B, OPTION_C, OPTION_D, CORRECT_OPTION FROM QUESTIONS WHERE DIFFICULTY = {difficulty} AND HOUSE = '{house}'")
            questions = cursor.fetchall()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)

        for i, (question, option1, option2, option3, option4, answer) in enumerate(questions):
            questions[i] = quiz.Quiz(question, [option1, option2, option3, option4], answer)

    return questions


class User:
    def __init__(self, username='Player', money=0.0, experience=0.0, exp_ai=0.0, exp_blockchain=0.0, exp_cloud=0.0, exp_cybersecurity=0.0,
                 exp_datascience=0.0, exp_iot=0.0, highscore_ai=0.0, highscore_blockchain=0.0, highscore_cloud=0.0, highscore_cybersecurity=0.0,
                 highscore_datascience=0.0, highscore_iot=0.0):
        self.username = username
        self.money = money
        self.experience = experience
        self.exp_ai = exp_ai
        self.exp_blockchain = exp_blockchain
        self.exp_cloud = exp_cloud
        self.exp_cybersecurity = exp_cybersecurity
        self.exp_datascience = exp_datascience
        self.exp_iot = exp_iot
        self.highscore_ai = highscore_ai
        self.highscore_blockchain = highscore_blockchain
        self.highscore_cloud = highscore_cloud
        self.highscore_cybersecurity = highscore_cybersecurity
        self.highscore_datascience = highscore_datascience
        self.highscore_iot = highscore_iot


if __name__ == '__main__':
    create_tables()
