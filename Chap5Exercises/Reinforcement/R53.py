# Modify the experiment from Code Fragment 5.1 in order to demonstrate  that Python’s list class occasionally shrinks
# the size of its underlying array  when elements are popped from a list.

import sys

data = [0] * 100

for i in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes {1:4d}'.format(a, b))
    data.pop()
