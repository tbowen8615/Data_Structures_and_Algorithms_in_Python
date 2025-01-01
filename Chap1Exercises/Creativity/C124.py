# Write a short Python function that counts the number of vowels in a given character string.

def count_vowels(data):
    vowel_count = 0
    for i in data:
        if i in 'aeiou':
            vowel_count += 1
    print("There are", vowel_count, " vowels in", data)
    return vowel_count

data = "Tyler Bowen is gonna fucking make it bitch"
count_vowels(data)