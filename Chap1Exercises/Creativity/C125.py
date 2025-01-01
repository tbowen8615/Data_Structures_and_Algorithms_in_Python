# Write a short Python function that takes a string s, representing a sentence,  and returns a copy of the string with
# all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return
# "Lets try Mike".

def remove_punctuation(s):
    new_string = ''
    for i in s:
        if i.isalpha() or i.isspace():
            new_string += i
    print(new_string)
    return new_string

s = "Let's try, Mike."
remove_punctuation(s)

def remove_punctuationV2(s):
    new_string = ''.join([char for char in s if char.isalpha() or char.isspace()])
    print(new_string)
    return new_string

remove_punctuationV2(s)