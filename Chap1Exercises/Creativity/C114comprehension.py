# Write a short Python function that takes a sequence of integer values and  determines if there is a distinct pair of
# numbers in the sequence whose  product is odd.
# List Comprehension syntax: [Expression for Value in Iterable if Condition]

def distinctOddProduct(data):
    odd_numbers = [x for x in data if x % 2 == 1]

    if len(odd_numbers) >= 2:
        print("There is a distinct pair of numbers in data whose product is odd")
        return True
    else:
        print("There is no distinct pair of numbers in data whose product is odd")
        return False

data = [2, 3, 4, 6, 8, 9]

distinctOddProduct(data)