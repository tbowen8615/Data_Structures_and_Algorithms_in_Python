# Take two integer values and return True if n is a multiple of m,
# that is n = mi for some integer i, and False otherwise

def is_multiple(n, m):
    if n % m == 0:
        print("n is a multiple of m")
        return True
    else:
        print("n is not a multiple of m")
        return False

is_multiple(10, 5)