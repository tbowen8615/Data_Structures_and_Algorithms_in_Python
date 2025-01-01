# Write a Python program that outputs all possible strings formed by using the characters
# 'c', 'a', 't', 'd', 'o', 'g' exactly once

from itertools import permutations
"""
This was my first attempt. It does not accomplish all permutations, but it was my first thought.
def allPossible(data):
    k = len(data) -1
    while k >= 0:
        for i in range(k):
            data[i], data[i+1] = data[i+1], data[i]
            print(data)
        k -= 1
    return True
"""

def allPermutations(data):
    perm_list = permutations(data)
    num_perms = 0
    for perm in perm_list:
        num_perms += 1
        print(''.join(perm))
    print(num_perms)

data = ['c', 'a', 't', 'd', 'o', 'g']
allPermutations(data)