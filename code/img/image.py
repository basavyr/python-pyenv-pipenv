import numpy as np
import png
from numpy import random as rd

resolution=[1920,1080]

def GeneratePixel():
	pixel=[rd.randint(255), rd.randint(255),rd.randint(255)]
	return pixel

def GenerateLineOfPixels(pixel_number,chunks):
	pixels=[GeneratePixel() for _ in range(chunks)]
#	print(f'The program generated {chunks} pixels')
#	for pixel in pixels:
#		print(f'p={pixel}')
	pixel_window=int(pixel_number/chunks)
#	print(f'There will be {chunks} colors that spread across the width {pixel_number}, each with a sub_width of {pixel_window}')
	pixel_list=[]
	for pixel in pixels:
		for _ in range(pixel_window):
			pixel_list.extend(pixel)
	return pixel_list

def GenerateImage(name,chunks):
	height=resolution[1]
	width=resolution[0]
	#uses the line of pixels generated with GenerateLineOfPixels to create a list of lines
	list_of_pixels=GenerateLineOfPixels(width,chunks)

	bg=[]

	#the number of chunks represents how many random colors will be generated for a single pixel line (e.g. if n.o. chunks is 3, then the image will have 3 rows of random colors when full image is generated
	for _ in range(height):
		bg.append(list_of_pixels)
	image=png.from_array(bg,'RGB')
	image.save(f'{name}.png')

path="./images/"
# create a dictionary with some words that will be used for image names
file_names=[]
#set the number of images to be created at script runtime
image_number=15
image_names=[path+"image-"+str(id) for id in range(image_number)]

for image in image_names:
	GenerateImage(image,5)

