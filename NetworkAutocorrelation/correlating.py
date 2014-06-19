import numpy as np 
np.set_printoptions(threshold=np.nan)

"""made groups
   40: # windows available
   7: # points in each window
"""
fakeSignalA = np.random.rand(40,7)
fakeSignalB = np.random.rand(40,7)
fakeSignalC = np.random.rand(40,7)

#print fakeSignal

"""compute correlations"""
numPts = len(fakeSignalA)

"""
  @autocorrelations: numPts x numPts array
      columns: correspond to the individual windows
      rows: correspond to the autocorrelations for that particular window at the row number i, and the rest of the windows
            NaN value for a window and itself. 

"""
def get_autocorrelations(data):
	autocorrelations = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		current_comparison = data[i,:]
		for j in xrange(numPts):
			if i==j: #do not check for 
				autocorrelations[i,i] = np.nan
			else:
				vec_j = data[j,:]
				ccp = np.corrcoef(current_comparison, vec_j)
				autocorrelations[i,j] = ccp[0,1]
	return autocorrelations

autocorrelationsA = get_autocorrelations(fakeSignalA)
autocorrelationsB = get_autocorrelations(fakeSignalB)
autocorrelationsC = get_autocorrelations(fakeSignalC)

"""computed median absolute deviation (MAD)
   formula here: http://en.wikipedia.org/wiki/Median_absolute_deviation
"""
def compute_median_absolute_deviation(autocorrelations):
	numPts = len(autocorrelations)
	reshaped_autocorrelations = autocorrelations.reshape(numPts*numPts,1)
	median1 = np.median(reshaped_autocorrelations)
	abs_diff = np.abs(reshaped_autocorrelations-median1)
	return np.median(abs_diff)

# sum all of them
network_correlation_coefficient = autocorrelationsA+autocorrelationsB+autocorrelationsC
MAD = compute_median_absolute_deviation(network_correlation_coefficient)
print 'MAD: %f' % MAD

"""detect and store window pairs 5 times above MAD
   window pairs with respect to original

   @windowPairsDetected: numPts x numPts array
   columns: correspond to individual windows
   rows: for that column, correspond to the windows other than itself where the correlation value exceeds the detection threshold
"""
def detect_window_pairs(autocorrelations, threshold):
	print 'threshold: %f' % threshold
	windowPairsDetected = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		for j in xrange(numPts):
			if autocorrelations[i,j] >= threshold:
				windowPairsDetected[i,j] = 1
				print 'Detected possible window event'
	return windowPairsDetected

windowPairsDetected = detect_window_pairs(network_correlation_coefficient, 3*MAD)

"""save all window pairs as candidate events"""
def get_candidate_events(windowPairsDetected, windows_array):
	candidate_events = []
	for i in xrange(numPts):
		detection_row = windowPairsDetected[i,:]
		has_event = False
		for j in xrange(numPts):
			if detection_row[j]:
				has_event = True
				candidate_events.append(windows_array[i,:])
				print windows_array[i,:]
				break

candidate_events = get_candidate_events(windowPairsDetected, fakeSignalA)

print 'candidate event windows: '
print candidate_events

"""
   apply waveform cross-correlation

"""

















