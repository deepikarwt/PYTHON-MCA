# Update student marks

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 76}
]

try:
    roll = int(input("Enter roll number: "))
    new_marks = float(input("Enter new marks: "))

    found = False

    for student in students:
        if student["roll"] == roll:
            student["marks"] = new_marks
            print("Marks updated successfully.")
            print(student)
            found = True
            break

    if not found:
        print("Student not found.")

except ValueError:
    print("Please enter a valid roll number and marks.")