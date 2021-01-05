import matplotlib.pyplot as plt
import numpy as np


def Write(file, expr): return file.write(str(expr)+'\n')


fil = open('output.dat', 'w')

x_lim = 60
y_lim = 60
x_step = 1
y_step = 1

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.arange(-x_lim, x_lim+x_step, x_step),
                   np.arange(-y_lim, y_lim+y_step, y_step))

Write(fil, f'The meshgrid has an x-size of {len(x)}')
Write(fil, f'The meshgrid has an y-size of {len(y)}')
Write(fil, x)
Write(fil, y)

count = 0
for _x in x:
    count = count+1
    my_str = f'_x[{len(_x)}] | {count} = {_x}'
    # print(my_str)
    # Write(fil, my_str)

# Write(fil, x`)
# Write(fil, y)

# z = (1 - x / 2. + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# z = np.power(np.sin(x*np.pi/180.0), 2)+np.power(np.cos(y*np.pi/180.0), 2)
z = np.tan(x*np.pi/180.0)*np.tan(y*np.pi/180.0) + \
    np.power(np.sin(x*np.pi/180.0), 2)+np.power(np.cos(y*np.pi/180.0), 2)

Write(fil, len(z))
# Write(fil, z)

count = 0
for _x in z:
    count = count+1
    my_str = f'_x[{len(_x)}] | {count} = {_x}'
    # print(my_str)
    Write(fil, my_str)


# # x and y are bounds, so z should be the value *inside* those bounds.
# # Therefore, remove the last value from the z array.


z = z[:-1, :-1]
Write(fil, len(z))

count = 0
for _x in z:
    count = count+1
    my_str = f'_x[{len(_x)}] | {count} = {_x}'
    # print(my_str)
    Write(fil, my_str)


fil.close()

z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)

ax.set_title('Heatmap')

plt.xlabel(r'$x_{list}$')
plt.ylabel(r'$y_{list}$')

# set the limits of the plot to the limits of the data

ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)

plt.savefig('2heatmap.pdf', dpi=400, bbox_inches='tight')
