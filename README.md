Pointcloud Downsampler
This is an octree implementation of downsampling by removing random clusters
Create an octree by using Octree(csv_data, max_points_per_octant)
Then downsample by tree.downsample(coefficient, filename.csv)
