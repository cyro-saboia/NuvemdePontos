import os
import cv2
import open3d as o3d
import imageio.v3 as iio

path = r'output/'

# Carrega a imagem
for filename in os.listdir(path):
    pcd = o3d.io.read_point_cloud(os.path.join(path,filename))
    o3d.visualization.draw_geometries([pcd])
