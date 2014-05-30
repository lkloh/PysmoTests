from obspy import read
from obspy import Trace
from obspy import Stream
import numpy as np

f = read('original-sacs/*.sac', format='SAC')


# trace scratch
trace = Trace()
trace.data = f[0].data
trace.stats = f[0].stats
print dir(trace.stats.sac)

stream = Stream(traces=trace)

# write to new sac file
stream.write('fake.sac', format='SAC') 

f.write('imApkl.bhz.pkl', format='PICKLE')

fake_trace = Trace()
fake_trace.data = np.array([1,2,3,4,5])
fake_trace.stats.network = 'TA'
fake_trace.stats.sac = {'dist',12}
