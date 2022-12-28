# Define a function to get input from the user
def get_input():
    return input("Enter a number or an operator (+, -, *, /): ")

# Define the main loop
while True:
    # Get the first operand
    operand1 = get_input()

    # Check if the user entered an operator
    if operand1 in ["+", "-", "*", "/"]:
        print("Error: Operand expected")
    else:
        # Get the operator
        operator = get_input()

        # Check if the user entered a valid operator
        if operator not in ["+", "-", "*", "/"]:
            print("Error: Invalid operator")
        else:
            # Get the second operand
            operand2 = get_input()

            # Check if the user entered a number
            if operand2 in ["+", "-", "*", "/"]:
                print("Error: Operand expected")
            else:
                # Convert the operands to floats
                operand1 = float(operand1)
                operand2 = float(operand2)

                # Perform the calculation
                if operator == "+":
                    result = operand1 + operand2
                elif operator == "-":
                    result = operand1 - operand2
                elif operator == "*":
                    result = operand1 * operand2
                elif operator == "/":
                    result = operand1 / operand2

                # Print the result
                print(result)
