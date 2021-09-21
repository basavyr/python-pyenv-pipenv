import numpy as np
from numpy import random as rd

from scipy.stats import norm
# for installation of scipy the BLAS package was required (via Homebrew)
# full guide [here](https://github.com/numpy/numpy/issues/17784#issuecomment-729950525)

# according to the documentation, this is the superior way of using the random package within Python [https://numpy.org/doc/stable/reference/random/index.html#random-quick-start]
from numpy.random import default_rng
import matplotlib.pyplot as plt

rng = default_rng()

# x0 = np.array(rd.normal(0, 0.2, 100))
# x1 = np.array(rd.standard_normal(100))
# x2 = rng.standard_normal(100)

# y = np.linspace(-1, 1, len(x0))

# plt.plot(y, x1, '-r', label='data1')
# plt.plot(y, x2, '--k', label='data2')
# plt.legend(loc='best')
# plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)


x = np.linspace(-5, 5, 100)

# plot normal distribution with mean mu and standard deviation sigma
mu = 0
sigma = 1.69
plt.plot(x, norm.pdf(x, mu, sigma))
plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)
plt.close()

for x0 in x:
    print(x0)
