#! /Users/robertpoenaru/.pyenv/versions/3.8.6/envs/numerical/bin/python

import numpy as np

from numpy import random as rd

# used for sorting a list of tuples by specified tuple index
# source: https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
from operator import itemgetter

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


# mat_counter = 1
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

possible_shapes = []
for x in range(0, no_elems + 1):
    for y in range(0, no_elems + 1):
        if(x * y == no_elems):
            possible_shapes.append((x, y))

# testing the reshape of a matrix
# with open('matrix_reshape.dat', 'w') as mat_out:
#     for shape in possible_shapes:
#         reshape = m0.reshape(shape)
#         mat_out.write(str(reshape))
#         mat_out.write('\n')


def RemoveCols(matrix, n_cols):
    # print(matrix)
    # print(f'Trying to remove {n_cols} columns from the matrix...')
    try:
        # matrix = np.delete(matrix, slice(n_cols, len(matrix[0])), axis=1)
        matrix = np.delete(matrix, slice(
            len(matrix[0]) - n_cols, len(matrix[0])), axis=1)
    except IndexError as err:
        print('Cannot delete the number of columns which was selected.')
        print(f'Reason: {err}')
    else:
        return matrix


def RemoveRows(matrix, n_rows):
    # print(matrix)
    # print(f'Removing {n_rows} rows from the matrix...')
    try:
        matrix = np.delete(matrix, slice(
            len(matrix) - n_rows, len(matrix)), axis=0)
    except IndexError as err:
        print('Cannot delete the number of rows which was selected.')
        print(f'Reason: {err}')
    else:
        return matrix


def GetN_cols(matrix):
    ret_val = len(matrix[0])
    return ret_val

# m0 = matrices[0]
# RemoveCols(m0, 2)
# m0 = matrices[0]
# RemoveRows(m0, 2)

# for m in matrices:
#     print(m)
#     print(GetMSize(m))


full_data = []

sizes = list(map(GetN_cols, matrices))

for mat, size in zip(matrices, sizes):
    element = [mat, size]
    full_data.append(element)

# sorted_data = full_data.sort(key=lambda x: x[1])
sorted_data = sorted(full_data, key=itemgetter(1), reverse=True)

# print(sorted_data[0])

id = 0
with open('matrix_file.dat', 'w') as mat_data:
    for data in sorted_data:
        # print(data[1])
        current_matrix = data[0]
        mat_data.write(str(current_matrix))
        mat_data.write('\n')
        matrices[id] = current_matrix
        id = id + 1


def AdjustMatrix(m1, m2):
    delta1 = GetMSize(m1)[0] - GetMSize(m2)[0]
    delta2 = GetMSize(m1)[1] - GetMSize(m2)[1]
    m1 = RemoveRows(m1, delta1)
    m1 = RemoveCols(m1, delta2)
    return m1


m1 = matrices[0]
m2 = matrices[1]

print(m1)

# m1 = RemoveCols(m1, 1)
# m1 = RemoveRows(m1, 1)

m1 = AdjustMatrix(m1, m2)

print(m1)
print(m2)

# AdjustMatrix(m1, m2)

# print(m1)
# print(m2)
# print(delta1)
# print(delta2)
# with open('matrix_file.dat', 'w') as mat_data:
#     id = 1
#     for mat in matrices:
#         mat_data.write(f'Matrix {id}')
#         mat_data.write('\n')
#         mat_data.write(str(mat))
#         mat_data.write('\n')
#         id = id + 1
