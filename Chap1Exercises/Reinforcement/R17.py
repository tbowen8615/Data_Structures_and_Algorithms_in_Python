# Give a single command that computes the sum of squares of odds
# less than n relying on Python's comprehension syntax and the
# built-in sum function

n = 10

total = sum([i * i for i in range(1, n, 2)])

print(total)
