import open3d as o3d
import numpy as np
import struct
size_float = 4
list_pcd = []

file_to_open = "test_files/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151605047769.pcd.bin"
file_to_save = "test_files/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151605047769.pcd"
with open (file_to_open, "rb") as f:
    byte = f.read(size_float*4)
    while byte:
        x,y,z,intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z])
        byte = f.read(size_float*4)
np_pcd = np.asarray(list_pcd)
pcd = o3d.geometry.PointCloud()
v3d = o3d.utility.Vector3dVector
pcd.points = v3d(np_pcd)

o3d.io.write_point_cloud(file_to_save, pcd)
