import pandas as pd


def oriented_bbox(pcd, labels, min_points=30, max_points=400):
    obbs = []
    indices = pd.Series(range(len(labels))).groupby(labels, sort=False).apply(list).tolist()

    for i in range(len(indices)):
        num_points = len(pcd.select_by_index(indices[i]).points)
        if min_points < num_points < max_points:
            sub_cloud = pcd.select_by_index(indices[i])
            obb = sub_cloud.get_axis_aligned_bounding_box()
            obb.color = (0, 0, 0)
            obbs.append(obb)

    print(f"Number of Bounding Boxes calculated {len(obbs)}")

    return obbs
