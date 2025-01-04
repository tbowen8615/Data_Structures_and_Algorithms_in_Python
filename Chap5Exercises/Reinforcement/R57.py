# Let A be an array of size n≥2 containing integers from 1 to n−1, inclusive, with exactly one repeated. Describe a
# fast algorithm for finding the  integer in A that is repeated.
#
# Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 224). Wiley Higher Ed. Kindle Edition.

data = [1, 3, 4, 5, 6, 7, 2, 8, 9, 3]

def duplicates(data):           # runs in n^2 time, not efficient for large inputs
    k = 0
    while True:
        for i in range(k+1, len(data)):
            if data[i] == data[k]:
                print(f"The integer that is repeated is {data[i]}")
                return data[i]
        k += 1

duplicates(data)


def duplicates_v2(data):        # runs in n time
    seen = set()
    for i in data:
        if i in seen:
            print(f"The integer that is repeated is {i}")
        seen.add(i)

duplicates_v2(data)