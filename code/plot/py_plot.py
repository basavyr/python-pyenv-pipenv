import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd
print('This python script generates a high-quality plot')

def Energy(spin,a):
	e0=a*spin*(spin+1)
	e=2.5*e0-a*spin
	return e

def CreatePlotLine(S,E,label):
	plt.plot(S,E,'ok',label=f'{label}')
def CreatePlotLine2(S,E,label):
	plt.plot(S,E,'-r',label=f'{label}')
	

def GenerateEnergies(spin):
	return Energy(spin,rd.uniform(1.0,2.0))


spinvalues=np.arange(8.5,48.5,2.0)
avalues=1.69*np.ones(len(spinvalues))
avalues_th=1.67*np.ones(len(spinvalues))

energies=map(Energy,spinvalues,avalues)
energies_th=map(Energy,spinvalues,avalues_th)

envalues=list(energies)
envalues=list(map(lambda x: x+ rd.randint(1000),envalues))
envalues_th=list(energies_th)

# comment fig, axes=plt.subplots(2,2,figsize=(10,10),dpi=300)
# comment plt.xlabel(r'I $[\hbar]$')
# comment plt.ylabel(r'E [a.u.]'

# for ax in axes.flat:
#     ax.set(xlabel='x-label', ylabel='y-label')
# axes[0,0].scatter(spinvalues,list(map(GenerateEnergies,spinvalues)),label='rd-test-1')
# axes[0,1].scatter(spinvalues,list(map(GenerateEnergies,spinvalues)),label='rd-test-2')
# axes[1,0].scatter(spinvalues,list(map(GenerateEnergies,spinvalues)),label='rd-test-3')
# axes[1,1].scatter(spinvalues,list(map(GenerateEnergies,spinvalues)),label='rd-test-4')
# #CreatePlotLine(spinvalues,envalues,f'{avalues[0]}-exp')
# #CreatePlotLine2(spinvalues,envalues_th,f'{avalues[0]}-th')
# plt.legend()
# plt.savefig('plot.pdf',dpi=300,bbox_inches='tight')
