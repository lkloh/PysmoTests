
from numpy import *
import matplotlib.pyplot as py
from numpy.fft import *
from scipy import signal

ot = arange(-20,20,0.25)
ots = 4*sin(ot/2) + 2.4*cos(ot*8) + 5*cos(ot*2)


# plot origingal signal-vs-time
fig = py.figure()
fig.suptitle('FILTERING FREQUENCIES')

# time -> frequency 
# UNFILTERED
ofs = fft(ots)
of = fftfreq(len(ots), 0.25)

am_freq = [nan]*len(ots)
for i in xrange(len(ofs)):
	am_freq[i] = ofs[i].real**2 + ofs[i].imag**2

#filter
B, A = signal.butter(2,[0.03,0.2],btype='bandpass')

w, h = signal.freqz(B,A)
filteredSignalFrequency = signal.lfilter(B,A,am_freq)

# frequenc -> time
# filtered
filteredSignalTime = ifft(filteredSignalFrequency)

ax1 = fig.add_subplot(211)
ax1.plot(ot,ots,label='Original')
ax1.plot(ot,filteredSignalTime,label='Filtered')
ax1.legend(loc="upper right")
ax1.set_title('Amplitude vs Time')


ax2 = fig.add_subplot(212)
ax2.plot(of,am_freq,label='Original')
ax2.plot(of,filteredSignalFrequency,label='Filtered')
MULTIPLE = 0.7*max(am_freq)
ax2.plot(w,MULTIPLE*h,label='Butter Filter')
ax2.legend(loc="upper right")
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

