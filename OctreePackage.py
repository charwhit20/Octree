import pandas as pd
"""
0 +x +y +z
1 +x +y -z
2 +x -y +z
3 +x -y -z
4 -x +y +z
5 -x +y -z
6 -x -y +z
7 -x -y -z
data (x, y, z)
"""

"""
Each Node denotes a perfect representation of an ideal octant
contains a list point maximum for each, and points to 8 other octants
"""


# This defines an OCTANT, which points to 8 POINTS inside it
class Octant:
    maxPoints = 8

    def __init__(self, data):
        # UPON CREATION, ASSIGN POINTS TO OCTANTS, UPON DIVISION, ASSIGN DATA TO NEW OCTANTS
        # tracks octants each octant points to
        self.octants = [None, None, None, None, None, None, None, None]
        # tracks coords of octant
        self.xcoord, self.ycoord, self.zcoord = data.mean()
        # after octant has been divided, now append data to each octant
        self.octant0 = pd.DataFrame()
        self.octant1 = pd.DataFrame()
        self.octant2 = pd.DataFrame()
        self.octant3 = pd.DataFrame()
        self.octant4 = pd.DataFrame()
        self.octant5 = pd.DataFrame()
        self.octant6 = pd.DataFrame()
        self.octant7 = pd.DataFrame()
        for index, row in data.iterrows():
            x = row['x']
            y = row['y']
            z = row['z']
            """
            0 +x +y +z
            1 +x +y -z
            2 +x -y +z
            3 +x -y -z
            4 -x +y +z
            5 -x +y -z
            6 -x -y +z
            7 -x -y -z
            """
            # octant 0
            if x >= self.xcoord and y >= self.ycoord and z >= self.zcoord:
                self.octant0.append(row)
            # octant 1
            elif x >= self.xcoord and y >= self.ycoord and z <= self.zcoord:
                self.octant1.append(row)
            # octant 2
            elif x >= self.xcoord and y <= self.ycoord and z >= self.zcoord:
                self.octant2.append(row)
            # octant 3
            elif x >= self.xcoord and y <= self.ycoord and z <= self.zcoord:
                self.octant3.append(row)
            # octant 4
            elif x <= self.xcoord and y >= self.ycoord and z >= self.zcoord:
                self.octant4.append(row)
            # octant 5
            elif x <= self.xcoord and y >= self.ycoord and z <= self.zcoord:
                self.octant5.append(row)
            # octant 6
            elif x <= self.xcoord and y <= self.ycoord and z >= self.zcoord:
                self.octant6.append(row)
            # octant 7
            elif x <= self.xcoord and y <= self.ycoord and z <= self.zcoord:
                self.octant7.append(row)
        # if length of octant data is greater than threshold, break it into more octants
        if len(self.octant0) > self.maxPoints:
            self.octants[0] = Octant(self.octant0)
        if len(self.octant1) > self.maxPoints:
            self.octants[1] = Octant(self.octant1)
        if len(self.octant2) > self.maxPoints:
            self.octants[2] = Octant(self.octant2)
        if len(self.octant3) > self.maxPoints:
            self.octants[3] = Octant(self.octant3)
        if len(self.octant4) > self.maxPoints:
            self.octants[4] = Octant(self.octant4)
        if len(self.octant5) > self.maxPoints:
            self.octants[5] = Octant(self.octant5)
        if len(self.octant6) > self.maxPoints:
            self.octants[6] = Octant(self.octant6)
        if len(self.octant7) > self.maxPoints:
            self.octants[7] = Octant(self.octant7)


class Octree:
    # include max and min so the tree knows how to divide quadrants
    def __init__(self, data):
        self.head = Octant(data)

    # Calculate the center of mass of a cloud of data
