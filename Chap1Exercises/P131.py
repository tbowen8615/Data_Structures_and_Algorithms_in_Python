# Write a Python program that can “make change.” Your program should  take two numbers as input, one that is a monetary
# amount charged and the  other that is a monetary amount given. It should then return the number  of each kind of bill
# and coin to give back as change for the difference  between the amount given and the amount charged. The values
# assigned to the bills and coins can be based on the monetary system of any current  or former government. Try to
# design your program so that it returns as  few bills and coins as possible.

hundreds, fifties, twenties, tens, fives, ones = 0, 0, 0, 0, 0, 0
quarters, dimes, nickels, pennies = 0, 0, 0, 0

charged = float(input("monetary amount charged: $"))
given = float(input("monetary amount given: $"))

difference = round((given - charged) * 100)
original_difference = difference / 100

while difference != 0:
    if difference >= 10000:
        difference -= 10000
        hundreds += 1
    elif difference >= 5000:
        difference -= 5000
        fifties += 1
    elif difference >= 2000:
        difference -= 2000
        twenties += 1
    elif difference >= 1000:
        difference -= 1000
        tens += 1
    elif difference >= 500:
        difference -= 500
        fives += 1
    elif difference >= 100:
        difference -= 100
        ones += 1
    elif difference >= 25:
        difference -= 25
        quarters += 1
    elif difference >= 10:
        difference -= 10
        dimes += 1
    elif difference >= 5:
        difference -= 5
        nickels += 1
    elif difference >= 1:
        difference -= 1
        pennies += 1

print(f"Your change is ${original_difference} and it is given in the following bills:")
print(f"""
Hundreds: {hundreds}
Fifties: {fifties}
Twenties: {twenties}
Tens: {tens}
Fives: {fives}
Ones: {ones}
Quarters {quarters}
Dimes: {dimes}
Nickels: {nickels}
Pennies: {pennies}""")