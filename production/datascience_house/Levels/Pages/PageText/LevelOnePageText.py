"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import font


class LevelOnePageText:
    def __init__(self):
        self.colour = (235,168,114)
        # Introduction text to welcome players to the level 1
        self.introduction_textLine1 = font.render(
            "Welcome to Scorpio Interstellar. I am the messenger here.",
            True, self.colour)
        self.introduction_textLine2 = font.render(
            "We have been attacked by some interstellar disruptors who",
            True, self.colour)
        self.introduction_textLine3 = font.render(
            "spread viruses to disrupt the ecology of this interstellar system.", True, self.colour)
        self.introduction_textLine4 = font.render("If you can help us eliminate them, I would be very grateful.", True,
                                                  self.colour)
        self.introduction_textLine5 = font.render("Good luck!", True, self.colour)

        # Reminder text telling the player how to operate the aircraft
        self.reminder_textLine1 = font.render("Press up, down, left or right to move your plane.", True, self.colour)
        self.reminder_textLine2 = font.render("Press w to fire.", True, self.colour)

        # The text displayed after the player has destroyed all enemies in this level
        self.end_textLine1 = font.render("Wow, it's incredible that you were able to eliminate those monsters.",
                                         True,
                                         self.colour)
        self.end_textLine2 = font.render(
            "To thank you for your help, let me give you some crystals from our", True, self.colour)
        self.end_textLine3 = font.render(
            "interstellar system. They can make your spacecraft faster and also", True, self.colour)
        self.end_textLine4 = font.render("enhance your weapons.", True, self.colour)
        self.end_textLine5 = font.render("I wish you a pleasant journey.", True, self.colour)

        # The text instructing the player to leave the level
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True,
                                          self.colour)
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, self.colour)
