Pointcloud Downsampler
This is an octree implementation of downsampling by removing random cluster
Create an octree by using Octree(csv_data, max_points_per_octant)
Then downsample by tree.downsample(coefficient, filename.csv)

-CURRENT VERSION
Example of a down sampling by random deletion from clusters with a max octant capacity of 4 and a downsampling coefficient of .5

Result was a loss of 65% of points, and a decrease in file size of 64% - 10,056 KB -> 3,669 KB, result was visually clearer, and maintaned large structures more efficiently


![downsampler github 2](https://github.com/charwhit20/Pointcloud-Downsampler/assets/99224673/a79eb09c-7098-43e7-8b29-5390def8e114)


-PREVIOUS VERSION
Example of down sampling by random leaf deletion with max octant capacity of 4 (removing clusters of 32 -> 8 * 4), and downsampling coeefficient of .8 (include only 80% of the leaves in the octree)

Result was a loss of 40% of points, and a decrease in file size of 37% - 10,056 KB -> 6,308 KB


![downsampler github](https://github.com/charwhit20/Pointcloud-Downsampler/assets/99224673/7ab1b11f-a09d-4f86-bac2-c159b673bab2)

