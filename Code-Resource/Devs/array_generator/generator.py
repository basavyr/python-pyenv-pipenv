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


# fixed seed for the array generator
my_seed = 5


x = [i for i in range(101)]
y_randrange = generateArray(len(x), my_seed, 'rand')
y_uniform = generateArray(len(x), my_seed, 'uniform')


plt.plot(x, y_randrange, '-b', label='rand_data')
plt.plot(x, y_uniform, '-r', label='uniform')
plt.xlabel('x')
plt.ylabel('arr')
plt.legend(loc='best')
plt.savefig('random_data.pdf', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.close()
