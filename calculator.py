
# Calculator Project #

while True: # Main program (WHILE) loop, asks user to enter a valid operator (+, -, *, /) or 'q' to quit 
    op = input("Please enter a valid operator (+, -, *, /) or 'q' to quit the program: ")

    if op == 'q': # If the user enters 'q' then exit program
        print("Exiting program. Bye!")
        exit()

    if op not in ('+', '-', '*', '/'): # If the user enters an invalid operator then ask user to try again
        print(f"'{op}' is not valid. Try again.")
        continue

    
    while True:
        num1_str = input("Please enter the 1st number (integer or float): ") # Prompt user to enter a valid number for the 1st number 
        try:
            num1 = float(num1_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the 1st number.") # Inform user that invalid input was entered

    while True:
        num2_str = input("Please enter the 2nd number (integer or float): ") # Prompt user to enter a valid number for the 2nd number 
        try:
            num2 = float(num2_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the 2nd number.") # Inform user that invalid input was entered
    
    if op == "+": # If the user enters a '+' operator then perform addition with first number and second number 
        answer = num1 + num2
    elif op == "-": # If the user enters a '-' operator then perform subtraction with first number and second number 
        answer = num1 - num2
    elif op == "*": # If the user enters a '*' operator then perform multiplication with first number and second number 
        answer = num1 * num2
    elif op == "/": # If the user enters a '/' operator then perform division with first number and second number 
        if num2 == 0: 
            print("Cannot divide by 0.") # Inform user that 0 cannot be divided by 0
            continue  # Skip, if above statement is untrue
        answer = num1 / num2 

    print(f"The answer is {answer:.3f}") # Prints the overall result

# At the end of each calculation, the user is sent back to the main loop and prompted to enter another operator or 'q' to quit the program