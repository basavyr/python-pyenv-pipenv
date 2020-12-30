#!/Users/robertpoenaru/.pyenv/shims/python
import numpy as np
import matplotlib.pyplot as plt

def ShowSpins(spins):
	for spin in spins:
		print(f'{int(2.0*spin)} / 2')

def ShowData(spins,energies):
	print('I [\hbar] , E [MeV]')
	for spin, energy in zip(spins,energies):
		print(f'{int(2.0*spin)}/2 , {energy}')

spin1=np.arange(25.0/2.0,89.0/2.0+2.0,2.0)

spin2=np.arange(27.0/2.0,91.0/2.0+2.0,2.0)

# Energies are in MeV

# Energies of the YRAST band (that is favored signature band)
tsd1=[2.5145, 2.9008, 3.3511, 3.8664, 4.445, 5.084, 5.781, 6.5336, 7.3391,8.1969, 9.1066, 10.0692, 11.0857, 12.1568, 13.283, 14.4623, 15.689]

# Energies of the TSD2 band (that is unfavored signature band) - the partner of TSD1
tsd2=[3.0793,3.4866,3.9583,4.4926,5.0883,5.7429,6.4542,7.2204,8.0403,8.9132,9.8397,10.8199,11.8546,12.9435,14.0865,15.284,16.531]


ShowData(spin1,tsd1)

stagg=lambda x: (x[1]-x[0])

energies=zip(tsd1,tsd2)
deltas=list(map(stagg,energies))

print(deltas)

plt.plot(spin2,deltas,'--r',label='transition energies')
plt.savefig('transitions.pdf',dpi=300,bbox_inches='tight')
plt.close()
