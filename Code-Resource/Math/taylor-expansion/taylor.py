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

plt_y = lambda n, lbl: plt.plot(xdata, coeff_list(n), '-b', label=f'c_n={lbl}')


plt_y(1, 1)
plt_y(2, 2)
plt.legend(loc='best')
plt.show()
plt.close()
