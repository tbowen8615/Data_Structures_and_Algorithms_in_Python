# Our implementation of insert for the DynamicArray class, as given in  Code Fragment 5.5, has the following
# inefficiency. In the case when a resize occurs, the resize operation takes time to copy all the elements from
# an old array to a new array, and then the subsequent loop in the body of  insert shifts many of those elements.
# Give an improved implementation  of the insert method, so that, in the case of a resize, the elements are  shifted
# into their final position during that operation, thereby avoiding the  subsequent shifting.
#
# Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 224). Wiley Higher Ed. Kindle Edition.

def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this version)
    if self._n == self._capacity:                 # not enough room
        self._resize(2 * self._capacity)         # so double capacity
    for j in range(self._n, k, -1):              # shift rightmost first
        self._A[j] = self._A[j - 1]
    self._A[k] = value                           # store newest element
    self._n += 1


def new_insert(self, k, value):
    if self._n == self._capacity:
        new_capacity = 2 * self._capacity
        new_array = [None] * new_capacity

        for i in range(k):
            new_array[i] = self._A[i]

        new_array[k] = value

        for i in range(k, self._n):
            new_array[i+1] = self._A[i]

        self._A = new_array
        self._capacity = new_capacity

    else:
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value

    self._n += 1
