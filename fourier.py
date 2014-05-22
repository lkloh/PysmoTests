
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

#amplitudeFreq = [nan]*len(originalSignalTime)
amplitudeFreq = np.zeros([len(originalSignalTime)])
for i in xrange(len(originalSignalFreq)):
	amplitudeFreq[i] = np.sqrt(originalSignalFreq[i].real**2 + originalSignalFreq[i].imag**2)

#filter
B, A = signal.butter(2,[0.03,0.2],btype='bandpass')

w, h = signal.freqz(B,A)
filteredSignalTime = signal.lfilter(B,A,originalSignalTime)

# frequency -> time
# filtered
filteredSignalFrequency = np.fft.fft(filteredSignalTime)

# convered filtered freq signal => amplitude freq signal
amplitudeFilteredFreq = np.zeros([len(filteredSignalFrequency)])
for i in xrange(len(filteredSignalFrequency)):
	amplitudeFilteredFreq[i] = np.sqrt(filteredSignalFrequency[i].real**2 + filteredSignalFrequency[i].imag**2)


ax1 = fig.add_subplot(211)
ax1.plot(originalTime,originalSignalTime,label='Original')
ax1.plot(originalTime,filteredSignalTime,label='Filtered')
ax1.legend(loc="upper right")
ax1.set_title('Amplitude vs Time')


ax2 = fig.add_subplot(212)
ax2.plot(originalFreq/(2*np.pi),amplitudeFreq ,label='Original')
ax2.plot(originalFreq/(2*np.pi),amplitudeFilteredFreq,label='Filtered')
MULTIPLE = 0.7*max(amplitudeFreq)
ax2.plot(w/(2*np.pi),MULTIPLE*np.abs(h),label='Butter Filter')
ax2.legend(loc="upper right")
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

