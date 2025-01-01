# Write a short program that takes as input three integers, a, b, and c, from  the console and determines if they can
# be used in a correct arithmetic  formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
print("Please type in three integers, a, b, and c")

try:
    a = int(input("Please enter the first integer: "))
    b = int(input("Please enter the second integer: "))
    c = int(input("Please enter the third integer: "))
    print(f"You entered integer 1: {a}, integer 2: {b}, integer 3: {c}")
    if a + b == c:
        print("a + b = c")
    else:
        print("a + b != c")

    if a == b - c:
        print("a = b - c")
    else:
        print("a != b - c")

    if a * b == c:
        print("a * b = c")
    else:
        print("a * b != c")
except ValueError:
    print("Input three integers.")