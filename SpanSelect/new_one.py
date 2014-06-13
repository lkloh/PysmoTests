import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

def onselectPeak(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)
    print "Xmin " + str(indmin) + " at index " + str(indmin)
    print "Xmax " + str(indmax) + " at index " + str(indmax)
    ax.fill_between(x[indmin:indmax], -1.0, y[indmin:indmax],facecolor='Red',alpha=0.5)

def onselectLeftContinuum(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)
    print "Leftmin " + str(indmin) + " at index " + str(indmin)
    print "Leftmax " + str(indmax) + " at index " + str(indmax)
    ax.fill_between(x[indmin:indmax], -1.0, y[indmin:indmax],facecolor='Blue',alpha=0.5)

def onselectRightContinuum(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)
    print "Xmin " + str(indmin) + " at index " + str(indmin)
    print "Xmax " + str(indmax) + " at index " + str(indmax)
    ax.fill_between(x[indmin:indmax], -1.0, y[indmin:indmax],facecolor='Blue',alpha=0.5)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, axisbg='#FFFFCC')

x = np.arange(0.0, 10.0, 1.0)
y = [0.0,0.0,0.0,0.0,5.0,0.0,0.0,0.0,0.0,0.0,]

ax.plot(x, y, '-')
ax.set_ylim([-1.0,6.0])

spans = []  # don't let the garbage collector have your spans!

ax.set_title('Press left mouse button and drag Line region')
spans.append(
    SpanSelector(ax, onselectPeak, 'horizontal', useblit=True, rectprops=dict(alpha=0.5, facecolor='red') ))

ax.set_title('Press left mouse button and drag left region of the continuum')
spans.append(
    SpanSelector(ax, onselectLeftContinuum, 'horizontal', useblit=True, rectprops=dict(alpha=0.5, facecolor='blue') ))

ax.set_title('Press left mouse button and drag right region of the continuum')
spans.append(
    SpanSelector(ax, onselectRightContinuum, 'horizontal', useblit=True, rectprops=dict(alpha=0.5, facecolor='blue') ))

plt.show()

print "Task Completed"