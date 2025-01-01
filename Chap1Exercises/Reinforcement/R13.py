# Take a sequence of one or more numbers and return the smallest and largest
# numbers, in the form of a tuple of length two without using the built-in
# min and max functions

def minmax(data):
    min = data[0]
    max = data[0]

    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i

    print("minimum value is", min)
    print("maximum value is", max)

    minmax = (min, max)
    print(minmax)

    return minmax

data = [1, 2, 3, 4, 5, 6]

minmax(data)