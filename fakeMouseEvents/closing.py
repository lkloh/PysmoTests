from numpy import *
import matplotlib.pyplot as plt
from scipy import *

t = linspace(0, 0.1,1000)
w = 60*2*pi


fig = plt.figure()
plt.plot(t,cos(w*t))
plt.plot(t,cos(w*t-2*pi/3))
plt.plot(t,cos(w*t-4*pi/3))
plt.show()
plt.close(fig)