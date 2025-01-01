# Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot
# product of a and b. That is, it returns an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.

def dotProduct(arr1, arr2):
    dot_product = []
    for i in range(len(arr1)):
        dot_product.append(arr1[i] * arr2[i])
    return dot_product

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 2, 2, 2, 2, 2, 2, 2, 2]
print(dotProduct(arr1, arr2))