import pandas as pd
from OctreePackage import Octree
import pickle
data = pd.read_csv('input.csv')
xmax, ymax, zmax = data.abs().max()

print(xmax, ymax, zmax)

Tree = Octree((xmax, ymax, zmax))
for index, row in data.iterrows():
    Tree.insert((row['x'], row['y'], row['z']))


file = open('processedPoints', 'wb')
pickle.dump(Tree, file)

clean = Tree.cleanTree()
print(clean)