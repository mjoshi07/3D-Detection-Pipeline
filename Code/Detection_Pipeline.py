import time
import numpy as np
import open3d as o3d
import Downsampling as ds
import Segmentation as sg
import Clustering as cl
import BoundingBoxes as bb


def detection_pipeline(pcl_file, downsample_factor=0.25, iterations=100, tolerance=0.3, eps=0.4, min_points=5, debug=True):
    pcd = o3d.io.read_point_cloud(pcl_file)
    if debug:
        print(len(np.asarray(pcd.points)))
        o3d.visualization.draw_geometries([pcd])
    t = time.time()
    downsample_pcd = ds.downsample(pcd, downsample_factor)
    if debug:
        print("Downsample Time", time.time() - t)
        o3d.visualization.draw_geometries([downsample_pcd])

    t = time.time()
    inlier_pts, outlier_pts = sg.ransac(downsample_pcd, iterations=iterations, tolerance=tolerance)
    if debug:
        print("Segmentation Time", time.time() - t)
        o3d.visualization.draw_geometries([outlier_pts, inlier_pts])

    t = time.time()
    outlier_pts, labels = cl.dbscan(outlier_pts, eps=eps, min_points=min_points, print_progress=False, debug=debug)
    if debug:
        print("Clustering Time", time.time() - t)
        o3d.visualization.draw_geometries([outlier_pts, inlier_pts])

    t = time.time()
    bboxes = bb.oriented_bbox(outlier_pts, labels)

    outlier_with_bboxes = [outlier_pts]
    outlier_with_bboxes.extend(bboxes)
    outlier_with_bboxes.append(inlier_pts)
    if debug:
        print("Bounding Boxes Time", time.time() - t)
        o3d.visualization.draw_geometries(outlier_with_bboxes)

    return outlier_with_bboxes


if __name__ == "__main__":
    pcl_file = "../Data/test_files/UDACITY/0000000008.pcd"
    a = detection_pipeline(pcl_file, debug=True)
