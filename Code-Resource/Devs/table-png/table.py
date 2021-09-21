#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt

#import scipy as sp
#import pandas as pd
l1 = np.arange(0, 100, 10)

l2 = np.arange(0, 1000, 100)


def My_Function(x, y):
    try:
        assert (x > 0)
    except AssertionError:
        return False
    else:
        term = np.log(x*y-np.sqrt(x*y))
        return term


def SameLength(l1, l2):
    if (len(l1) == len(l2)):
        return True
    return False


def TestLists(l1, l2):
    try:
        sl = SameLength(l1, l2)
        assert sl == True
    except AssertionError:
        print(f'The two lists do not have the same length!')
        print(f'[ l1= {len(l1)} | l2= {len(l2)} ]')
    else:
        print(f'All good')
        print(f'l1= {l1}')
        print(f'l2= {l2}')
    finally:
        pass


l3 = list(map(My_Function, l1, l2))


# l0 = [False, 1, 2, 43, False]


# l0 = [l for l in l0 if l != False]


l3 = list(filter(lambda a: a != False, l3))


print(l3)
