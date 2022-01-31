import numpy as np
from random import randrange, uniform
from matplotlib import pyplot as plt


def giveRandomNumber(seed):
    retval = randrange(-seed, seed)
    return retval


def generateArray(size, seed):
    ret_arr = []
    for idx in range(size):
        ret_arr.append(giveRandomNumber(seed))
    return ret_arr


# fixed seed for the array generator
my_seed = 5

x = [i for i in range(101)]
y = generateArray(len(x), my_seed)

plt.plot(x, y, '-ob', label='data')
plt.xlabel('x')
plt.ylabel('arr')
plt.legend(loc='best')
plt.savefig('random_data.pdf', dpi=300, bbox_inches='tight')
plt.close()