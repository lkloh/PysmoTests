"""
draw Atlantic Hurricane Tracks for storms that reached Cat 4 or 5.
part of the track for which storm is cat 4 or 5 is shown red.
ESRI shapefile data from http://nationalatlas.gov/mld/huralll.html

copied from http://matplotlib.org/basemap/users/examples.html
"""
import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Lambert Conformal Conic map.
m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,
            urcrnrlon=-20.,urcrnrlat=57.,
            projection='lcc',
            lat_1=20.,lat_2=40.,lon_0=-60.,
            resolution ='l',area_thresh=1000.)

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
m.drawparallels(np.arange(10,70,20),labels=[1,1,0,0])
m.drawmeridians(np.arange(-100,0,20),labels=[0,0,0,1])
plt.title('YOLOSWAG')
plt.show()