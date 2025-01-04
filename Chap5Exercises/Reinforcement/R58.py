# Experimentally evaluate the efficiency of the pop method of Python’s list  class when using varying indices as a
# parameter, as we did for insert on  page 205. Report your results akin to Table 5.5.
#
# Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 224). Wiley Higher Ed. Kindle Edition.

import time

# Create a list with 100,000 elements
lst = list(range(1000000))

# Timing pop from the end
start = time.time()
lst.pop()  # Pop from the end
end = time.time()
print(f"Time to pop from the end: {end - start:.10f} seconds")

# Reset the list
lst = list(range(1000000))

# Timing pop from the middle
middle_index = len(lst) // 2
start = time.time()
lst.pop(middle_index)  # Pop from the middle
end = time.time()
print(f"Time to pop from the middle: {end - start:.10f} seconds")

# Reset the list
lst = list(range(1000000))

# Timing pop from the beginning
start = time.time()
lst.pop(0)  # Pop from the beginning
end = time.time()
print(f"Time to pop from the beginning: {end - start:.10f} seconds")
