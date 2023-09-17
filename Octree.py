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


class Node:
    def __init__(self, data=(None, None, None, None, None, None, None, None), quads=(0, 0, 0), depth=0):
        # tracks depth of each node
        self.depth = depth
        # tracks datapoints inside quadrant radius, mutable
        self.data = list(data)
        # tracks coords of quadrant (x, y, z), immutable, set at quadrant creation
        self.quads = quads
        # tracks nodes each quadrant points to, mutable
        self.qvals = [None, None, None, None, None, None, None, None]


class Octree:
    def __init__(self):
        self.head = Node()


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
    x1, y1, z1 = cur.quads
    while True:
        # decipher quadrant point belongs to
        # quad 0
        if x > x1 and y > y1 and z > z1:
            return
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
