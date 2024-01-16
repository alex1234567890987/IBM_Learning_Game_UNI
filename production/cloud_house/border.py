class Border():
    
    def __init__(self, ps: list[(int,int)]):
        """
        It takes a list containing coordinates of polygon vertices, the coordinates must be ordered

        *CURRENTLY THIS IMPLEMENTATION IS MADE ONLY FOR A CLOUD HOUSE,
        """

        self.points = ps
        self.edges = []

        for i, current_point in enumerate(self.points):
            
            if i != len(self.points) - 1:
                self.edges.append((current_point,self.points[i+1]))

    
    def is_colliding(self, coord):
        """
        Check collisions between a point with every edges. Return True if collides with any edges
        """

        collides = []

        for (x1,y1),(x2,y2) in self.edges:

            temp_bools = []

            if x1 == x2:
                temp_bools.append(coord[0] == x1)
            else:
                rnge = (x1,x2) if x1 < x2 else (x2,x1) 
                temp_bools.append(rnge[0] <= coord[0] <= rnge[1])
            
            if y1 == y2:
                temp_bools.append(coord[1] == y1)
            else:
                rnge = (y1,y2) if y1 < y2 else (y2,y1)
                temp_bools.append(rnge[0] <= coord[1] <= rnge[1])

            collides.append(all(temp_bools))
            
        return any(collides)

if __name__ == "__main__":
    
    points = [(550,185),(766,185)]
    
    walkable_area_border = Border(points)
    print(walkable_area_border.edges)
    print(walkable_area_border.is_colliding((600,185)))