# Write a short Python function that takes a sequence of integer values and  determines if there is a distinct pair of
# numbers in the sequence whose  product is odd.

def distinctOddProduct(data):
    odd_count = 0
    for i in data:
        if i % 2 == 1:
            odd_count += 1
    if odd_count >= 2:
        print("There is a distinct pair of numbers in data whose product is odd")
        return True
    else:
        print("There is no distinct pair of numbers in data whose product is odd")
        return False

data = [2, 3, 4, 6, 8, 9]
distinctOddProduct(data)