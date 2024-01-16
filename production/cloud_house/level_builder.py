"""
AI Group Project Team 7 Spring22/23

Desc: This module contains classses for level creation.

Tile class represent a single tile that'll be used in the connect-the-pipe game.
Level class represent a level of the game which contains bunch of Tile classes.
 
Created by: Muhammad Kamaludin
Modified by:
Last modified: 18/5/2023
"""

import pygame
pygame.init()

class Tile():
    """
    class for individual tiles in the 'connect the pipe/cable' minigame
    """
    def __init__(self, current_dir : int = 0, target_dir : int= 0, type : str = "blank"
                 , locked : bool = True, key_solution: bool = False):
        
        """
        Tile type:
        'blank' 'straight' 'turn' '3branch' '4branch' 'input' 'output'
        
        """

        #load image
        self.surf = pygame.image.load(f"cloud_house/assets/pipe_{type}.png")
        self.rect = self.surf.get_rect()
        if type in ['straight','turn','3branch'] and locked:
            self.surf = pygame.image.load(f"cloud_house/assets/pipe_{type}_locked.png")
            self.rect = self.surf.get_rect()
        self.type = type
        self.current_direction = 0
        self.target_direction = target_dir   
        self.locked = locked
        self.key_solution = key_solution #this bool indicate this tile is included in the level solution     
        self.rotate(current_dir)
 
    def rotate(self, count : int = 1):

        if self.type == "straight":
            self.current_direction = (self.current_direction + count) % 2
        elif self.type == "turn" or self.type == "3branch":
            self.current_direction = (self.current_direction + count ) % 4
        
        #update image and rectangle
        self.surf = pygame.transform.rotate(self.surf,90*count)
        self.rect = self.surf.get_rect()

    def unlock(self):
        temp_rect = self.rect
        self.surf = pygame.image.load(f"cloud_house/assets/pipe_{self.type}.png")
        self.surf = pygame.transform.scale_by(self.surf,2.5)
        self.surf = pygame.transform.rotate(self.surf,90*self.current_direction)
        self.rect = self.surf.get_rect(center=temp_rect.center)
        self.locked = False

class Level():
    """
    Class for levels
    """
    def __init__(self, width : int, height: int, qna, distinct_tiles):
        """
        distinct_tiles must be a list of tuples of form (type,current_dir, target_dir, locked, key_solution, row, col)
        """
        self.quiz = qna #Quiz object
        self.score = 0
        self.is_answered = False

        #make the level layout
        temp_layout = [ [ Tile() for col in range(width) ] for row in range(height)]

        for type, curr, targ, lock, key, row, col in distinct_tiles:
            temp_layout[row][col] = Tile(curr, targ, type, lock, key)

        self.layout = temp_layout #2-D array of Tile

    
    def is_complete(self):
        """
        Check if all tiles head the correct direction
        """
        is_complete = True
        for row in self.layout:
            for tile in row:

                if not is_complete:
                    return is_complete
                if tile.key_solution:
                    is_complete = tile.current_direction == tile.target_direction
                    #print(f"{tile.type} tile, : ", is_complete)
                    
        return is_complete
    
    def update():
        print("This is update function")

    def scale(self, factor: float = 1):
        """
        
        """
        for row in self.layout:
            for tile in row:
                tile.surf = pygame.transform.scale_by(tile.surf,factor)
                tile.rect = tile.surf.get_rect()

    def display_on_screen(self,screen):

        tile_width = self.layout[0][0].rect.width
        row_count = len(self.layout)
        wrapper_rect = pygame.Rect(0,0,tile_width*row_count,tile_width*row_count)
        wrapper_rect.center = (screen.get_width()/2,screen.get_height()/2)
        
        for row_index, row in enumerate(self.layout):
            for col_index, tile in enumerate(row):
                x = wrapper_rect.topleft[0] + tile.rect.width*col_index
                y = wrapper_rect.topleft[1] + tile.rect.height*row_index
                tile.rect = tile.surf.get_rect(topleft=(x,y))
                screen.blit(tile.surf, tile.rect)

"""
All cloud minigame sublevels are created here
"""       
#(type,current_dir, target_dir, locked, key_solution, row, col)

tiles_1 = [('input',0,0,True,False,4,2),('straight',1,0,False,True,3,2),
           ('straight',0,0,False,True,2,2),('straight',1,0,True,True,1,2),
           ('output',2,2,True,False,0,2)]

tiles_2 = [('input',0,0,True,False,4,2),('straight',0,0,False,True,3,2),
           ('turn',2,0,True,True,2,2), ('straight',0,1,False,True,2,3),
           ('output',1,1,True,False,2,4)]


tiles_3 = [('input',2,2,True,False,0,0),('turn',3,1,False,True,1,0),
           ('3branch',0,0,False,True,1,1),('straight',1,1,False,True,1,2), 
           ('turn',3,3,False,True,1,3),('straight',1,0,True,True,2,3),
           ('turn',1,2,False,True,3,3),('turn',0,0,False,True,3,2),
           ('output',0,0,True,False,4,2)]

tiles_4 = [('input',3,3,True,False,2,0),('turn',2,3,False,True,2,1),
           ('turn',3,1,False,True,3,1),('straight',1,1,False,False,1,1),
           ('straight',1,1,False,True,3,2),
           ('straight',1,1,False,True,3,3),('turn',0,2,True,True,3,4),
           ('straight',0,0,False,True,2,4),('turn',3,3,False,True,1,4),
           ('output',3,3,True,False,1,3)]

tiles_5 = [('input',0,0,True,False,4,0),('turn',0,0,False,True,3,0),
           ('4branch',0,0,True,False,3,1),('turn',3,0,False,True,2,1),
           ('straight',1,1,False,False,3,2),('4branch',0,0,True,False,2,2),
           ('straight',1,0,False,True,1,2),('turn',0,0,False,True,0,2),
           ('straight',0,1,True,True,0,3),('turn',2,2,False,False,1,3),
           ('4branch',0,0,True,False,0,4),('straight',0,0,False,True,1,4),
           ('straight',0,0,False,True,2,4),('4branch',0,0,True,False,3,4),
           ('output',0,0,True,False,4,4)]

tiles_6 = [('output',2,2,True,False,0,0),('straight',0,0,False,True,1,0),
           ('straight',0,0,False,True,2,0),('straight',0,0,False,True,3,0),
           ('turn',3,1,False,True,4,0),('straight',0,1,False,True,4,1),
           ('straight',0,1,False,True,4,2),('straight',1,1,False,True,4,3),
           ('turn',2,2,False,True,4,4),('straight',0,0,False,True,3,4),
           ('straight',1,0,False,True,2,4),('straight',1,0,False,True,1,4),
           ('turn',0,3,False,True,0,4),('straight',1,1,False,True,0,3),
           ('turn',3,0,True,True,0,2),('straight',0,0,False,True,1,2),
           ('output',0,0,True,False,2,2)]

tiles_7 = [('input',2,2,True,False,1,2),
           ('straight',1,0,True,True,2,2),
           ('output',0,0,True,False,3,2)]

tiles_8 = [('3branch',3,3,False,False,1,1),('turn',3,0,True,True,1,2),
           ('straight',1,1,False,True,1,3),('turn',2,3,False,True,1,4),
           ('input',3,3,True,False,2,0),('straight',0,1,False,True,2,1),
           ('turn',2,2,False,True,2,2),('3branch',2,2,False,False,2,3),
           ('straight',0,0,False,True,2,4),('turn',2,0,False,True,3,1),
           ('straight',1,1,False,True,3,2),('straight',0,1,False,True,3,3),
           ('3branch',3,3,False,True,3,4),('turn',1,1,False,True,4,1),
           ('output',1,1,True,False,4,2)]

tiles_9 = [('turn',3,0,True,True,0,1),('straight',0,1,False,True,0,2),
           ('turn',3,3,False,True,0,3),('turn',0,0,False,True,1,0),
           ('4branch',0,0,True,False,1,1),('turn',1,1,False,False,1,2),
           ('turn',0,1,False,True,1,3),('turn',3,3,False,True,1,4),
           ('straight',0,0,False,True,2,0),('turn',3,0,False,True,2,2),
           ('straight',0,1,False,True,2,3),('turn',2,2,False,True,2,4),
           ('turn',3,1,False,True,3,0),('output',1,1,True,False,3,1),
           ('turn',0,1,False,True,3,2),('turn',0,3,False,True,3,3),
           ('straight',0,0,False,False,4,1),('turn',1,1,False,True,4,3),
           ('input',1,1,True,False,4,4)]



all_tiles = [tiles_1,tiles_2,tiles_3,tiles_4,tiles_5,tiles_6,tiles_7,tiles_8,tiles_9]

def get_levels(lower:int, upper:int):
    """
    Get multiples level object based on the specified levels created above
    """
    selected_tiles = all_tiles[lower:upper+1]
    lvls = [None for i in selected_tiles]

    #(type,current_dir, target_dir, locked, key_solution, row, col)
    for i, tiles in enumerate(selected_tiles):
        lvl = Level(5, 5, "qna", tiles)
        lvl.scale(2.5)
        lvls[i] = lvl

    return lvls