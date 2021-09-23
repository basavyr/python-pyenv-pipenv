import numpy as np
from numpy import random as rd

from scipy.stats import norm
# for installation of scipy the BLAS package was required (via Homebrew)
# full guide [here](https://github.com/numpy/numpy/issues/17784#issuecomment-729950525)

# according to the documentation, this is the superior way of using the random package within Python [https://numpy.org/doc/stable/reference/random/index.html#random-quick-start]
from numpy.random import default_rng
import matplotlib.pyplot as plt

rng = default_rng()


def draw_normal_dist(data_set, mu, sigma):
    """
    - Take a data-set containing values evenly spaced between a fixed value (the mean - mu)
    - Draw the normal distribution of the entire data-set
    - The spacing of the data set is given by the fixed value sigma - standard deviation of the sample.
    """
    x_data = np.array(data_set)
    y_data = norm.pdf(x_data, norm.pdf(x_data, mu, sigma))

    return [x_data, y_data]


def normal_dist(data_set, mu, sigma):

    inv_2pi = 1.0 / np.sqrt(2.0 * np.pi)
    exp_x = lambda x: np.exp(-0.5 * np.power(x, 2))
    inv_x = lambda x: 1.0 / x

    f_normal = lambda x, mu, sigma: inv_x(
        sigma) * inv_2pi * exp_x((x - mu) / sigma)

    normal_dist.f_normal = lambda x, mu, sigma: inv_x(
        sigma) * inv_2pi * exp_x((x - mu) / sigma)
    # normal_dist.f_normal = lambda x: 2 * x

    collection = []

    for x in data_set:
        set_tuple = [x, f_normal(x, mu, sigma)]
        collection.append(set_tuple)

    return collection


def auc_left(mu, sigma, distribution, left_limit):
    x_data = [x[0] for x in distribution]

    dx = [x_data[n] - x_data[n - 1] for n in range(1, len(x_data))]

    avg_dx = np.sum(dx) / len(dx)

    y_data = [x[1] * avg_dx for x in distribution]

    summer = 0
    for x in x_data:
        # print(x, normal_dist.f_normal(x, mu, sigma))
        summer += normal_dist.f_normal(x, mu, sigma) * avg_dx

    print(summer, np.sum(y_data))

    # x0 = np.array(rd.normal(0, 0.2, 100))
    # x1 = np.array(rd.standard_normal(100))
    # x2 = rng.standard_normal(100)

    # y = np.linspace(-1, 1, len(x0))

    # plt.plot(y, x1, '-r', label='data1')
    # plt.plot(y, x2, '--k', label='data2')
    # plt.legend(loc='best')
    # plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)

    # plot normal distribution with mean mu and standard deviation sigma
mu = 0
sigma = 1.69
test_data = np.linspace(-5, 5, 10000)
statistic = draw_normal_dist(test_data, mu, sigma)

n_dist = normal_dist(test_data, mu, sigma)
ndist_x = [x[0] for x in n_dist]
ndist_y = [x[1] for x in n_dist]

plt.plot(ndist_x, ndist_y, '-or', label='data')
plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)
plt.close()

auc_left(mu, sigma, n_dist, 1)

# plt.plot(statistic[0], statistic[1])
# plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)
# plt.close()

# for x0 in statistic:
#     print(x0)
