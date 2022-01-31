import numpy as np
from random import randrange, uniform
from matplotlib import pyplot as plt


def giveUniformNumber(seed):
    """
    return a random number using uniform
    """
    retval = uniform(-seed, seed)
    return retval


def giveRandNumber(seed):
    """
    return a random number using randrange
    """
    retval = randrange(-seed, seed)
    return retval


def generateArray(size, seed, type):
    ret_arr = []
    for idx in range(size):
        if(type == 'rand'):
            ret_arr.append(giveRandNumber(seed))
        elif type == 'uniform':
            ret_arr.append(giveUniformNumber(seed))
    return ret_arr


def plotter_2y(xdata, ydata1, ydata2, labels):
    plot_file = 'random_data.pdf'

    plt.plot(xdata, ydata1, '-b', label=labels[0])
    plt.plot(xdata, ydata2, '-r', label=labels[1])

    plt.xlabel('x')
    plt.ylabel('arr')
    plt.legend(loc='best')
    plt.savefig(plot_file, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.close()


def main():
    # fixed seed for the array generator
    my_seed = 5
    # generate the data for graphical representation
    x = [i for i in range(101)]
    y_randrange = generateArray(len(x), my_seed, 'rand')
    y_uniform = generateArray(len(x), my_seed, 'uniform')
    labels = ['rand_data', 'uniform']


if __name__ == '__main__':
    main()
