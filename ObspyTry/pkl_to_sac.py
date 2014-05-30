from obspy import read
from obspy import Trace
from obspy import Stream
import os

stream = read('imApkl.pkl', format='PICKLE')

for trace in stream:
	filename = trace.stats.network+'.'+trace.stats.station+'._.'+trace.stats.channel+'.sac'
	# make directory
	if not os.path.exists('sac'):
		os.makedirs('sac')
	trace.write('sac/'+filename, format='SAC') 


