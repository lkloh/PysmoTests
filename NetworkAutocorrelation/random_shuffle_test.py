import random
import numpy as np

# taken from http://stackoverflow.com/questions/976882/shuffling-a-list-of-objects-in-python

a = range(5)
b = random.sample(a, len(a))
print a, b, "two list same:", a == b
# print: [0, 1, 2, 3, 4] [2, 1, 3, 4, 0] two list same: False

# sample() allows no duplicates.
# Result can be smaller but not larger than the input.
a = range(50)
print 'LIST A:'
print a

b = range(50)
lol = b[10:20]
rand_b = random.sample(lol, len(lol))
print rand_b
for i in np.arange(10,20):
	b[i] = rand_b[i-10]

print 'LIST B:'
print b
print "no duplicates:", a == list(set(b))

try:
	random.sample(a, len(a) + 1)
except ValueError as e:
	print "Nope!", e