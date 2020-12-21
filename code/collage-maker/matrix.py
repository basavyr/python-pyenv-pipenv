import numpy as np
import png
from numpy import random as rd


out_file = './graphs_output/'

# Resolution
width, height = 30, 20
resolution = f'Screen res: {width}x{height} px'


def SaveImage(img, path):
    image = png.from_array(img, 'RGB')
    image.save(f'{path}testBG.png')


def GenerateBG(width, height, n_pics):
    # Steelblue color (testing)
    pixel = [70, 130, 180]

    # Random color pixel
    rd_pixel = [rd.randint(0, 256), rd.randint(0, 256), rd.randint(0, 256)]

    line_of_pixels = []
    if (n_pics == 2):
        for _ in range(int(width/2)):
            line_of_pixels.extend(pixel)
        for _ in range(int(width/2)):
            line_of_pixels.extend(rd_pixel)

    bg = []
    for _ in range(height):
        bg.append(line_of_pixels)
    return bg


bg = GenerateBG(1920, 1080, 2)
SaveImage(bg, out_file)


# def GenerateMatrix(width, height):
#     l = np.linspace(1, 100, width)
#     ret_m = np.array([l])
#     for _ in range(height-1):
#         line = np.array(l)
#         ret_m = np.vstack([ret_m, line])
#     return ret_m


# def ShowMatrix(mat):
#     id = 1
#     for row in mat:
#         print(f'Row id={id}: {row}')
#         id = id+1


# m = GenerateMatrix(width, height)

# print(f'Size of M: {np.size(m,axis=1)}x{np.size(m,axis=0)} pixels')


# # ShowMatrix(bg)

# # print(np.vstack([bg,[1,2,2]]))
