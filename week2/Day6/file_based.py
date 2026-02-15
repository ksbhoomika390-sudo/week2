while True:
    print("\n--- MENU ---")
    print("1. Add Student Record")
    print("2. View Student Record")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        with open("student.txt", "a") as f:
            f.write(roll + " " + name + " " + marks + "\n")

        print("Record added successfully!")
    elif choice == "2":
        print("\n--- Student Records ---")
        with open("student.txt", "r") as f:
            data = f.read()
            print(data)
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
