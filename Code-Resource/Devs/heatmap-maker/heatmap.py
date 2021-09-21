#! /Users/robertpoenaru/.pyenv/shims/python

#source -> Plotting a 2D heatmap with Matplotlib
#SO POST -> https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib

import matplotlib.pyplot as plt
import numpy as np


def heatmap2d(arr: np.ndarray):
    graph = f'heatmap_smooth.pdf'
    plt.imshow(arr, cmap='PuBu')
    plt.colorbar()
    plt.xlabel(f'x')
    plt.ylabel(f'y')
    plt.title('x')
    # plt.legend(loc='best')
    plt.savefig(graph, dpi=400, bbox_inches='tight')


N = 4

test_array = np.arange(N*N)

print(test_array)

test_array = np.arange(N*N).reshape(N, N)

print(test_array)

# cout = open('heat_data.dat', 'w')

# for x in test_array:
#     cout.write(str(x)+'\n')

# cout.close()

# heatmap2d(test_array)
