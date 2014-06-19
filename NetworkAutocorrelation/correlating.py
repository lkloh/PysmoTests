import numpy as np 
np.set_printoptions(threshold=np.nan)

"""made groups
   40: # windows available
   20: # points in each window
"""

delta = 0.5
window = 3
overlap = 1

totalDataPoints = 40
numPointsInWindow = int(window/delta)
numPointsInOverlap = int(overlap/delta)

fakeSignalA = np.random.rand(totalDataPoints,numPointsInWindow)
fakeSignalB = np.random.rand(totalDataPoints,numPointsInWindow)
fakeSignalC = np.random.rand(totalDataPoints,numPointsInWindow)

#print fakeSignal

"""compute correlations
  @autocorrelations: numPts x numPts array
      columns: correspond to the individual windows
      rows: correspond to the autocorrelations for that particular window at the row number i, and the rest of the windows
            NaN value for a window and itself. 
"""
def get_correlations(data):
	numPts = len(data)
	all_correlations = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		current_comparison = data[i,:]
		for j in xrange(numPts):
			if i==j: #do not check for 
				all_correlations[i,i] = np.nan
			else:
				vec_j = data[j,:]
				ccp = np.corrcoef(current_comparison, vec_j)
				all_correlations[i,j] = ccp[0,1]
	return all_correlations

autocorrelationsA = get_correlations(fakeSignalA)
autocorrelationsB = get_correlations(fakeSignalB)
autocorrelationsC = get_correlations(fakeSignalC)

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
   rows: for that column, correspond to the windows other than itself where the 
         correlation value exceeds the detection threshold
"""
def detect_window_pairs(autocorrelations, threshold):
	print 'threshold: %f' % threshold
	numPts = len(autocorrelations)
	windowPairsDetected = np.zeros(shape=(numPts, numPts))
	for i in xrange(numPts):
		for j in xrange(numPts):
			if autocorrelations[i,j] >= threshold:
				windowPairsDetected[i,j] = 1
				#print 'Detected possible window event'
	return windowPairsDetected

windowPairsDetected = detect_window_pairs(network_correlation_coefficient, 3*MAD)

"""save all window pairs as candidate events"""
def get_candidate_events(windowPairsDetected, windows_array):
	numPts = len(windowPairsDetected)
	
	# count number of events
	num_events = 0
	for i in xrange(numPts):
		detection_row = windowPairsDetected[i,:]
		for j in xrange(numPts):
			if detection_row[j]:
				num_events = num_events+1
				break
	candidate_events = np.zeros(shape=(num_events, numPointsInWindow))

	# save windows with events
	counter = 0
	for i in xrange(numPts):
		detection_row = windowPairsDetected[i,:]
		for j in xrange(numPts):
			if detection_row[j]:
				candidate_events[counter,:] = windows_array[i,:]
				counter=counter+1
				break
	return candidate_events


candidate_events_A = get_candidate_events(windowPairsDetected, fakeSignalA)
candidate_events_B = get_candidate_events(windowPairsDetected, fakeSignalB)
candidate_events_C = get_candidate_events(windowPairsDetected, fakeSignalC)

"""processing candidate events more
   take the middle bits only
"""
middle_num_seconds = 5
def get_middle_candidate_events(candidate_events, num_original, num_kept):
	pass

#truncate_candidate_events_A = get_middle_candidate_events(candidate_events_A, 7, middle_num_seconds)

"""
   apply waveform cross-correlation 1
"""
waveform_cc_A = get_correlations(candidate_events_A)
waveform_cc_B = get_correlations(candidate_events_B)
waveform_cc_C = get_correlations(candidate_events_C)
waveform_cc_all = waveform_cc_A + waveform_cc_B + waveform_cc_C

waveform_windowPairsDetected = detect_window_pairs(waveform_cc_all, 2)


waveform_window_events_A = get_candidate_events(waveform_windowPairsDetected, candidate_events_A)
waveform_window_events_B = get_candidate_events(waveform_windowPairsDetected, candidate_events_B)
waveform_window_events_C = get_candidate_events(waveform_windowPairsDetected, candidate_events_C)

print waveform_window_events_A













