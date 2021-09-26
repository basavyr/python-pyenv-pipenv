import numpy as np
from numpy import random as rd
from numpy.lib.function_base import disp
from datetime import datetime

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
    def exp_x(x): return np.exp(-0.5 * np.power(x, 2))
    def inv_x(x): return 1.0 / x

    def f_normal(x, mu, sigma): return inv_x(
        sigma) * inv_2pi * exp_x((x - mu) / sigma)

    normal_dist.f_normal = lambda x, mu, sigma: inv_x(
        sigma) * inv_2pi * exp_x((x - mu) / sigma)
    # normal_dist.f_normal = lambda x: 2 * x

    distribution = []

    for x in data_set:
        set_tuple = [x, f_normal(x, mu, sigma)]
        distribution.append(set_tuple)

    return distribution


def auc_left(mu, sigma, distribution, right_limit):
    """calculates the area under the curve by performing the Riemann summation starting from the left-most data point and up to the right limit"""
    x_data = [x[0] for x in distribution]

    dx = [x_data[n] - x_data[n - 1] for n in range(1, len(x_data))]

    avg_dx = np.sum(dx) / len(dx)

    y_data = [x[1] * avg_dx for x in distribution]

    x_data_left = [x for x in x_data if x <= right_limit]

    sum_left = 0
    for x in x_data_left:
        sum_left += normal_dist.f_normal(x, mu, sigma) * avg_dx

    # print(sum_left, np.sum(y_data))

    return sum_left


def auc_right(mu, sigma, distribution, left_limit):
    """calculates the area under the curve by performing the Riemann summation starting from the left-limit (given as function argument) and the right-most data-point of the curve

    the distribution is made up elements of the form [x,f(x)]
    """
    x_data = [x[0] for x in distribution]

    dx = [x_data[n] - x_data[n - 1] for n in range(1, len(x_data))]

    avg_dx = np.sum(dx) / len(dx)

    y_data = [x[1] * avg_dx for x in distribution]

    x_data_right = [x for x in x_data if x >= left_limit]

    sum_right = 0
    for x in x_data_right:
        sum_right += normal_dist.f_normal(x, mu, sigma) * avg_dx

    # print(sum_right, np.sum(y_data))

    return sum_right

    # x0 = np.array(rd.normal(0, 0.2, 100))
    # x1 = np.array(rd.standard_normal(100))
    # x2 = rng.standard_normal(100)

    # y = np.linspace(-1, 1, len(x0))

    # plt.plot(y, x1, '-r', label='data1')
    # plt.plot(y, x2, '--k', label='data2')
    # plt.legend(loc='best')
    # plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)

    # plot normal distribution with mean mu and standard deviation sigma


def auc(mu, sigma, distribution, left_limit, right_limit):
    """Calculates the area under the curve for the normal distribution function my performing the Riemann summation from the left liimit (given as argument) to the right limit (also given as a function argument)
    """


# declare the set of constant parameters to be used for simulations
mu = 0
sigma = 1.69
left_limit = -2
right_limit = 2
delta = 5  # how much should the normal curve "spread" from the mean


def Create_Dist_Plot(distribution,  plot_file):
    # prepare the data from the distribution
    ndist_x = [x[0] for x in distribution]
    ndist_y = [x[1] for x in distribution]

    fig, ax = plt.subplots()

    plt.plot(ndist_x, ndist_y, '-or', label='data')
    plt.text(0.20, 0.85, f'{datetime.utcnow()}', horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes, fontsize=8)
    plt.savefig(plot_file, bbox_inches='tight', dpi=300)
    ax.set_title(f'Title')
    ax.set_ylabel(f'P(x)')
    ax.set_xlabel(f'x')
    plt.close()


# the curve that is drawn automatically using the norm module from scipy.stats
def normal_dist_statistic(
    test_data): return draw_normal_dist(test_data, mu, sigma)


if __name__ == '__main__':
    # create a test plot with a testing normal distribution
    plot_file = 'normal_plot.pdf'
    test_data = np.linspace(-delta, delta, 100)
    n_dist = normal_dist(test_data, mu, sigma)

    Create_Dist_Plot(n_dist, plot_file)

    # auc_left(mu, sigma, n_dist, -1)
    # auc_right(mu, sigma, n_dist, -1)
