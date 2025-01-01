# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be
# out of bounds. If that index  is out of bounds, the program should catch the exception that results, and  print the
# following error message:  “Don’t try buffer overflow attacks in Python!”

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    input("Choose an index for the data array that you would like to write a new element into")
    index = int(input())

    data[index] = 100
except IndexError:
    print("Don't try buffer overflow attacks in Python!")

