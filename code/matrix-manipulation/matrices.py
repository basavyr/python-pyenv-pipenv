#! /Users/robertpoenaru/.pyenv/versions/3.8.6/envs/numerical/bin/python

import numpy as np

from numpy import random as rd

# set the limit for MINIMUM randomized number used within calculations
RAND_LIM_0 = 1
# set the limit for MAXIMUM randomized number used within calculations
RAND_LIM_1 = 4


def GenerateMatrix(N, M):
    m = rd.randint(RAND_LIM_0, RAND_LIM_1, (N, M))
    return m


for _ in range(3):
    N = rd.randint(RAND_LIM_0, RAND_LIM_1)
    M = rd.randint(RAND_LIM_0, RAND_LIM_1)
    print(f'{N} and {M} were randomly chosen for dimensions of the matrix')
    print(GenerateMatrix(N, M))
