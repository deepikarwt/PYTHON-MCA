# Create a list of student records

students = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    print(f"\nEnter details for student {i + 1}")
    roll = int(input("Roll number: "))
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

print("\nStudent records created successfully.")
print(students)