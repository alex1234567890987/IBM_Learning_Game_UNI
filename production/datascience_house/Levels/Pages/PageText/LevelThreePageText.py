"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import font


class LevelThreePageText:
    def __init__(self):
        self.colour = (193, 223, 132)

        # Introduction text to welcome players to the level 3 (players have not answered any questions yet).
        # Players will be informed that they will need to answer questions in this level.
        self.introduction1_textLine1 = font.render("Hello, this is the messenger from the Pisces interstellar region.",
                                                   True,
                                                   self.colour)
        self.introduction1_textLine2 = font.render(
            "You are about to enter our territory, and according to our ", True, self.colour)
        self.introduction1_textLine3 = font.render(
            "communication records, you do not have the permission to enter.", True, self.colour)
        self.introduction1_textLine4 = font.render("However, since you have managed to reach this point,", True,
                                                   self.colour)
        self.introduction1_textLine5 = font.render(
            "I assume you are aware of the rules.", True,
            self.colour)
        self.introduction1_textLine6 = font.render("Would you like to take on the challenge?", True, self.colour)

        # Reminder text after a player chooses to answer the questions
        self.reminder1_textLine1 = font.render("You are indeed very brave. Let's begin then.", True, self.colour)
        self.reminder1_textLine2 = font.render("There are a total of 9 questions here.", True,
                                               self.colour)
        self.reminder1_textLine3 = font.render("Good luck!", True,
                                               self.colour)

        # Reminder text after a player fails to answer the questions
        self.reminder2_textLine1 = font.render("I'm sorry, but you did not meet the requirements,", True,
                                               self.colour)
        self.reminder2_textLine2 = font.render("so I cannot grant you access. Please feel free to", True,
                                               self.colour)
        self.reminder2_textLine3 = font.render("come back and challenge again in the future.", True, self.colour)

        # Reminder text after a player has successfully answered the questions
        self.reminder3_textLine1 = font.render("Congratulations, you have passed the test.", True,
                                               self.colour)
        self.reminder3_textLine2 = font.render(
            "Now, let me grant you the permission to enter our interstellar",
            True, self.colour)
        self.reminder3_textLine3 = font.render(
            "region. However, I must warn you that the monsters in our", True, self.colour)
        self.reminder3_textLine4 = font.render("region are quite formidable.", True,
                                               self.colour)
        self.reminder3_textLine5 = font.render(
            "Good luck!", True, self.colour)

        # Introduction text to welcome players to the third level (players have answered the questions)
        self.introduction2_textLine1 = font.render("Welcome to the Pisces interstellar region.", True, self.colour)
        self.introduction2_textLine2 = font.render("This was one of the first places to be invaded by the ", True,
                                                   self.colour)
        self.introduction2_textLine3 = font.render("interstellar destroyers.", True, self.colour)
        self.introduction2_textLine4 = font.render("Those destroyers have evolved and become stronger here,", True,
                                                   self.colour)
        self.introduction2_textLine5 = font.render("and we have not been able to eliminate them.", True, self.colour)
        self.introduction2_textLine6 = font.render("If you can help us defeat them, you will become a hero ", True,
                                                   self.colour)
        self.introduction2_textLine7 = font.render("of our interstellar region.", True, self.colour)
        self.introduction2_textLine8 = font.render("Good luck to you!", True, self.colour)

        # Tell players how aircraft performance changes
        self.reminder4_textLine1 = font.render(
            "Your spacecraft can now shoot bullets that automatically track the enemy.", True, self.colour)
        self.reminder4_textLine2 = font.render("Press the R key to fire them.", True, self.colour)

        # The text displayed after the player has destroyed all enemies in this level
        self.end_textLine1 = font.render("Wow, you have eliminated all those destroyers.", True, self.colour)
        self.end_textLine2 = font.render("That's incredible! You have truly become a hero",
                                         True, self.colour)
        self.end_textLine3 = font.render("of the interstellar region.",
                                         True, self.colour)
        self.end_textLine4 = font.render("Congratulations on your achievement!", True, self.colour)

        # The text instructing the player to leave the level
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, self.colour)
        self.exit_textLine2 = font.render("Please proceed to finish your journey.", True, self.colour)
