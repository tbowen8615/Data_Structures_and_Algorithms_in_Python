# Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word
# appears in the list. You  need not worry about efficiency at this point, however, as this topic is  something that
# will be addressed later in this book.

def main():
    # Prompt the user for a line of text.
    user_input = input("Enter a list of words (separated by spaces): ")

    # Split the input on whitespace to get a list of words.
    words = user_input.split()

    # Create a dictionary to store word counts.
    word_counts = {}

    # For each word in the list, update the count in the dictionary.
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print out the results.
    print("\nWord counts:")
    for word, count in word_counts.items():
        print(f"{word} : {count}")

if __name__ == "__main__":
    main()
