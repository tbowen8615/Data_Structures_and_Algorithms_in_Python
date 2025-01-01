# The birthday paradox says that the probability that two people in a room  will have the same birthday is more than
# half, provided n, the number of  people in the room, is more than 23. This property is not really a paradox,  but
# many people find it surprising. Design a Python program that can test  this paradox by a series of experiments on
# randomly generated birthdays,  which test this paradox for n = 5,10,15,20,...,100.

import random


def has_duplicate_birthday(num_people, days_in_year=365):
    """
    Generate random birthdays for 'num_people' and check if there's a duplicate.
    Returns True if at least two people share the same birthday.
    """
    birthdays = set()
    for _ in range(num_people):
        # Pick a random day out of 365
        day = random.randint(1, days_in_year)
        if day in birthdays:
            # We found a duplicate
            return True
        birthdays.add(day)
    return False


def estimate_collision_probability(num_people, trials=10_000, days_in_year=365):
    """
    Run 'trials' simulations for 'num_people'.
    Returns the fraction of trials in which at least two share a birthday.
    """
    collisions = 0
    for _ in range(trials):
        if has_duplicate_birthday(num_people, days_in_year):
            collisions += 1
    return collisions / trials


def main():
    # We'll test for room sizes in steps of 5, from 5 to 100.
    room_sizes = range(5, 101, 5)

    # Number of trials per room size
    num_trials = 10_000

    print(f"Testing Birthday Paradox with {num_trials} trials per room size.\n")
    print("   n | Estimated Probability of a Shared Birthday")
    print("-----|------------------------------------------")

    for n in room_sizes:
        prob = estimate_collision_probability(n, trials=num_trials)
        # Display a nicely formatted percentage
        print(f"{n:4d} | {prob:>9.4f}  ({prob * 100:>5.1f}%)")


if __name__ == "__main__":
    main()
