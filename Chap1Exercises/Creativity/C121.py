# Write a Python program that repeatedly reads lines from standard input  until an EOFError is raised, and then outputs
# those lines in reverse order  (a user can indicate end of input by typing ctrl-D).

def reverseInput():
    try:
        user_input = []
        while True:
            user_input.append(input())

    except EOFError:
        user_input = user_input[::-1]
        for i in range(len(user_input)):
            print(user_input[i])

reverseInput()