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


# This defines a QUADRANT, which points to 8 POINTS inside it
class Node:
    def __init__(self, coords=(0, 0, 0), depth=0):
        # tracks depth of each node
        self.depth = depth
        # tracks datapoints inside quadrant radius, mutable
        self.data = [None, None, None, None, None, None, None, None]
        # tracks coords of quadrant (x, y, z), immutable, set at quadrant creation
        self.coords = coords
        # tracks nodes each quadrant points to, mutable
        self.nodes = [None, None, None, None, None, None, None, None]


class Octree:
    # include max and min so the tree knows how to divide quadrants
    def __init__(self, constraints):
        self.head = Node()
        self.xmax, self.xmin, self.ymax, self.ymin, self.zmax, self.zmin = constraints


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
    # insert point in octree
    # octant check, if point in slot in octant != None, create new Node
    # data is (x,y,z)

    def insert(self, data):
        cur = self.head
        x, y, z = data
        x1, y1, z1 = cur.coords
        while True:
            # decipher quadrant point belongs to
            # quad 0
            # create new node based on coords + xmax / 2^depth ex, 0,0,0, creates node 8, 8, 8 in 32,32,32 space
            # created by dividing 16x16x16 octant into 8, the point is in the center at 8,8,8 or 16/2^1
            if x > x1 and y > y1 and z > z1:
                # if there is data in spot where it should go, but the current node is a leaf
                # then you must divide the 0 quadrant into 8 and put the new point in there
                if cur.data[0] is not None and cur.nodes[0] is None:
                    cur.nodes[0] = Node((x1 + (self.xmax / 2 ** cur.depth), y1 + (self.ymax / 2 ** cur.depth),
                                         z1 + (self.zmax / 2 ** cur.depth)), cur.depth + 1)
                    cur = cur.nodes[0]
                    continue
                # Else there is data in the spot where it should go, but the current node is not a leaf
                # then you must traverse to the next node, and recheck the placement
                elif cur.data[0] is not None and cur.nodes[0] is not None:
                    cur = cur.nodes[0]
                    continue
                # else, node is a leaf, and the data point is empty
                else:
                    cur.data[0] = (x, y, z)
                    break
            # quad 1
            elif x > x1 and y > y1 and z < z1:
                return
            # quad 2
            elif x > x1 and y < y1 and z > z1:
                return
            # quad 3
            elif x > x1 and y < y1 and z < z1:
                return
            # quad 4
            elif x <= x1 and y >= y1 and z >= z1:
                return
            # quad 5
            elif x <= x1 and y >= y1 and z <= z1:
                return
            # quad 6
            elif x <= x1 and y <= y1 and z >= z1:
                return
            # quad 7
            elif x <= x1 and y <= y1 and z <= z1:
                return
