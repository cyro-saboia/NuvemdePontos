import open3d as o3d
import numpy as np
import os
import cv2

path = r'test/'
path_to_save = r'output/'

# Carrega a imagem
for filename in os.listdir(path):
    img = cv2.imread(os.path.join(path,filename))

    # Converte a imagem em um array NumPy
    img_array = np.array(img)

    # Obtém as coordenadas dos pixels da imagem
    h, w, _ = img_array.shape
    x, y = np.meshgrid(np.arange(w), np.arange(h))
    z = img_array[:, :, 0]  # Usa o canal R como profundidade

    # Cria uma nuvem de pontos
    y_inv = h - 1 - y # Inverte a orientação da imagem
    pcd = np.column_stack([x.flatten(), y_inv.flatten(), z.flatten()])

    # Cria um objeto PointCloud do Open3D e define os pontos
    pcd_o3d = o3d.geometry.PointCloud()
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)

    # Salva a nuvem de pontos como um arquivo PLY
    o3d.io.write_point_cloud(path_to_save + filename.split('.')[0] + ".ply", pcd_o3d)

    # Visualiza a nuvem de pontos
    # o3d.visualization.draw_geometries([pcd_o3d])