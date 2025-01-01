# Write a function that takes a positive integer n and returns the
# sum of the squares of all the odd positive integers smaller than n

def sumOfSquaresOfOdds(n):
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            sum += i * i
    print(sum)
    return sum

n = 10
sumOfSquaresOfOdds(n)