students = []
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students.append([roll, name, marks])
        print("Student added successfully!")
    elif choice == "2":
        print("\nStudent Records:")
        for s in students:
            print("Roll No:", s[0], "| Name:", s[1], "| Marks:", s[2])
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
