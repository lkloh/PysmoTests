from obspy import read
from obspy import Trace
from obspy import Stream

f = read('original-sacs/CI.ADO.__.BHN.sac')

print '#############'
print (f)

print '#############'
print f[0].stats

print '#############'
print f[0].data

print '#############'
print f.plot

print '#############'
print type(f)

# trace scratch
trace = Trace()
trace.data = f[0].data
trace.stats = f[0].stats

stream = Stream(traces=trace)

# write to new sac file
stream.write('fake.sac', format='SAC') 