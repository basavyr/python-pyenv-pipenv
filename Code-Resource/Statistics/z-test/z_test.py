import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

x1 = np.array(rd.standard_normal(100))

print(x1)

x = np.array(rd.normal(0, 0.2, 100))

y = np.linspace(0, 100, len(x))


plt.plot(y, x1, '-r', label='data')
plt.legend(loc='best')
plt.savefig('normal_plot.pdf', bbox_inches='tight', dpi=300)
plt.close()
