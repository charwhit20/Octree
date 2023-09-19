Pointcloud Downsampler
This is an octree implementation of downsampling by removing random cluster
Create an octree by using Octree(csv_data, max_points_per_octant)
Then downsample by tree.downsample(coefficient, filename.csv)


Example of down sampling with max octant capacity of 4 (removing clusters of 32 -> 8 * 4), and downsampling coeefficient of .8 (include only 80% of the leaves in the octree)

Result was a loss of 40% of points, and a decrease in file size of 37% - 10,056 KB -> 6,308 KB


![downsampler github](https://github.com/charwhit20/Pointcloud-Downsampler/assets/99224673/7ab1b11f-a09d-4f86-bac2-c159b673bab2)
