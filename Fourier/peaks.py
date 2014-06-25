from scipy import signal
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"
import matplotlib.pyplot as py


xs = np.arange(0, np.pi, 0.05)
data = np.sin(xs)

peakind = signal.find_peaks_cwt(data, np.arange(1,10))
print peakind
print xs[peakind]
print data[peakind]

fig = py.figure()
fig.suptitle('peaks')
py.plot(xs, data)
py.show()