
import numpy as np
import matplotlib.pyplot as py
from scipy import signal

originalTime = np.arange(-20,20,0.25)
originalSignalTime= 4*np.sin(originalTime/2) + 2.4*np.cos(originalTime*8) + 5*np.cos(originalTime*2)


# plot origingal signal-vs-time
fig = py.figure()
fig.suptitle('FILTERING FREQUENCIES')

# time -> frequency 
# UNFILTERED
originalSignalFreq = np.fft.fft(originalSignalTime)
originalFreq = np.fft.fftfreq(len(originalSignalTime), 0.25)

#filter
B, A = signal.butter(2,[0.03,0.2],btype='bandpass')

w, h = signal.freqz(B,A)
filteredSignalTime = signal.lfilter(B,A,originalSignalTime)

# frequency -> time
# filtered
filteredSignalFrequency = np.fft.fft(filteredSignalTime)

ax1 = fig.add_subplot(211)
ax1.plot(originalTime,originalSignalTime,label='Original')
ax1.plot(originalTime,filteredSignalTime,label='Filtered')
ax1.legend(loc="upper right")
ax1.set_title('Amplitude vs Time')

# in Hertz
ax2 = fig.add_subplot(212)
ax2.plot(originalFreq/(2*np.pi),np.abs(originalSignalFreq),label='Original')
ax2.plot(originalFreq/(2*np.pi),np.abs(filteredSignalFrequency),label='Filtered')
MULTIPLE = 0.7*max(amplitudeFreq)
ax2.plot(w/(2*np.pi),MULTIPLE*np.abs(h),label='Butter Filter')
ax2.legend(loc="upper right")
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

