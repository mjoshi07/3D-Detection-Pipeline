
def ransac(pcd, iterations=10, tolerance=0.25):
    # fit a plane (ground) to the 3d points

    plane_model, inliers = pcd.segment_plane(distance_threshold=tolerance, ransac_n=3, num_iterations=iterations)

    inlier_cloud = pcd.select_by_index(inliers)
    outlier_cloud = pcd.select_by_index(inliers, invert=True)
    outlier_cloud.paint_uniform_color([1, 0, 0])  # R, G, B
    inlier_cloud.paint_uniform_color([0, 0, 1])  # R, G, B

    return inlier_cloud, outlier_cloud
