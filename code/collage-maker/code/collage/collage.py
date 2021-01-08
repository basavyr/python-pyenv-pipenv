#! /Users/robertpoenaru/.pyenv/shims/python

# Sources
# [Convert image to a matrix in python] -> https://stackoverflow.com/questions/3493092/convert-image-to-a-matrix-in-python
# [Using the Image class] -> https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html
# [how to convert an RGB image to numpy array?] -> https://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
# [np.asarray] -> https://numpy.org/doc/stable/reference/generated/numpy.asarray.html

# Numpy
import numpy as np
from numpy import random as rd

# Pillow package
from PIL import Image

# Matplotlib package
import matplotlib.pyplot as plt
from matplotlib.image import imread

# Misc
import time
import datetime

# input images (collection)
test_image = './input_imgs/testBG.png'

# output -> place to store the resulted figures
image_output_as_pixles = '../../output/images/pixels.dat'

pixel_data = 'pixels.dat'

im = Image.open(test_image)  # These two lines
im_arr = np.array(im)  # are all you need
# plt.imshow(im_arr)


def ShowPixels(img_arr, output_data):
    i = 1
    with open(output_data, 'w') as pixel_file:
        for line in im_arr:
            j = 1
            for pixel in line:
                c_str = f'p[ {i} , {j} ]={pixel}'
                print(c_str)
                pixel_file.write(c_str + '\n')
                id = 1
                for color in pixel:
                    c_str = f'color[ {id} ]={color}'
                    print(c_str)
                    pixel_file.write(c_str + '\n')
                    id = id + 1
                j = j + 1
            i = i + 1


ShowPixels(im_arr, pixel_data)

# xx = open(image_output_as_pixles, 'w')
# xx.write(str(im_arr))
# xx.close()

# read_img = imread(test_image)
# print(type(read_img))

# for line in read_img:
#     print(line)
