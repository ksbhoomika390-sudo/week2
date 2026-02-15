while True:
    print("\n---- MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Thank you!")
        break

    if choice >= 1 and choice <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

        elif choice == 4:
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)

    else:
        print("Invalid choice!")
