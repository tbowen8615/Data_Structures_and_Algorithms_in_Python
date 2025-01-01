# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times
# one must repeatedly divide this  number by 2 before getting a value less than 2.

def num_of_divs():
    while True:
        try:
            n = int(input("Please input a positive integer greater than 2: "))
            if n <= 2:
                print("That is not a positive integer greater than 2.")
            else:
                original_input = n
                divs = 0
                while n >= 2:
                    n /= 2
                    divs += 1
                print(f"The number of divisions it takes to reduce {original_input} to less than 2 is {divs}")
                return divs
        except ValueError:
            print("Invalid input. Please input a positive integer greater than 2")

num_of_divs()