import pandas as pd
from OctreePackage import Octree

data = pd.read_csv('input.csv')
Tree = Octree(data, 2)
Tree.downsample(2, 'newdata.csv')
