#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math


class Taylor:
    @staticmethod
    def c(n, a, x):
        fact = math.factorial(n)
        term = np.power(x - a, n)
        return fact * term


test = Taylor()

xdata = [i for i in range(0, 10)]
coeff_list = lambda n: [test.c(n, 0, x)for x in xdata]
plt.plot(xdata, coeff_list(1), '-r', label='test poly')
plt.plot(xdata, coeff_list(2), '-b', label='test poly')
plt.show()
plt.close()
