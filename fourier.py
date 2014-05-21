
from numpy import *
import matplotlib.pyplot as py
from numpy.fft import *
from scipy import signal

ot = arange(-20,20,0.25)
ots = 4*sin(ot/2) + 2.4*cos(ot*8) + 5*cos(ot*2)


# plot origingal signal-vs-time
fig = py.figure()
fig.suptitle('FILTERING FREQUENCIES')

ax1 = fig.add_subplot(211)
ax1.plot(ot,ots)
ax1.set_title('Amplitude vs Time')

ofs = fft(ots)
of = fftfreq(len(ots), 0.25)

#filter
order = 2
lowFreq = 1.0
highFreq = 1.5
B, A = signal.butter(2,[0.5,1.0],btype='bandpass')

print A

w, h = signal.freqz(B,A)
# w, h = signal.freqs(B,A)
ff = signal.lfilter(B,A,ofs)
# 

# print ff

ax2 = fig.add_subplot(212)
ax2.plot(of,ofs,label='Original')
ax2.plot(of,ff,label='Filtered')
ax2.legend(loc="lower left")

ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

