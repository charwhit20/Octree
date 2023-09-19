Pointcloud Downsampler
This is an octree implementation of downsampling by removing random clusters
Create an octree by using Octree(csv_data, max_points_per_octant)
Then downsample by tree.downsample(coefficient, filename.csv)

Example of down sampling with max octant capacity of 4 (removing clusters of 32 -> 8 * 4),
and downsampling coeefficient of .8 (include online 80% of the leaves in the octree)


![downsampler github](https://github.com/charwhit20/Pointcloud-Downsampler/assets/99224673/7ab1b11f-a09d-4f86-bac2-c159b673bab2)
