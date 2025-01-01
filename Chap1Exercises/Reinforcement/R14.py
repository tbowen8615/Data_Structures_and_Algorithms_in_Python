# returns sum of squares of all positive integers less than n

def sumOfSquares(n):
    sum = 0
    for i in range(n):
        sum += i * i
    print(sum)
    return sum

n = 5
sumOfSquares(n)