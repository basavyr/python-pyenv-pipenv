import png
color=(255,0,0)
pixels=[128,2,3,120,2,3,120,2,3,
        128,2,3,128,2,3,120,2,3]
list_of_pixels=[]
for _ in range(100):
	list_of_pixels.append(pixels)
image=png.from_array(list_of_pixels,'RGB')
image.save('my_image.png')
