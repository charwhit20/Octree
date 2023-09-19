Pointcloud Downsampler
This is an octree implementation of downsampling by removing random clusters
Create an octree by using Octree(csv_data, max_points_per_octant)
Then downsample by tree.downsample(coefficient, filename.csv) coefficient is how many times smaller the new dataset should be

![downsampler sample github](https://github.com/charwhit20/Pointcloud-Downsampler/assets/99224673/a76f0fc0-88cb-4979-8d95-d03db9e8e4d0)
