import numpy as np 
import random as rand

fakeSignal = rand.sample(range(-50,50), 20)
delta = 0.5

window = 5
overlap = 1

# transform fakeSignal to sliding windows

totalDataPoints = len(fakeSignal)
numPointsInWindow = window/delta
numPointsInOverlap = overlap/delta

numWindows = int((totalDataPoints-numPointsInWindow)/numPointsInOverlap + 1)
print numWindows