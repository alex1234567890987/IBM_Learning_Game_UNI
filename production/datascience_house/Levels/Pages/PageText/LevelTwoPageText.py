"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import font


class LevelTwoPageText:
    def __init__(self):
        self.colour = (251,252,214)
        # Introduction text to welcome players to the level 2 (players have not answered any questions yet).
        # Players will be informed that they will need to answer questions in this level.
        self.introduction1_textLine1 = font.render("Hello there! You've worked hard all the way!", True, self.colour)
        self.introduction1_textLine2 = font.render("I am a Libra constellation interstellar navigator, and in charge", True,
                                                   self.colour)
        self.introduction1_textLine3 = font.render("of navigating through this constellation.", True,
                                                   self.colour)
        self.introduction1_textLine4 = font.render("You need my permission to enter the Libra constellation.", True,
                                                   self.colour)
        self.introduction1_textLine5 = font.render("According to regulations, you need to answer a few questions.",
                                                   True,
                                                   self.colour)
        self.introduction1_textLine6 = font.render("Do you have the courage to accept the challenge?", True, self.colour)

        # Reminder text after the player chooses to answer the questions
        self.reminder1_textLine1 = font.render("You're so brave, I'm rooting for you!", True, self.colour)
        self.reminder1_textLine2 = font.render("There are 6 questions in total.", True, self.colour)
        self.reminder1_textLine3 = font.render("If you answer 70% correctly, you win!", True, self.colour)
        self.reminder1_textLine4 = font.render("Good luck!", True, self.colour)

        # Reminder text after a player fails to answer the questions
        self.reminder2_textLine1 = font.render("I'm sorry, but you didn't achieve a 70% accuracy rate,", True,
                                               self.colour)
        self.reminder2_textLine2 = font.render("so I cannot grant you access to our interstellar network.", True,
                                               self.colour)
        self.reminder2_textLine3 = font.render("Don't be discouraged, though.", True, self.colour)
        self.reminder2_textLine4 = font.render("You're welcome to come back and try again.", True, self.colour)

        # Reminder text after a player has successfully answered the questions
        self.reminder3_textLine1 = font.render("You have achieved a 70% accuracy rate, that's great!", True, self.colour)
        self.reminder3_textLine2 = font.render("Now I will grant you the passage to the Libra constellation", True,
                                               self.colour)
        self.reminder3_textLine3 = font.render("interstellar, and wish you a smooth journey.", True, self.colour)

        # Introduction text to welcome players to the second level (players have answered the questions)
        self.introduction2_textLine1 = font.render("Welcome to the interstellar of Libra constellation.", True,
                                                   self.colour)
        self.introduction2_textLine2 = font.render(
            "It used to be a beautiful place, but since some interstellar", True, self.colour)
        self.introduction2_textLine3 = font.render("raiders came, they have destroyed the ecology here.",
                                                   True,
                                                   self.colour)
        self.introduction2_textLine4 = font.render(
            "I hope you can use your power to help us eliminate these",
            True,
            self.colour)
        self.introduction2_textLine5 = font.render(
            "annoying invaders.",
            True,
            self.colour)
        self.introduction2_textLine6 = font.render("If you can do it, I would be very grateful.", True,
                                                   self.colour)
        self.introduction2_textLine7 = font.render("Good luck!", True,
                                                   self.colour)

        # Tell players how aircraft performance changes
        self.reminder4_textLine = font.render("You now have faster movement speed and stronger firepower.", True,
                                              self.colour)

        # The text displayed after the player has destroyed all enemies in this level
        self.end_textLine1 = font.render("Thank you for helping us eliminate these monsters.", True, self.colour)
        self.end_textLine2 = font.render("You're really amazing! However, I still have a gift for you.", True,
                                         self.colour)
        self.end_textLine3 = font.render("Here's a crystal from our interstellar world. It can enable", True,
                                         self.colour)
        self.end_textLine4 = font.render("your spacecraft to shoot bullets that automatically track", True,
                                         self.colour)
        self.end_textLine5 = font.render(
            "the enemy.", True,
            self.colour)
        self.end_textLine6 = font.render("I wish you a pleasant journey through the stars.", True, self.colour)

        # The text instructing the player to leave the level
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, self.colour)
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, self.colour)
