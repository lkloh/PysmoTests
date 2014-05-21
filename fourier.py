
from numpy import *
import matplotlib.pyplot as py
from numpy.fft import *

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

ax2 = fig.add_subplot(212)
ax2.plot(of,ofs)
ax2.set_title('Amplitude Spectrum vs frequency')

py.show()

