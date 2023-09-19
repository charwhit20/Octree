import pandas as pd
from OctreePackage import Octree

data = pd.read_csv('input.csv')
Tree = Octree(data, 4)
Tree.downsample(.5, 'newdata.csv')
