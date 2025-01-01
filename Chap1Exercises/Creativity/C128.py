# The p-norm of a vector v = (v1, v2, ..., vn) in n-dimensional space is defined as
# magnitude(v) = pth root (v1^p + v2^p + ... + vn^p)
# For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the
# vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of
# sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5.
# Give an implementation of a function named norm such that norm(v,p) returns the p-norm value of v and norm(v) returns
# the Euclidean norm of v. You may assume that v is a list of numbers

def norm(v, p = 2):
    sum_of_elements = 0
    for i in v:
        sum_of_elements += i ** p
    pnorm = (sum_of_elements) ** (1/p)

    print(pnorm)
    return pnorm

v = [4, 3]
norm(v, 3)