# Take an integer value and return True if k is even and False otherwise
# Do not use multiplication, modulo, or division operators

def is_even(k):
    while k != 1 and k != 0:
        k -= 2
    if k == 0:
        print("k is even")
        return True
    else:
        print("k is odd")
        return False
is_even(5)