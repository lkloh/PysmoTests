import numpy as np 

"""made groups"""
fakeSignal = np.random.rand(40,3)

#print fakeSignal

"""compute correlations"""
numPts = len(fakeSignal)

"""
  @autocorrelations: numPts x numPts array
      columns: correspond to the individual windows
      rows: correspond to the autocorrelations for that particular window at the row number i, and the rest of the windows
            NaN value for a window and itself. 

"""
def get_autocorrelations(data):
	autocorrelations = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		current_comparison = fakeSignal[i,:]
		for j in xrange(numPts):
			if i==j: #do not check for 
				autocorrelations[i,i] = np.nan
			else:
				vec_j = fakeSignal[j,:]
				ccp = np.corrcoef(current_comparison, vec_j)
				autocorrelations[i,j] = ccp[0,1]
	return autocorrelations

autocorrelations = get_autocorrelations(fakeSignal)
print autocorrelations

"""computer median absolute deviation (MAD)"""
reshaped_autocorrelations = autocorrelations.reshape(numPts*numPts,1)
median1 = np.median(reshaped_autocorrelations)
MAD = np.median(reshaped_autocorrelations-median1)

"""detect and store window pairs 5 times above MAD
   window pairs with respect to original
"""
DetectionThreshold = 5*MAD

"""
  @windowPairsDetected: numPts x numPts array
  	columns: correspond to individual windows
  	rows: for that column, correspond to the windows other than itself where the correlation value exceeds the detection threshold
"""
def detect_window_pairs(autocorrelations, threshold):
	windowPairsDetected = np.zeros(shape=(numPts, numPts))
	autocorrelations = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		for j in xrange(numPts):
			if autocorrelations[i,j]>threshold:
				windowPairsDetected = 1
				print 'YOLO'
	return windowPairsDetected


windowPairsDetected = detect_window_pairs(autocorrelations, DetectionThreshold)
print windowPairsDetected















