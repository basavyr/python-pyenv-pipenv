import matplotlib.pyplot as plt
from numpy import random as rd
import numpy as np

xs=np.linspace(0,10,100)


def my_f(arg):
	if(not arg):
		arg=1
	return arg+np.log(arg)+np.exp(np.power(arg,0.5))

ys=list(map(my_f,xs))

y2=[x for x in range(10,100)]
y3=rd.uniform(10,100, size=(1,10))


y4=list(map(lambda x: rd.uniform(0,1)*x,xs))

plt.errorbar(xs,ys,yerr=y4)
plt.savefig("errorplot.pdf",bbox_inches='tight')
