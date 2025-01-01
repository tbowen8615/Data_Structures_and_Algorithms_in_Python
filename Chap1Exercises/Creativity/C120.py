# Python’s random module includes a function shuffle(data) that accepts a  list of elements and randomly reorders the
# elements so that each possible order occurs with equal probability. The random module includes a  more basic function
# randint(a, b) that returns a uniformly random integer  from a to b (including both endpoints). Using only the randint
# function,  implement your own version of the shuffle function.

from random import randint

def custom_shuffle(data):
    for i in range(len(data)):
        j = randint(0, i)
        data[i], data[j] = data[j], data[i]
    return data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
custom_shuffle(data)
print(data)