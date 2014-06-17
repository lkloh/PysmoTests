import matplotlib
matplotlib.rcParams['backend'] = "TkAgg"

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

"""
Equatorial/Polar minor radii for WGS84 ellipsoid
approximation of the geoid
"""
rEquat = 6378137.00
rPolar = 6356752.3142
"""
Standard latitudes for LCC projection.  Used in this
projection by Australia's BoM.
"""
trueLat1 = -10.
trueLat2 = -40.

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

"""
CASE 1:
BoM's projection parameters.  Cuts off W. edge of 
WA and N end of Cape York Peninsula.
"""
m = Basemap(llcrnrlon=ozMinLon, llcrnrlat=ozMinLat, 
            urcrnrlon=ozMaxLon, urcrnrlat= ozMaxLat,
            resolution='c',
            area_thresh=100.,projection='lcc',
            lat_1=trueLat1, lat_2=trueLat2, 
            lat_0=centerLat, lon_0=centerLon)
m.drawstates()
m.drawcountries()
m.drawcoastlines()            
plt.show()