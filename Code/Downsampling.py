
def downsample(pcd, factor=0.2):
    downsample_pcd = pcd.voxel_down_sample(voxel_size=factor)
    return downsample_pcd