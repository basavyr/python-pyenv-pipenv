import numpy as np

# Resolution
width, height = 1920, 1080

resolution=f'Screen res: {width}x{height} px'

bg = np.array([[1, 2, 3], [3, 2, 1]])

print(resolution)

def GenerateMatrix(width, height):
    l=np.linspace(1,100,width)
    ret_m=np.array([l])
    for _ in range(height-1):
        line=np.array(l)
        ret_m=np.vstack([ret_m,line])
    return ret_m
    


def ShowMatrix(mat):
    id=1
    for row in mat:
        print(f'Row id={id}: {row}')
        id=id+1

m=GenerateMatrix(width,height)
print(np.size(m,axis=0))

# ShowMatrix(bg)

# print(np.vstack([bg,[1,2,2]]))
