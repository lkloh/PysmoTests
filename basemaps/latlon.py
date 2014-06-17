import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"

from matplotlib import pylab as plt
from mpl_toolkits.basemap import Basemap

"""copied from http://stackoverflow.com/questions/21756671/basemap-unknown-property-latlon
big dot
"""


fig = plt.figure
ax = plt.subplot(111)
m = Basemap(llcrnrlon=-180,
llcrnrlat=-90,urcrnrlon=180,urcrnrlat=90,projection='mill') 
m.drawcoastlines(linewidth=0.65, color='0.3')
x = 30.
y = 50.
m.scatter(x, y, s=50, color='k', latlon=True)   
plt.show()
