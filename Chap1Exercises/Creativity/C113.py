# Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in
# the opposite order than they  were before, and compare this method to an equivalent Python function  for doing the
# same thing.

def reverse_a_list(data):
    new_data = data[::-1]
    print(data)
    print(new_data)
    return new_data

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_a_list(data)