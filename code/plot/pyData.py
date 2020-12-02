# import the energies for Lu163 and create a connected list of energies

# alternate between the energies of each band, such that the final array represents a sorted list by the spin-value rather than the actual value of the energy.

from operator import itemgetter

tsd1 = [1.97023, 2.25606, 2.59742, 2.99431, 3.44673, 3.95468, 4.51816,5.13716, 5.81168, 6.54173, 7.3273, 8.16839, 9.065, 10.0171, 11.0248, 12.088, 13.2067, 14.381, 15.6107, 16.896, 18.2369]
tsd2 = [3.08893, 3.51358, 3.99377, 4.52948, 5.12072, 5.76748, 6.46976,7.22757, 8.0409, 8.90976, 9.83413, 10.814, 11.8495, 12.9404, 14.0869, 15.2889, 16.5464]
tsd3 = [3.78228, 4.31386, 4.89878, 5.5373, 6.22966, 6.97603, 7.7766, 8.63151,9.54089, 10.5049, 11.5235, 12.5969, 13.7252, 14.9084]
tsd4 = [6.06748, 6.76976, 7.52757, 8.3409, 9.20976, 10.1341, 11.114, 12.1495,13.2404, 14.3869] 

# add index next to the energies from each band

# data1=[]
# 
# spinZero=8.5
# for x in tsd1:
# 	x_item=[spinZero,x]
# 	data1.append(x_item)
# 	spinZero=spinZero+2.0
# 	
# print(data1)
# 
# data1.sort(key=itemgetter(0))
# 
# 
# print(data1)

# encode in a method the above procedure


#generate the data tuple with all the spins and energies for the four TSD bands

data=[]

spin01=8.5
spin02=13.5
spin03=16.5
spin04=23.5
for x in tsd1:
	data.append([spin01,x])
	spin01=spin01+2.0
for x in tsd2:
	data.append([spin02,x])
	spin02=spin02+2.0
for x in tsd3:
	data.append([spin03,x])
	spin03=spin03+2.0
for x in tsd4:
	data.append([spin04,x])
	spin04=spin04+2.0

def generateBand(spin0,energies):
	s=spin0
	data=[]
	for x in energies:
		x_item=[s,x]
		data.append(x_item)
		s=s+2.0
	# sort the array
	data.sort(key=itemgetter(0))
	return data

#print(data)
data.sort(key=itemgetter(0))
#print(data)

for x in data:
	print("{",x[0],",",x[1],"},")
