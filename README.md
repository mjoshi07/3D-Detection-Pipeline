# 3D Object Detection Pipeline
An unsupervised 3D Object detection pipeline using 3D LiDAR points 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/detection_pipeline.png" width=640/>
</p>

### Read the point clouds
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/loaded_pcl.png" width=640>
</p>

### Downsample the point clouds
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/downsample_pcl.png" width=640/>
</p>

### Segment the point clouds as inliers (objects of interest) and outliers (ground)
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/segment_pcl.png" width=640/>
</p>

### Clustering the inliers to individual objects
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/clustering_pcl.png" width=640/>
</p>

### Compute 3D bounding box for each cluster
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/bbox_pcl.png" width=640/>
</p>

## Result
<p align="center">
<img src="https://github.com/mjoshi07/3D-Detection-Pipeline/blob/main/Results/visualization.gif" width=640/>
</p>


## TODO
- [ ] References
- [ ] Details
- [ ] HDSCAN method
- [ ] Oriented Bounding Box
