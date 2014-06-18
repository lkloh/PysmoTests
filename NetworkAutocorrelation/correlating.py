import numpy as np 

"""made groups"""
fakeSignal = 200*np.random.rand(40,3)

for j in range(20,30):
	fakeSignal[j,:] = np.random.rand(3)

for j in range(0,19):
	fakeSignal[j,:] = -fakeSignal[j,:]

print fakeSignal

"""compute correlations"""
numPts = len(fakeSignal)

autocorrelations = np.zeros(shape=(numPts, numPts))

for i in xrange(numPts):
	for j in xrange(numPts):
		vec_i = fakeSignal[i,:]
		vec_j = fakeSignal[j,:]
		ccf = np.corrcoef(vec_i, vec_j)
		autocorrelations[i,j]=ccf[1,0]

print autocorrelations

