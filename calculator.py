def basic_calculator():
    # Get user input for the first NO
    num1 = float(input("Enter the first NO: "))
    
    # Get user input for the second NO
    num2 = float(input("Enter the second NO: "))
    
    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please enter +, -, *, or /.")

# Call the calculator function
basic_calculator()