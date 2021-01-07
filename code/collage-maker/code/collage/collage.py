#! /Users/robertpoenaru/.pyenv/shims/python

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

im = Image.open(test_image)  # These two lines
im_arr = np.array(im)  # are all you need
# plt.imshow(im_arr)


xx = open(image_output_as_pixles, 'w')
xx.write(str(im_arr))
xx.close()

# read_img = imread(test_image)
# print(type(read_img))

# for line in read_img:
#     print(line)
