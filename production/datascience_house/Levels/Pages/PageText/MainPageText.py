"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import font


class MainPageText:
    def __init__(self):
        # Welcome to "Data Science House" (Homepage) - Introduction Text for Players
        self.colour = (248, 170, 148)
        self.introduction_textLine1 = font.render(
            "Welcome to the Data Science House !",
            True, self.colour)
        self.introduction_textLine2 = font.render(
            "Here, you will play the role of an interstellar traveler piloting a fighter jet,", True, self.colour)
        self.introduction_textLine3 = font.render(
            "exploring different galaxies and helping the intergalactic steward eliminate", True, self.colour)
        self.introduction_textLine4 = font.render("space destroyers.", True, self.colour)
        self.introduction_textLine5 = font.render("Begin your fantastic journey now !!", True, self.colour)

        self.reminder_textLine = font.render("Please complete the previous level first!", True, self.colour)
