# Simple Calculator Program

while True:
    print("\n--- Simple Calculator ---")
    print("Available operations: +, -, *, /")
    
    operation = input("Enter the operation you want to perform: ").strip()
    
    # Validate the operation
    if operation not in ['+', '-', '*', '/']:
        print("Error: Invalid operation. Please choose from +, -, *, or /.")
        continue  # Skip to the next iteration
    
    try:
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue  # Skip to the next iteration
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue  # Skip to the next iteration
        result = num1 / num2
    
    print(f"The result of {num1} {operation} {num2} is: {result}")
    
    continue_calc = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if continue_calc != 'y':
        print("Thank you for using the calculator. Goodbye!")
        break  # Exit the loop
