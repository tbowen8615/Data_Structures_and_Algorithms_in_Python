# Give a single command that computes the sum of squares of integers less
# than n relying on Python's comprehension syntax and the built-in sum function

n = 5

total = sum([n * n for n in range(1, n)])

print(total)