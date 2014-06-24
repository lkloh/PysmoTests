
from obspy import read, UTCDateTime, signal
import numpy as np

np.random.seed(123)  # make test reproducable
st = read()
print 'suspected event:\n'
print st

t = UTCDateTime(2009, 8, 24, 0, 20, 7, 700000)
templ = st.copy().slice(t, t+5)
print 'Template:\n'
print templ

for tr in templ:
	tr.data += np.random.random(len(tr)) * tr.data.max() * 0.5
	print signal.cross_correlation.templatesMaxSimilarity(st, t, [templ])
