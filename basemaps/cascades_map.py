import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

"""
lower-left/upper-right corners for the Australian domain.
"""
ozMinLat = 40
ozMinLon = -123
ozMaxLat = 47
ozMaxLon = -120

"""
Central lat/lon coordinates.
"""
centerLat = 0.5 * (ozMinLat + ozMaxLat)
centerLon = 0.5 * (ozMinLon + ozMaxLon)

"""make the basemap for cascades region"""
m = Basemap(llcrnrlon=ozMinLon, llcrnrlat=ozMinLat, 
            urcrnrlon=ozMaxLon, urcrnrlat= ozMaxLat,
            resolution='c',
            area_thresh=100.,projection='lcc',
            lat_0=centerLat, lon_0=centerLon)

m.drawstates()
m.drawcountries()
m.drawcoastlines()      
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')   

plt.show()