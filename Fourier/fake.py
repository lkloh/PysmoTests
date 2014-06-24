import obspy
import numpy as np
from scipy import signal


def matlab_xcorr(longer, shorter):
	return np.convolve(longer, shorter[::-1])

a=[1,2,3,4,5]
b=[5,4,3,2,1]

print matlab_xcorr(a,b)

