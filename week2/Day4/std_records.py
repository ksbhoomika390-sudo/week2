students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nEnter details for Student", i + 1)
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    student = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }
    students.append(student)
print("\nStudent Records:")
for s in students:
    print(s)
