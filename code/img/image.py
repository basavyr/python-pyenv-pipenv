import png

resolution=[1920,1080]

color=(255,0,0)
pixel1=(100,128,128)
pixel2=(200,128,75)
pixels=[]
[pixels.extend(value for value in pixel1) for _ in range(resolution[0])]
#print(pixels,len(pixels))
list_of_pixels=[]
for _ in range(resolution[1]):
	list_of_pixels.append(pixels)
image=png.from_array(list_of_pixels,'RGB')
image.save('my_image.png')
