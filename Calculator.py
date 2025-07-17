while True:   # Master loop – lets the whole program run again when reaches the end.

    # 1. Get first number (validated)
    while True:
        try:          # Tells the program to try this and if its true, then break, if not then run again.
            num1 = float(input("Enter first number: "))
            break                       # valid - break out of inner loop
        except ValueError:
            print("Error: please enter a valid number.")

    # 2. Get second number (validated)
    while True:
        try:        # Tells the program to try this and if its true, then break, if not then run again.
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Error: please enter a valid number.")

    # 3. Show menu & validate choice
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1 / 2 / 3 / 4): ")
        if choice in ('1', '2', '3', '4'):
            break
        else:
            print("Error: please choose 1, 2, 3, or 4.")

    
    # 4. Perform the chosen operation
    if choice == '1':                       # Addition
        result = num1 + num2
        print(f"Result: {result}")

    elif choice == '2':                     # Subtraction
        result = num1 - num2
        print(f"Result: {result}")

    elif choice == '3':                     # Multiplication
        result = num1 * num2
        print(f"Result: {result}")

    elif choice == '4':                     # Division (with zero-check)
        while num2 == 0.0:
            print("Error: cannot divide by zero.")
            # Ask again only for the *second* number
            try:
                num2 = float(input("Enter a non-zero second number: "))
            except ValueError:
                print("Error: please enter a valid non-zero number.")
                continue
        result = num1 / num2
        print(f"Result: {result}")
