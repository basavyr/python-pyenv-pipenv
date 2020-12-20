import numpy as np
import png
from numpy import random as rd


out_file='./graphs_output/'
# Resolution
width, height = 30, 20

resolution = f'Screen res: {width}x{height} px'

print(resolution)

def GenerateBG(width,height):
    # Steelblue color (testing)
    pixel=[70,130,180]
    bg=[]
    line_of_pixels=[]
    for _ in range(width):
        line_of_pixels.extend(pixel)
    for _ in range(height):
        bg.append(line_of_pixels)
    return bg

bg=GenerateBG(1920,1080)
image=png.from_array(bg,'RGB')
image.save(f'{out_file}testBG.png')

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
