
from numpy import *
import matplotlib.pyplot as py
from numpy.fft import *
from scipy import signal

originalTime = arange(-20,20,0.25)
originalSignalTime= 4*sin(originalTime/2) + 2.4*cos(originalTime*8) + 5*cos(originalTime*2)


# plot origingal signal-vs-time
fig = py.figure()
fig.suptitle('FILTERING FREQUENCIES')

# time -> frequency 
# UNFILTERED
originalSignalFreq = fft(originalSignalTime)
originalFreq = fftfreq(len(originalSignalTime), 0.25)

amplitudeFreq = [nan]*len(originalSignalTime)
for i in xrange(len(originalSignalFreq)):
	amplitudeFreq [i] = originalSignalFreq[i].real**2 + originalSignalFreq[i].imag**2

#filter
B, A = signal.butter(2,[0.03,0.2],btype='bandpass')

w, h = signal.freqz(B,A)
filteredSignalFrequency = signal.lfilter(B,A,amplitudeFreq)

# frequency -> time
# filtered
filteredSignalTime = ifft(filteredSignalFrequency)

ax1 = fig.add_subplot(211)
ax1.plot(originalTime,originalSignalTime,label='Original')
ax1.plot(originalTime,filteredSignalTime,label='Filtered')
ax1.legend(loc="upper right")
ax1.set_title('Amplitude vs Time')


ax2 = fig.add_subplot(212)
ax2.plot(originalFreq,amplitudeFreq ,label='Original')
ax2.plot(originalFreq,filteredSignalFrequency,label='Filtered')
MULTIPLE = 0.7*max(amplitudeFreq)
ax2.plot(w,MULTIPLE*h,label='Butter Filter')
ax2.legend(loc="upper right")
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

