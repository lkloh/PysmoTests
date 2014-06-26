import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"
import matplotlib.pyplot as py

import numpy as npy
from numpy.random import rand

# copied from http://matplotlib.org/examples/event_handling/pick_event_demo.html


x, y, c, s = rand(4, 100)

def onpick3(event):
    ind = event.ind
    print 'onpick3 scatter:', ind, npy.take(x, ind), npy.take(y, ind)

fig = py.figure()
ax1 = fig.add_subplot(111)
col = ax1.scatter(x, y, 100*s, c, picker=True)
#fig.savefig('pscoll.eps')
fig.canvas.mpl_connect('pick_event', onpick3)

py.show()