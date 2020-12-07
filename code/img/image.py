import numpy as np
import png
from numpy import random as rd

resolution=[1920,1080]

def GeneratePixel():
	pixel=[rd.randint(255), rd.randint(255),rd.randint(255)]
	return pixel

def GenerateLineOfPixels(pixel_number,chunks):
	pixels=[GeneratePixel() for _ in range(chunks)]
	print(f'The program generated {chunks} pixels')
	for pixel in pixels:
		print(f'p={pixel}')
	pixel_window=int(pixel_number/chunks)
	print(f'There will be {chunks} colors that spread across the width {pixel_number}, each with a sub_width of {pixel_window}')
	pixel_list=[]
	for pixel in pixels:
		for _ in range(pixel_window):
			pixel_list.extend(pixel)
	return pixel_list

#the number of chunks represents how many random colors will be generated for a single pixel line (e.g. if n.o. chunks is 3, then the image will have 3 rows of random colors when full image is generated
chunks=10
list_of_pixels=GenerateLineOfPixels(1920,chunks)

#uses the line of pixels generated with GenerateLineOfPixels to create a list of lines
def GenerateImage(pixel_list,height):
	image=[]
	for _ in range(height):
		image.append(pixel_list)
	return image

pixel_line=GenerateImage(list_of_pixels,resolution[1])
 
image=png.from_array(pixel_line,'RGB')
image.save('my_image.png')
