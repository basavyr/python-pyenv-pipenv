import matplotlib.pyplot as plt 
import numpy as np
from numpy import random as rd

y=list(np.arange(0,100,20))

rand = lambda x: rd.randint(10,100)+x

l1=list(map(rand,y))
l2=list(map(rand,y))

path='./graphs_output/'

plt.plot(l1,'-r',label='beta1')
plt.plot(l2,'ok',label='beta2')
plt.legend(loc='best')
plt.savefig(path+'show.pdf',dpi=3000,bbox_inches='tight')
