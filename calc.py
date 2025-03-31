def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Validate operation
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation! Please restart the program.")
        return

    # Get numbers from user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform calculation based on selected operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")

# Run the calculator
calculator()
### test###
###TEST1##