#! /Users/robertpoenaru/.pyenv/versions/3.8.6/envs/numerical/bin/python

import numpy as np

from numpy import random as rd

# set the limit for MINIMUM randomized number used within calculations
RAND_LIM_0 = 0
# set the limit for MAXIMUM randomized number used within calculations
RAND_LIM_1 = 2


def GenerateMatrix(N, M):
    m = rd.randint(RAND_LIM_0, RAND_LIM_1, (N, M))
    return m


def GetMSize(M):
    n_rows = len(M)
    n_cols = len(M[0])
    size = [n_rows, n_cols]
    # print(f'The matrix has dimensions NxM: {n_rows}')
    return size


# for _ in range(3):
#     # N = rd.randint(RAND_LIM_0, RAND_LIM_1)
#     # M = rd.randint(RAND_LIM_0, RAND_LIM_1)
#     N = RAND_LIM_0
#     M = RAND_LIM_1
#     Mat = GenerateMatrix(N, M)
#     print(f'{N} and {M} were randomly chosen for dimensions of the matrix')
#     print(Mat)
#     print(
#         f'Dimension of the generated matrix is: {GetMSize(Mat)[0]}x{GetMSize(Mat)[1]}')


matrix_sizes = [(3, 4), (4, 5), (4, 4), (5, 1)]


mat_counter = 1
# for size in matrix_sizes:
#     n_rows = size[0]
#     n_cols = size[1]
#     print(f'Matrix {mat_counter}')
#     print(f'Size: {n_rows}x{n_cols}')
#     mat = GenerateMatrix(n_rows, n_cols)
#     print(mat)

matrices = [GenerateMatrix(size[0], size[1]) for size in matrix_sizes]

m0 = matrices[0]

no_elems = len(m0) * len(m0[0])

print(f'number of elements are {no_elems}')
print(matrices[0].reshape((4, 3)))

possible_shapes = []
for x in range(0, no_elems + 1):
    for y in range(0, no_elems + 1):
        if(x * y == no_elems):
            possible_shapes.append((x, y))

print(possible_shapes)

with open('matrix_reshape.dat', 'w') as mat_out:
    for shape in possible_shapes:
        reshape = m0.reshape(shape)
        mat_out.write(str(reshape))
        mat_out.write('\n')

# # for mat in matrices:

# new_matrices = [mat.reshape(3, 3) for mat in matrices]

# print(new_matrices)
