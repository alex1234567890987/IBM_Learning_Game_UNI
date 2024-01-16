Intoduction:

Here is the minigame used by Data Science House, where players take on the role of interstellar travellers and explore the different stars.

There are three levels in this game and players will quickly familiarise themselves with the gameplay in the first level and in the second and third levels they will need to answer questions before they can play.

After the player has completed all three levels, the data for this house will be reset, meaning that the player will need to start again from the beginning if they are playing.

Object-Oriented Design:

WindowScript: Instantiate pygame and set up other related functionalities here.

Plane class: Contains properties and functions of the plane, such as health, speed, bullet firing, etc. The Plane class includes Bullet class (objects created by it will be member variables of the Plane class).

Enemy class: Contains properties and abilities of the enemy. The Enemy class includes a Bullet class (objects created by it will be member variables of the Enemy class).

EventScript: Provides two methods for retrieving events, one for the home page events and one for level events.

Launch class: This is the entry point of the game. Instantiate all classes here and call methods provided by each class according to the game's logic.

Levels package: Contains three level classes, a script providing common functions to the three levels, and a page package. 

The pages package contains four page classes and a PageText package. 

The PageText package includes four PageText classes and a script providing common functions. 

The following is an explanation of all the classes in these packages and their relationships:

LevelOne class: Contains various properties of the first level, including the level's running status, maximum number of enemies in the level, enemies that have appeared in the level, etc. This class includes a Plane class and a 

LevelOnePage class from the pages package as member variables. It also provides a method to run the game, which is called by the Launch class.

LevelTwo class and LevelThree class follow the same structure as LevelOne class.

LevelOnePage class: Provides methods to display images and texts in the first level and controls the state of displaying these elements. This class includes a 

LevelOnePageText class from the page text package as a member variable.

LevelTwoPage class and LevelThreePage class follow the same structure as LevelOnePage class.

LevelOnePageText class: Provides all the texts to be displayed in Level One, along with their font, color, size settings.

LevelTwoPageText class and LevelThreePageText class follow the same structure as LevelOnePageText class.











































