from obspy import read
from obspy import Trace
from obspy import Stream

f = read('original-sacs/*.sac', format='SAC')

print len(f)

# trace scratch
trace = Trace()
trace.data = f[0].data
trace.stats = f[0].stats

stream = Stream(traces=trace)

# write to new sac file
stream.write('fake.sac', format='SAC') 

f.write('imApkl.bhz.pkl', format='PICKLE')