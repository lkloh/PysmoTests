import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"

import matplotlib.pyplot as py
from mpl_toolkits.basemap import Basemap
import numpy as np

"""
lower-left/upper-right corners for the cascades domain.
"""
minLat = 40
minLon = -123
maxLat = 47
maxLon = -120

"""
Central lat/lon coordinates.
"""
centerLat = 0.5 * (minLat + maxLat)
centerLon = 0.5 * (minLon + maxLon)

"""make the basemap for cascades region"""
m = Basemap(llcrnrlon=minLon, llcrnrlat=minLat, 
            urcrnrlon=maxLon, urcrnrlat= maxLat,
            resolution='c',
            area_thresh=100.,projection='lcc',
            lat_0=centerLat, lon_0=centerLon)

m.drawstates()
m.drawcountries()
m.drawcoastlines()        

"""attempt to plot pointshere"""
lat_pts = [42,44,45,43,46.5,46,41]
lon_pts = [-120.5,-121.5,-120,-122.5,-122.9,-121.2,-120.1]
data_pts = [-34,-56,21,45,1,-3,30]

m.scatter(lon_pts, lat_pts, latlon=True, marker='o', c=data_pts, cmap=py.cm.RdBu_r, vmin=min(data_pts), vmax=max(data_pts))

# add colorbar
cb = m.colorbar()
cb.set_label('Delay Times') 


#m.drawmapboundary(fill_color='#99ffff')

"""show the map"""
py.show()