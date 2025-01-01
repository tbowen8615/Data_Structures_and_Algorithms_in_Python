# Write a Python program that can simulate a simple calculator, using the  console as the exclusive input and output
# device. That is, each input to the  calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output  to the Python console what would be
# displayed on your calculator.


print("The following is a simple calculator.")
print("Valid inputs are numbers, the operators +, -, /, -, and the equals sign =")
print("Please enter inputs one at a time followed by enter.")
print("When you input an equals sign = the calculation will be performed and output")
print("You may exit the calculator by pressing ctrl + d")

inputs = []

while True:
    try:
        user_input = input("Enter input: ").strip()

        # check if input is the equals sign
        if user_input == "=":
            # Join inputs into a valid Python expression
            try:
                expression = " ".join(inputs)
                result = eval(expression) # evaluate the expression
                print(f"Result: {result}")
                inputs = [] # Clear inputs for the next calculation
            except Exception as e:
                print(f"Error in calculation: {e}")
                inputs = [] # Clear inputs on error
        elif user_input in "+-*/": # Valid operators
            inputs.append(user_input)
        else:
            # Try to convert input to a number and store it
            try:
                number = float(user_input) # Use float for numbers
                inputs.append(str(number))
            except ValueError:
                print("Invalid input. Please enter a number or operator.")
    except EOFError: # Handle exit with ctrl + d
            print("\nExiting calculator. Goodbye!")
            break
