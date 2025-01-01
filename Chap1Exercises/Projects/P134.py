# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program
# that will write out the  following sentence one hundred times: “I will never spam my friends  again.” Your program
# should number each of the sentences, and it should  make eight different random-looking typos.

import random
import string


def create_typo(sentence):
    """
    Returns a version of 'sentence' with a small random typo.
    Possible typos:
      1) Random character removed
      2) Random character replaced with another random letter
      3) Two adjacent characters swapped
    """
    # We don't want to make the typo on an empty or 1-char string,
    # so let's ensure the sentence is long enough to handle a swap or removal.
    # But the sentence is pretty long, so it's safe.

    if len(sentence) < 2:
        # If for some reason it's too short, just return the original
        return sentence

    typo_type = random.choice(['remove', 'replace', 'swap'])

    # Convert the sentence to a list of characters so that we
    # can manipulate it more easily.
    chars = list(sentence)

    # Choose a random position in the sentence
    pos = random.randint(0, len(chars) - 1)

    if typo_type == 'remove':
        # Remove the character at 'pos'
        del chars[pos]

    elif typo_type == 'replace':
        # Replace the character at 'pos' with a different random letter
        old_char = chars[pos]
        # Pick a random ASCII letter that is different from the old character
        possible_replacements = (string.ascii_letters
                                 + string.punctuation
                                 + string.digits
                                 + " ")
        new_char = random.choice(possible_replacements)
        while new_char == old_char:
            new_char = random.choice(possible_replacements)
        chars[pos] = new_char

    elif typo_type == 'swap' and pos < len(chars) - 1:
        # Swap the character at 'pos' with the next character
        chars[pos], chars[pos + 1] = chars[pos + 1], chars[pos]

    # Convert the list of characters back to a string
    return "".join(chars)


def main():
    sentence = "I will never spam my friends again."
    num_times = 100
    # Randomly choose 8 unique line numbers (from 1..100) where we insert typos
    lines_with_typos = set(random.sample(range(1, num_times + 1), 8))

    for i in range(1, num_times + 1):
        # Check if the current line should have a typo
        if i in lines_with_typos:
            # Create and print a typo version
            output_sentence = create_typo(sentence)
        else:
            # Print the correct sentence
            output_sentence = sentence

        # Print with line number
        print(f"{i}. {output_sentence}")


if __name__ == "__main__":
    main()
