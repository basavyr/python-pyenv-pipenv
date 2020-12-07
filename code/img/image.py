import numpy as np
import png
from numpy import random as rd

resolution=[1920,1080]

def GeneratePixel():
	pixel=[rd.randint(255), rd.randint(255),rd.randint(255)]
	return pixel

def GenerateListOfPixels(pixel_number,chunks):
	pixels=[GeneratePixel() for _ in range(chunks)]
	pixel_window=int(pixel_number/chunks)
#	print(pixel_window)
	pixel_list=[]
	for pixel in pixels:
		current_list=[pixel for _ in range(pixel_window)]
		pixel_list.extend(current_list)
	return pixel_list

#the number of chunks represents how many random colors will be generated for a single pixel line (e.g. if n.o. chunks is 3, then the image will have 3 rows of random colors when full image is generated
chunks=10
list_of_pixels=GenerateListOfPixels(resolution[1],chunks)

print(list_of_pixels)

def GeneratePixelArray(pixel_list,width,height):
	image=[]
	for id in range(len(pixel_list)):
		image.extend(pixel for pixel in pixel_list[id])
	return image



pixel_line=GeneratePixelArray(list_of_pixels,resolution[0],resolution[1])

print(pixel_line,len(pixel_line))
#bg=[pixel_line for _ in range(resolution[1])]
#print(pixel_line)
#image=png.from_array(bg,'RGB')
#image.save('my_image.png')
