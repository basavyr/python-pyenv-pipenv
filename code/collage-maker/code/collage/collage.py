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
test_image2 = './input_imgs/testBG2.png'

input_images = [test_image, test_image2]

# output -> place to store the resulted figures
image_output_as_pixles = '../../output/images/pixels.dat'

# File to store the arrays obtained from reading each image
pixel_data = 'pixels.dat'


def ReadImage(img_file):
    im_arr = None
    print(im_arr)
    try:
        im = Image.open(img_file)
    except OSError as err:
        print('could not import the image')
        print(f'Error: {err}')
    else:
        im_arr = np.array(im)
        print(im_arr)
        # plt.imshow(im_arr) -> still doesn't work
    return im_arr


def ShowPixels(img_arr, pixel_file):
    i = 1
    for line in img_arr:
        pixel_file.write(f'Image-Line {i}:\n')
        j = 1
        for pixel in line:
            c_str = f'p[ {i} , {j} ]={pixel}'
            # print(c_str)
            pixel_file.write(c_str + '\n')
            id = 1
            for color in pixel:
                c_str = f'color[ {id} ]={color}'
                # print(c_str)
                pixel_file.write(c_str + '\n')
                id = id + 1
            j = j + 1
        i = i + 1


with open(pixel_data, 'w') as pixel_file:
    for img in input_images:
        img_arr = ReadImage(img)
        pixel_file.write(f'Reading data from image {img}')
        pixel_file.write('\n')
        ShowPixels(img_arr, pixel_file)


# xx = open(image_output_as_pixles, 'w')
# xx.write(str(im_arr))
# xx.close()

# read_img = imread(test_image)
# print(type(read_img))

# for line in read_img:
#     print(line)
