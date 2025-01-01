# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each
# other (that is, they are distinct).

def areAllDifferent(data):
    data_set = set(data)
    if len(data) == len(data_set):
        print("All numbers in data are different from each other")
    else:
        print("All numbers in data are not different from each other")

data = [2, 3, 4, 5, 6, 7, 8, 9]

areAllDifferent(data)