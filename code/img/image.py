import png
color=(255,0,0)
p = [(255,0,0, 0,255,0, 0,0,255),
     (128,0,0, 0,128,0, 0,0,128)]
pp=[(222,1,1)]
f = open('swatch.png', 'wb')
w = png.Writer(1, 1, greyscale=False)
w.write(f, pp)
f.close()
