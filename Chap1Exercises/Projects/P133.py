# Write a Python program that simulates a handheld calculator. Your program should process input from the Python
# console representing buttons  that are “pushed,” and then output the contents of the screen after each operation is
# performed. Minimally, your calculator should be able to process  the basic arithmetic operations and a reset/clear
# operation.

def run_calculator():
    """
    Runs a simple console-based calculator simulation.
    The calculator accepts the following commands:
      - Digits (0-9) to type numbers
      - +, -, *, / to set the current operation
      - = to apply the pending operation
      - C to clear the calculator
      - Q to quit/exit
    """

    accumulator = 0  # The "screen" once an operation is applied
    current_input = ""  # Digits being typed but not yet applied
    pending_op = None  # One of ['+', '-', '*', '/'] or None

    print("Welcome to the Python Calculator!")
    print("Enter digits (0-9), operators (+ - * /), =, C (clear), or Q (quit).")
    print("Screen:", accumulator)

    while True:
        user_input = input(">> ").strip()  # Read input from the console

        # 1) Handle QUIT
        if user_input.upper() == "Q":
            print("Exiting calculator.")
            break

        # 2) Handle CLEAR
        elif user_input.upper() == "C":
            accumulator = 0
            current_input = ""
            pending_op = None
            print("Screen:", accumulator)

        # 3) Handle DIGITS (0-9) or multi-digit numbers
        elif user_input.isdigit():
            # Append digits to 'current_input' string
            current_input += user_input
            print("Screen:", current_input)

        # 4) Handle OPERATORS (+, -, *, /)
        elif user_input in ['+', '-', '*', '/']:
            # If there is some current_input number typed,
            # apply it to the accumulator (or set accumulator if first time).
            if current_input != "":
                if pending_op is None:
                    # This is the first number typed
                    accumulator = float(current_input)
                else:
                    # Apply the pending operation to the old accumulator
                    accumulator = apply_op(accumulator, float(current_input), pending_op)

                current_input = ""  # Reset the typed number
            pending_op = user_input
            print("Screen:", accumulator)

        # 5) Handle EQUALS (=)
        elif user_input == "=":
            if pending_op is not None and current_input != "":
                accumulator = apply_op(accumulator, float(current_input), pending_op)
                pending_op = None
                current_input = ""
            print("Screen:", accumulator)

        else:
            print("Unknown input. Valid options: digits, +, -, *, /, =, C, Q")


def apply_op(left_operand, right_operand, operator):
    """Helper function to apply a given arithmetic operator."""
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        # Handle division by zero gracefully
        if right_operand == 0:
            print("Error: Division by zero!")
            return left_operand
        return left_operand / right_operand
    return left_operand


if __name__ == "__main__":
    run_calculator()
