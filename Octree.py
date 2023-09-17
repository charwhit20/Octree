"""
p1 +x +y +z
p2 +x +y -z
p3 +x -y +z
p4 +x -y -z
p5 -x +y +z
p6 -x +y -z
p7 -x -y +z
p8 -x -y -z
data (x, y, z)
"""

"""
Each Node denotes a perfect representation of an ideal octant
contains a list point maximum for each, and points to 8 other octants
"""
class Node:
    def __init__(self, data, quads=(0,0,0,0,0,0,0,0)):
        self.data = [0,0,0,0,0,0,0,0]
        self.q1 = quads[0]
        self.q2 = quads[1]
        self.q3 = quads[2]
        self.q4 = quads[3]
        self.q5 = quads[4]
        self.q6 = quads[5]
        self.q7 = quads[6]
        self.q8 = quads[7]


class Octree:
    def __init__(self):
        self.head = Node()

#insert point in octree
def insert(self, data):
