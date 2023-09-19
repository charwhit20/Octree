import pandas as pd
import random
import math
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

# downsampled pointcloud pd.DataFrame(columns=['x', 'y', 'z'])
dspc = []


def save(filename) -> None:
    global dspc
    print("total datapoints in new set: ", len(dspc))
    data = pd.DataFrame(dspc, columns=['x', 'y', 'z'])
    data.to_csv(filename, index=False)


# This defines an OCTANT, which points to 8 POINTS inside it
class Octant:
    def is_leaf(self):
        return all(child is None for child in self.octants)

    def pick_leaf(self):
        global dspc
        leaf_data = (self.octant0 + self.octant1 + self.octant2 + self.octant3 +
                     self.octant4 + self.octant5 + self.octant6 + self.octant7)
        dspc.extend(leaf_data)

    def __init__(self, data, maxp):
        # UPON CREATION, ASSIGN POINTS TO OCTANTS, UPON DIVISION, ASSIGN DATA TO NEW OCTANTS
        self.maxPoints = maxp
        # tracks octants each octant points to
        self.octants = [None, None, None, None, None, None, None, None]
        # tracks coords of octant
        self.xcoord = sum(row[0] for row in data) / len(data)
        self.ycoord = sum(row[1] for row in data) / len(data)
        self.zcoord = sum(row[2] for row in data) / len(data)
        # after octant has been divided, now append data to each octant
        self.octant0 = []
        self.octant1 = []
        self.octant2 = []
        self.octant3 = []
        self.octant4 = []
        self.octant5 = []
        self.octant6 = []
        self.octant7 = []
        for index, row in enumerate(data):
            x, y, z = row
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
            # print("Octant has ", len(self.octant0), " points")
            self.octants[0] = Octant(self.octant0, self.maxPoints)
            self.octant0 = None
        if len(self.octant1) > self.maxPoints:
            # print("Octant has ", len(self.octant1), " points")
            self.octants[1] = Octant(self.octant1, self.maxPoints)
            self.octant1 = None
        if len(self.octant2) > self.maxPoints:
            # print("Octant has ", len(self.octant2), " points")
            self.octants[2] = Octant(self.octant2, self.maxPoints)
            self.octant2 = None
        if len(self.octant3) > self.maxPoints:
            # print("Octant has ", len(self.octant3), " points")
            self.octants[3] = Octant(self.octant3, self.maxPoints)
            self.octant3 = None
        if len(self.octant4) > self.maxPoints:
            # print("Octant has ", len(self.octant4), " points")
            self.octants[4] = Octant(self.octant4, self.maxPoints)
            self.octant4 = None
        if len(self.octant5) > self.maxPoints:
            # print("Octant has ", len(self.octant5), " points")
            self.octants[5] = Octant(self.octant5, self.maxPoints)
            self.octant5 = None
        if len(self.octant6) > self.maxPoints:
            # print("Octant has ", len(self.octant6), " points")
            self.octants[6] = Octant(self.octant6, self.maxPoints)
            self.octant6 = None
        if len(self.octant7) > self.maxPoints:
            # print("Octant has ", len(self.octant7), " points")
            self.octants[7] = Octant(self.octant7, self.maxPoints)
            self.octant7 = None


class Octree:
    # include max and min so the tree knows how to divide quadrants
    def __init__(self, data: pd.DataFrame, maxp=8):
        self.head = Octant(data.values.tolist(), maxp)

    # now with tree created, find all the leaves in the tree
    def __get_leaf_nodes__(self, octant):
        leaves = []
        for i in range(8):
            child = octant.octants[i]
            if child is not None:
                if child.is_leaf():
                    leaves.append(child)
                else:
                    leaves.extend(self.__get_leaf_nodes__(child))
        return leaves

    # this will randomly select and delete leaves from the tree, then return a new dataframe for the cleaned data
    def __pick_leaves__(self, compression):
        leaves = self.__get_leaf_nodes__(self.head)
        print("leaves: ", len(leaves))
        leaves_to_process = random.sample(leaves, max(1, math.floor(len(leaves) * compression)))
        print("leaves to process: ", len(leaves_to_process))
        for leaf in leaves_to_process:
            leaf.pick_leaf()

    def downsample(self, compression, filename):
        self.__pick_leaves__(compression)
        save(filename)
