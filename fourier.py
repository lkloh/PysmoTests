
import numpy as np
import matplotlib.pyplot as py
from scipy import signal

originalTime = np.arange(-20,20,0.25)
originalSignalTime= 4*np.sin(originalTime/2) + 2.4*np.cos(originalTime*8) + 5*np.cos(originalTime*2)

# plot original signal-vs-time
fig = py.figure()
fig.suptitle('FILTERING FREQUENCIES')

# time -> frequency 
# unfiltered
originalSignalFreq = np.fft.fft(originalSignalTime)
originalFreq = np.fft.fftfreq(len(originalSignalTime), 0.25)

#filter the time signal
B, A = signal.butter(2,[0.03,0.2],btype='bandpass')
w, h = signal.freqz(B,A)
filteredSignalTime = signal.lfilter(B,A,originalSignalTime)

# convert filtered time signal -> frequency signal
filteredSignalFreq = np.fft.fft(filteredSignalTime)

# PLOT TIME
ax1 = fig.add_subplot(211)
ax1.plot(originalTime,originalSignalTime,label='Original')
ax1.plot(originalTime,filteredSignalTime,label='Filtered')
ax1.legend(loc="upper right")
ax1.set_title('Amplitude vs Time')

# PLOT FREQUENCY
# in Hertz
ax2 = fig.add_subplot(212)
ax2.plot(originalFreq/(2*np.pi),np.abs(originalSignalFreq),label='Original')
ax2.plot(originalFreq/(2*np.pi),np.abs(filteredSignalFreq),label='Filtered')
MULTIPLE = 0.7*max(np.abs(originalSignalFreq))
ax2.plot(w/(2*np.pi),MULTIPLE*np.abs(h),label='Butter Filter')
ax2.legend(loc="upper right")
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

