# Python’s random module includes a function choice(data) that returns a  random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parameterization similar to  the built-in range
# function, that return a random choice from the given  range. Using only the randrange function, implement your own
# version  of the choice function.
from random import randrange
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def custom_choice(data):
    random_index = randrange(0, len(data))

    print(data[random_index])
    return data[random_index]

custom_choice(data)