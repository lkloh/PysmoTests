import numpy as np 
import random as rand

fakeSignal = rand.sample(range(-50,50), 20)
print fakeSignal

delta = 0.5

window = 5
overlap = 1

# transform fakeSignal to sliding windows

totalDataPoints = len(fakeSignal)
numPointsInWindow = int(window/delta)
numPointsInOverlap = int(overlap/delta)

numWindows = int((totalDataPoints-numPointsInWindow)/numPointsInOverlap + 1)

splitToWindows = np.zeros(shape=(numWindows, numPointsInWindow))

for i in xrange(numWindows):
	start_index = i*numPointsInOverlap
	for j in xrange(numPointsInWindow):
		splitToWindows[i,j] = fakeSignal[start_index+j]

print splitToWindows
